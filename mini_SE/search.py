import spacy 

nlp = spacy.load("en_core_web_sm")

STOPWORDS = {"is", "the", "a", "an", "and", "to", "of", "for"}

def preprocess(text):
    doc = nlp(text.lower())
    return [token.lemma_ 
            for token in doc 
            if token.is_alpha and token.text not in STOPWORDS]

def load_documets():
    with open("documents.txt", "r") as f:
        return f.readlines() 

def score(query_tokens, doc_tokens):
    score = 0 
    for token in query_tokens:
        if token in doc_tokens:
            score += 2  # match bonus 
    return score 
            
def search(query, documents):
    query_tokens = preprocess(query)


    results = [] 

    for doc in documents:
        doc_tokens = preprocess(doc)
        s = score(query_tokens, doc_tokens)
        results.append((s, doc.strip()))


    results.sort(reverse=True, key= lambda x: x[0])

    return results 

# ---- run -----
docs = load_documets() 


while True:
    q = input("\nSearch: ")
    results = search(q, docs)

    if results[0][0] == 0:
        print("\nNo relevant results found.")
        continue

    print("\nTop results")
    # // note  here we renamed for score ... to for s, ... as it made a type conflict with score() 
    for s, text in results[:3]:
        print(f"[{s}] {text}")
