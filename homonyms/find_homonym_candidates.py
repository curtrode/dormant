import pandas as pd, unicodedata, re, difflib, json
from wordfreq import zipf_frequency
D={'inherited_from','borrowed_from','derived_from','learned_borrowing_from','has_root',
   'semi_learned_borrowing_from','orthographic_borrowing_from'}
FAM={'Latin':'Latin','Late Latin':'Latin','Medieval Latin':'Latin','New Latin':'Latin','Vulgar Latin':'Latin',
     'Ancient Greek':'Greek','Proto-Germanic':'Proto-Germanic','Proto-Indo-European':'PIE',
     'Old Norse':'Old Norse','Arabic':'Arabic','Frankish':'Frankish','Hebrew':'Hebrew','Persian':'Persian'}
d=pd.read_parquet('en.parquet')
d=d[d.reltype.isin(D)&d.related_term.notna()]
terms=[t for t in d.term.unique() if isinstance(t,str) and re.fullmatch(r'[a-z]+',t)]
keep={t:zipf_frequency(t,'en') for t in terms}
keep={t:z for t,z in keep.items() if z>=3.0}
d=d[d.term.isin(keep)]
def norm(t):
    t=re.sub(r'\(.*?\)','',t).replace('*','').replace('-','').strip().lower()
    t=unicodedata.normalize('NFKD',t); return ''.join(c for c in t if not unicodedata.combining(c))
def distinct(ts):
    reps=[]
    for raw in ts:
        n=norm(raw)
        if not n: continue
        if not any(difflib.SequenceMatcher(None,n,r[1]).ratio()>=0.8 for r in reps): reps.append((raw,n))
    return [r[0] for r in reps]
dormant=set()
for e in json.load(open('dormant/canonical.json'))['entries']:
    dormant.add(e['word'].lower()); dormant.update(f['word'].lower() for f in e.get('forms',[]))
rows=[]
for w,g in d.groupby('term'):
    split={}
    for fam in set(FAM.values()):
        ts=distinct(dict.fromkeys(g[g.related_lang.map(FAM)==fam].related_term))
        if len(ts)>=2: split[fam]=ts
    oe=[t for t in dict.fromkeys(g[g.related_lang=='Old English'].related_term)]
    fr=[t for t in dict.fromkeys(g[g.related_lang.isin(['Old French','Anglo-Norman','Middle French'])].related_term)]
    if oe and fr and all(difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()<0.6 for a in oe for b in fr):
        split['Old English vs French']=[oe[0],fr[0]]
    if not split: continue
    minratio=min(difflib.SequenceMatcher(None,norm(a),norm(b)).ratio() for v in split.values() for i,a in enumerate(v) for b in v[i+1:])
    tier='A' if (len(split)>=2 or minratio<0.45) else 'B'
    rows.append({'tier':tier,'word':w,'zipf':round(keep[w],2),'split_in':', '.join(sorted(split)),
                 'distinct_etyma':' | '.join(f'{f}: '+' / '.join(v) for f,v in sorted(split.items())),
                 'in_dormant':w in dormant})
out=pd.DataFrame(rows).sort_values(['tier','zipf'],ascending=[True,False])
out.to_csv('candidates_raw.csv',index=False)
print(len(out)); print(out.split_in.value_counts().head(8))
test=['bank','mint','grave','school','sound','date','host','quarry','policy','fair','temple','bark','cleave','kind','salary','pupil']
print(out[out.word.isin(test)][['tier','word','distinct_etyma']].to_string()); print(out.tier.value_counts())
for t in 'AB': print(t, ', '.join(out[out.tier==t].sample(40,random_state=1).word))
print('missing:',[w for w in test if w not in set(out.word)])
