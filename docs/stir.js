// The matching and stirring engine shared by index.html (reading) and
// write.html (writing): lemmatizes surface words, looks them up in the
// lexicon, inflects glosses to agree, and renders text into stirrable layers.
// Load after lexicon.js; exposes window.DORMANT.
(function(){
  "use strict";
  var L = window.LEXICON || [];

  // Build lookup by word (lowercase).
  var MAP = {};
  L.forEach(function(e){ MAP[e.word.toLowerCase()] = e; });

  // Candidate lemmas for a surface token, each tagged with the inflection
  // that produced it (lightweight morphology). "s" is ambiguous (plural noun
  // or 3rd-person verb) and resolved later by part of speech.
  // Irregular verb forms the suffix rules cannot reach.
  var IRREG_FORMS = {wrote:"write", written:"write", sold:"sell", paid:"pay"};

  function lemmas(w){
    w = w.toLowerCase();
    var out = [{base:w, infl:"base"}];
    if(IRREG_FORMS[w]) out.push({base:IRREG_FORMS[w], infl:"ed"});
    function undouble(stem, infl){                  // cancelled -> cancel
      if(/([^aeiou])\1$/.test(stem)) out.push({base:stem.slice(0,-1), infl:infl});
    }
    if(w.length > 3){
      if(w.slice(-2) === "'s") out.push({base:w.slice(0,-2), infl:"poss"});
      if(w.slice(-3) === "ies") out.push({base:w.slice(0,-3)+"y", infl:"es"});
      if(w.slice(-2) === "es")  out.push({base:w.slice(0,-2), infl:"es"});
      if(w.slice(-1) === "s")   out.push({base:w.slice(0,-1), infl:"s"});
      if(w.slice(-3) === "ing"){ out.push({base:w.slice(0,-3), infl:"ing"}); out.push({base:w.slice(0,-3)+"e", infl:"ing"}); undouble(w.slice(0,-3), "ing"); }
      if(w.slice(-3) === "ied") out.push({base:w.slice(0,-3)+"y", infl:"ed"});  // replied -> reply
      if(w.slice(-2) === "ed"){ out.push({base:w.slice(0,-2), infl:"ed"}); out.push({base:w.slice(0,-1), infl:"ed"}); out.push({base:w.slice(0,-2)+"e", infl:"ed"}); undouble(w.slice(0,-2), "ed"); }
    }
    return out;
  }

  // Words that signal a verb follows ("they answer", "to answer", "did not answer").
  var VERB_CUES = {i:1, you:1, we:1, they:1, he:1, she:1, it:1, to:1, will:1, would:1, shall:1,
                   should:1, can:1, could:1, may:1, might:1, must:1, did:1, do:1, does:1, not:1,
                   never:1, also:1, "don't":1, "doesn't":1, "didn't":1, "won't":1, "can't":1,
                   "wouldn't":1, "i'll":1, "we'll":1, "you'll":1};
  // A noun entry with a verb_gloss switches to it when the word is used as a
  // verb: always after -ed/-ing, and after a verb cue for the bare or -s form.
  function asVerb(entry, infl, before){
    if(!entry.verb_gloss) return entry;
    var cue = before && VERB_CUES[before.toLowerCase()];
    if(infl === "ed" || infl === "ing" || (cue && (infl === "base" || infl === "s" || infl === "es"))){
      var v = {}; for(var k in entry) v[k] = entry[k];
      v.gloss = entry.verb_gloss; v.part_of_speech = "verb"; delete v.plural;
      return v;
    }
    return entry;
  }

  function lookup(token){
    var ls = lemmas(token);
    for(var i=0;i<ls.length;i++){ if(MAP[ls[i].base]) return {entry:MAP[ls[i].base], infl:ls[i].infl}; }
    return null;
  }

  // Inflect the gloss to agree with the surface word. Verbs inflect their
  // first word (count -> counted); nouns inflect their last word (eye -> eyes).
  var IRREG_PLURAL = {mouse:"mice", man:"men"};
  var IRREG_PAST   = {make:"made", come:"came", take:"took", cut:"cut", put:"put", sit:"sat",
                      swear:"swore", slip:"slipped", unbuild:"unbuilt", send:"sent", see:"saw",
                      say:"said", sing:"sang", give:"gave", strike:"struck", go:"went", tread:"trod", hang:"hung", throw:"threw"};
  var IRREG_GERUND = {cut:"cutting", put:"putting", sit:"sitting", slip:"slipping"};
  var NO_INFLECT_VERB = {from:1};                    // gloss not headed by a verb (desire -> from the stars)
  var NO_INFLECT   = {money:1, news:1, pain:1, white:1, hand:1, salt:1}; // mass/adjectival heads

  function pluralize(w){
    if(IRREG_PLURAL[w]) return IRREG_PLURAL[w];
    if(NO_INFLECT[w]) return w;
    if(/(s|x|z|ch|sh)$/.test(w)) return w + "es";
    if(/[^aeiou]y$/.test(w)) return w.slice(0,-1) + "ies";
    return w + "s";
  }
  function past(w){
    if(IRREG_PAST[w]) return IRREG_PAST[w];
    if(/e$/.test(w)) return w + "d";
    if(/[^aeiou]y$/.test(w)) return w.slice(0,-1) + "ied";
    return w + "ed";
  }
  function gerund(w){
    if(IRREG_GERUND[w]) return IRREG_GERUND[w];
    if(/[^aeiou]e$/.test(w)) return w.slice(0,-1) + "ing";
    return w + "ing";
  }
  function thirdPerson(w){
    if(/(s|x|z|ch|sh)$/.test(w)) return w + "es";
    if(/[^aeiou]y$/.test(w)) return w.slice(0,-1) + "ies";
    return w + "s";
  }

  function inflectGloss(entry, infl){
    var gloss = entry.gloss;
    if(!gloss) return gloss;
    var pos = entry.part_of_speech;
    if(pos === "verb") gloss = gloss.replace(/^to /, "");      // "to sit before" -> "sit before" in running text
    if((infl === "s" || infl === "es") && pos === "noun" && entry.plural) return entry.plural; // cuttings off
    if(infl === "s" || infl === "es") gloss = gloss.replace(/^an? /, ""); // plural nouns drop "a": verdicts -> truly said things
    if(infl === "base") return gloss;
    if(pos === "adjective") return gloss;            // shining white, of cattle — leave as-is
    var words = gloss.split(" ");
    var isVerb = (pos === "verb");
    var hi = isVerb ? 0 : words.length - 1;          // head-word index
    var head = words[hi].toLowerCase(), out = head;
    if(isVerb){
      if(NO_INFLECT_VERB[head]) return gloss;
      if(infl === "ed") out = past(head);
      else if(infl === "ing") out = gerund(head);
      else if(infl === "s" || infl === "es") out = thirdPerson(head);
      else return gloss;                             // possessive on a verb: skip
    } else {                                         // noun
      if(infl === "s" || infl === "es") out = pluralize(head);
      else if(infl === "poss") out = (NO_INFLECT[head] ? head : head + "'s");
      else return gloss;                             // -ed/-ing on a noun: skip
    }
    if(out === head) return gloss;                   // NO_INFLECT head, no change
    words[hi] = out;
    return words.join(" ");
  }

  function matchCase(sample, target){
    if(!sample) return target;
    if(sample[0] === sample[0].toUpperCase() && sample[0] !== sample[0].toLowerCase()){
      return target.charAt(0).toUpperCase() + target.slice(1);
    }
    return target;
  }

  // A determiner right before a recovered word makes the gloss's own article
  // redundant ("the hospital" -> "the guest-house", not "the a guest-house").
  var DETERMINERS = {a:1, an:1, the:1, his:1, her:1, its:1, their:1, my:1, your:1, our:1,
                     this:1, that:1, these:1, those:1, some:1, every:1, each:1, no:1, any:1,
                     another:1, whose:1};
  function takesAn(g){ return /^[aeiou]/i.test(g) && !/^one\b/i.test(g); }

  function esc(s){ return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

  var TOKEN = /[A-Za-z]+(?:'[A-Za-z]+)?|[^A-Za-z]+/g;

  // Stirring: each recovered word holds its layers in stir order (word, root,
  // image) and cycles through them. The Stir view starts every word at its
  // word; the Translate view starts at the image. render() returns this state
  // keyed by match id, rebuilt on every render.
  var LAYER_CLASS = {gloss:"gloss", word:"word", ety:"ety", contested:"contested"};

  function render(text, view){
    var out = [], src = [], tokens = text.match(TOKEN) || [], n = 0;
    var STIR = {};
    var prev = null, prevIdx = -1;                   // last plain word, if only whitespace follows it
    for(var i=0;i<tokens.length;i++){
      var t = tokens[i];
      if(!/[A-Za-z]/.test(t)){
        if(!/^\s+$/.test(t)) prev = null;
        out.push(esc(t)); src.push(esc(t)); continue;
      }
      var m = lookup(t), before = prev, e = m && asVerb(m.entry, m.infl, before);
      prev = null;
      if(e){
        var id = "m"+(n++), layers, art = before && /^an?$/i.test(before);
        var ety = e.etymon && e.etymon.toLowerCase() !== e.word.toLowerCase()   // nostalgia: root looks the same
                ? {text:matchCase(t, e.etymon), kind:"ety"} : null;
        if(e.recovery_type === "contested"){
          layers = [{text:t, kind:"contested"}].concat(ety ? [ety] : []);
        } else {
          var g = inflectGloss(e, m.infl);
          if(before && DETERMINERS[before.toLowerCase()]) g = g.replace(/^(a|an|the) /, "");
          layers = [{text:t, kind:"word"}].concat(ety ? [ety] : [], [{text:matchCase(t, g), kind:"gloss"}]);
        }
        var start = (view === "translate" && layers[layers.length-1].kind === "gloss") ? layers.length-1 : 0;
        STIR[id] = {layers:layers, at:start, start:start};
        if(art) out[prevIdx] = '<span class="art" data-art="'+id+'">'
                             + matchCase(before, takesAn(layers[start].text) ? "an" : "a") + '</span>';
        var stir = layers.length > 1 ? ' data-stir tabindex="0" role="button"' : '';
        out.push('<span class="w '+LAYER_CLASS[layers[start].kind]+'" data-id="'+id+'"'+stir
               + (e.recovery_type === "contested" ? ' data-kind="contested"' : '')
               + ' data-word="'+esc(e.word)+'"'
               + ' data-gloss="'+esc(e.gloss||"")+'" data-ety="'+esc(e.etymon||"")+'"'
               + ' data-lang="'+esc(e.language||"")+'" data-rt="'+esc(e.recovery_type||"")+'"'
               + ' data-base="'+esc(e.base||"")+'">'+esc(layers[start].text)+'</span>');
        src.push('<span class="w src" data-id="'+id+'">'+esc(t)+'</span>');
      } else {
        prev = t; prevIdx = out.length;
        out.push(esc(t)); src.push(esc(t));
      }
    }
    return {out:out.join(""), src:src.join(""), count:n, stir:STIR};
  }

  window.DORMANT = {MAP:MAP, TOKEN:TOKEN, LAYER_CLASS:LAYER_CLASS, lookup:lookup,
                    asVerb:asVerb, render:render, matchCase:matchCase, takesAn:takesAn, esc:esc};
})();
