from keybert import KeyBERT

doc = "A cheat version of Hainanese chicken, poached and seasoned with soy sauce and oyster sauce, resulting in tender, flavourful and juicy meat"

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc, use_mmr=True, keyphrase_ngram_range=(2, 2), nr_candidates=20, top_n=3, diversity=0.3)

print(keywords)