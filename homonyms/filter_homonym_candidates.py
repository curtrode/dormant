"""Cut dormant_homonym_candidates.csv to words Wiktionary splits into separate etymologies.

Wiktionary numbers the etymologies of a spelling it treats as several words
(Etymology 1, Etymology 2, ...). A section counts when it holds a current sense
(not obsolete, archaic, rare or dialectal; not an abbreviation or proper noun)
and is not built on another section: "from the noun (see above)", an agent noun
or participle (river "one who rives", felt "perceived"), or a phrase containing
the word itself (have on, gold master). Sections that descend from the same
Latin, Greek or Germanic word (matched by shared stem; Middle English, French
and PIE forms are ignored) are one history. A candidate survives with two or
more histories. Output: dormant_homonym_shortlist.csv, one row per word with
the first current sense and origin of each history.

Usage: python3 filter_homonym_candidates.py [cache.json]
Page wikitext is fetched from the Wiktionary API once and kept in the cache
(default wiktionary_cache.json in the working directory; keep it out of the repo).
"""
import csv, json, os, re, sys, time, unicodedata, urllib.error, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = sys.argv[1] if len(sys.argv) > 1 else 'wiktionary_cache.json'
POS = {'Noun', 'Verb', 'Adjective', 'Adverb', 'Interjection', 'Preposition', 'Conjunction',
       'Pronoun', 'Determiner', 'Numeral', 'Particle', 'Article', 'Contraction', 'Phrase'}
DEAD = {'obsolete', 'archaic', 'rare', 'dialectal', 'dialect', 'nonstandard', 'historical',
        'dated', 'poetic', 'nonce word', 'misspelling', 'eye dialect', 'Middle English'}
FORM_OF = re.compile(r'\{\{(abbreviation of|abbr of|initialism of|init of|acronym of|alternative form of|'
                     r'alt form|alt sp|alternative spelling of|misspelling of|obsolete form of|archaic form of|'
                     r'obsolete spelling of|archaic spelling of|dialectal form of|pronunciation spelling of|'
                     r'eye dialect of|inflection of|plural of|en-past of|en-third-person singular of|'
                     r'past participle of|present participle of|en-ing form of|en-simple past of)\|', re.I)
LANG = {'enm': 'Middle English', 'ang': 'Old English', 'fro': 'Old French', 'frm': 'Middle French',
        'fr': 'French', 'xno': 'Anglo-Norman', 'la': 'Latin', 'la-lat': 'Late Latin', 'la-med': 'Medieval Latin',
        'la-vul': 'Vulgar Latin', 'LL.': 'Late Latin', 'ML.': 'Medieval Latin', 'VL.': 'Vulgar Latin',
        'la-new': 'New Latin', 'NL.': 'New Latin', 'grc': 'Ancient Greek', 'non': 'Old Norse',
        'gem-pro': 'Proto-Germanic', 'gmw-pro': 'Proto-West Germanic', 'ine-pro': 'PIE', 'ar': 'Arabic',
        'fa': 'Persian', 'he': 'Hebrew', 'nl': 'Dutch', 'dum': 'Middle Dutch', 'gml': 'Middle Low German',
        'odt': 'Old Dutch', 'de': 'German', 'goh': 'Old High German', 'it': 'Italian', 'es': 'Spanish',
        'pt': 'Portuguese', 'frk': 'Frankish', 'gem': 'Germanic', 'sv': 'Swedish', 'da': 'Danish',
        'is': 'Icelandic', 'sco': 'Scots', 'en': 'English', 'cel-pro': 'Proto-Celtic', 'ga': 'Irish',
        'cy': 'Welsh', 'sa': 'Sanskrit', 'tr': 'Turkish', 'ota': 'Ottoman Turkish', 'hi': 'Hindi',
        'ja': 'Japanese', 'zh': 'Chinese', 'rom': 'Romani', 'yi': 'Yiddish', 'pro': 'Old Occitan',
        'oc': 'Occitan', 'ONF.': 'Old Northern French', 'fro-nor': 'Old Northern French'}
ETY_TEMPLATES = {'inh', 'inh+', 'der', 'der+', 'bor', 'bor+', 'lbor', 'slbor', 'm', 'l', 'cog', 'ncog',
                 'uder', 'ubor', 'calque', 'cal', 'sl', 'semantic loan', 'obor', 'psm', 'm+', 'noncog'}


def fetch(words):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = [w for w in words if w not in cache]
    for i in range(0, len(todo), 50):
        q = urllib.parse.urlencode({'action': 'query', 'prop': 'revisions', 'rvprop': 'content',
                                    'rvslots': 'main', 'format': 'json', 'formatversion': '2',
                                    'titles': '|'.join(todo[i:i + 50])})
        req = urllib.request.Request('https://en.wiktionary.org/w/api.php?' + q,
                                     headers={'User-Agent': 'dormant-homonyms/0.1 (research script)'})
        for attempt in range(8):
            try:
                data = json.load(urllib.request.urlopen(req, timeout=60))
                break
            except urllib.error.HTTPError as e:
                if e.code != 429:
                    raise
                time.sleep(int(e.headers.get('Retry-After') or 0) or 15 * (attempt + 1))
        else:
            raise SystemExit('Wiktionary kept refusing requests; rerun later to resume from the cache.')
        for p in data['query']['pages']:
            cache[p['title']] = p['revisions'][0]['slots']['main']['content'] if 'revisions' in p else None
        json.dump(cache, open(CACHE, 'w'))
        time.sleep(4)
    return cache


def english(text):
    m = re.search(r'^==English==\s*$', text or '', re.M)
    if not m:
        return ''
    rest = text[m.end():]
    n = re.search(r'^==[^=].*==\s*$', rest, re.M)
    return rest[:n.start()] if n else rest


def template_text(inner):
    parts = [p for p in inner.split('|') if '=' not in p or p.startswith('=')]
    name = parts[0].strip()
    if name in ETY_TEMPLATES:
        if name in ('m', 'l', 'm+'):
            lang, word, gloss = parts[1] if len(parts) > 1 else '', parts[2] if len(parts) > 2 else '', parts[4] if len(parts) > 4 else ''
            lang = '' if lang == 'en' else LANG.get(lang, lang) + ' '
        else:
            lang, word, gloss = parts[2] if len(parts) > 2 else '', parts[3] if len(parts) > 3 else '', parts[5] if len(parts) > 5 else ''
            lang = LANG.get(lang, lang) + ' '
        word = re.sub(r'<.*?>', '', word)
        return f'{lang}{word}' + (f' “{gloss}”' if gloss else '')
    if name in ('gloss', 'gl'):
        return f'({parts[1]})' if len(parts) > 1 else ''
    if name in ('lb', 'lbl', 'label', 'q', 'qualifier', 'i', 'sense'):
        return ''
    if name in ('w', 'W'):
        return parts[1] if len(parts) > 1 else ''
    if name in ('unk', 'unknown'):
        return 'Unknown'
    if name in ('unc', 'uncertain'):
        return 'Uncertain'
    if name in ('onomatopoeic', 'onom'):
        return 'Onomatopoeic'
    if name in ('clipping', 'clip', 'back-formation', 'bf', 'blend', 'short for'):
        return f'{name.capitalize()} of ' + ' + '.join(p for p in parts[2:] if p)
    if name in ('compound', 'com', 'af', 'affix', 'suffix', 'prefix', 'confix'):
        return ' + '.join(p for p in parts[2:] if p)
    return ''


def plain(wikitext):
    s = re.sub(r'<ref[^>]*/>|<ref.*?</ref>|<!--.*?-->', '', wikitext, flags=re.S)
    s = re.sub(r'\[\[(?:File|Image):[^\[\]]*(?:\[\[[^\]]*\]\][^\[\]]*)*\]\]', '', s)
    for _ in range(4):
        s = re.sub(r'\{\{([^{}]*)\}\}', lambda m: template_text(m.group(1)), s)
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', s)
    s = re.sub(r"'''?|<[^>]+>", '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'\s+([,.;:)])', r'\1', s)
    return s


DEEP_SKIP = {'en', 'enm', 'fro', 'frm', 'fr', 'xno', 'ine-pro', 'ONF.', 'fro-nor'}
ETYMON = re.compile(r'\{\{(?:inh\+?|der\+?|bor\+?|lbor|slbor|uder|ubor|obor|calque|cal|psm)\|en\|([^|}]+)\|([^|}]*)')
BUILT_ON = re.compile(r'see above|from the (?:noun|verb|adjective)\b|etymology \d', re.I)
AGENT = re.compile(r'^(?:\w+: )?(?:one who|a person who|someone who|something that|that which|that has been)\b', re.I)
AFFIXED = re.compile(r'\+ -?(?:er|ed|ing|s)\b')


def norm(t):
    t = re.sub(r'<.*?>|\(.*?\)|[*\-]', '', t).strip().lower()
    return ''.join(c for c in unicodedata.normalize('NFKD', t) if not unicodedata.combining(c))


def deep_etyma(ety):
    out = set()
    for m in ETYMON.finditer(ety):
        lang, word = m.groups()
        if lang not in DEEP_SKIP and norm(word):
            out.add((LANG.get(lang, lang).split()[-1], norm(word)))
    return out


def related(a, b):
    for la, wa in a:
        for lb, wb in b:
            shared = len(os.path.commonprefix([wa, wb]))
            if la == lb and shared >= 3 and shared >= 0.8 * min(len(wa), len(wb)):
                return True
    return False


def on_itself(word, origin):
    """True when the origin opens with an English phrase containing the word (have on, gold master)."""
    m = re.match(r'(?:Probably |Perhaps |Possibly )?(?:From|Clipping of|Shortening (?:of|from)|Short for)\s+(?:the\s+)?([^,;“]*)', origin)
    head = m.group(1) if m else ''
    langs = sorted(set(LANG.values()), key=len, reverse=True)
    return bool(head) and not any(head.startswith(l) for l in langs) and \
        bool(re.search(rf'\b{re.escape(word)}\b', head, re.I))


def histories(word, live):
    """Group independent live sections into separate histories."""
    own = [e for e in live if not (BUILT_ON.search(e['raw']) or AFFIXED.search(e['origin']) or
                                   (not e['origin'] and AGENT.match(e['senses'][0][1])) or
                                   on_itself(word, e['origin']))]
    groups = []
    for e in own:
        for g in groups:
            if any(related(e['etyma'], f['etyma']) for f in g):
                g.append(e)
                break
        else:
            groups.append([e])
    return groups


def first_sentence(s, limit=240):
    m = re.match(r'(.+?[.;])(\s|$)', s)
    s = m.group(1) if m else s
    return s if len(s) <= limit else s[:limit - 1].rstrip() + '…'


def live_senses(body):
    """Current definitions in this section's part-of-speech blocks."""
    senses = []
    for block in re.split(r'^====\s*', body, flags=re.M)[1:]:
        head = block.split('=', 1)[0].strip()
        if head not in POS:
            continue
        for line in re.findall(r'^#(?![#:*])\s*(.+)$', block, re.M):
            labels = set()
            for lb in re.findall(r'\{\{(?:lb|lbl|label)\|en\|([^}]*)\}\}', line):
                labels.update(x.strip() for x in lb.split('|'))
            if labels & DEAD or FORM_OF.search(line):
                continue
            text = plain(line)
            if text:
                senses.append((head, text))
    return senses


def etymologies(text):
    parts = re.split(r'^===\s*Etymology(?:\s+\d+)?\s*===\s*$', english(text), flags=re.M)
    out = []
    for body in parts[1:]:
        ety = re.split(r'^=', body, flags=re.M)[0]
        senses = live_senses(body)
        out.append({'origin': first_sentence(plain(ety)), 'senses': senses,
                    'rfv': '{{rfv' in ety, 'raw': ety, 'etyma': deep_etyma(ety)})
    return out


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'dormant_homonym_candidates.csv'))))
    pages = fetch([r['word'] for r in rows])
    out = []
    for r in rows:
        ety = etymologies(pages.get(r['word']))
        live = [e for e in ety if e['senses'] and not e['rfv']]
        groups = histories(r['word'], live)
        if len(groups) < 2:
            continue
        rec = {'word': r['word'], 'zipf': r['zipf'], 'in_dormant': r['in_dormant'],
               'wiktionary_etymologies': len(ety), 'histories': len(groups)}
        for i, e in enumerate([g[0] for g in groups][:4], 1):
            rec[f'origin_{i}'] = e['origin']
            rec[f'sense_{i}'] = f'{e["senses"][0][0].lower()}: {first_sentence(e["senses"][0][1], 160)}'
        out.append(rec)
    out.sort(key=lambda x: -float(x['zipf']))
    fields = ['word', 'zipf', 'in_dormant', 'wiktionary_etymologies', 'histories'] + \
             [f'{k}_{i}' for i in range(1, 5) for k in ('sense', 'origin')]
    with open(os.path.join(HERE, 'dormant_homonym_shortlist.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    print(f'{len(out)} of {len(rows)} candidates have two or more separate histories on Wiktionary')


if __name__ == '__main__':
    main()
