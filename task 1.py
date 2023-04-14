Doc_1 = "new home ho sales top forecasts"
Doc_2 = "home sales home rise in July"
Doc_3 = "increase in home sales in July"
Doc_4 = "July new home sales rise"

Docs =[Doc_1,Doc_2,Doc_3,Doc_4]
print(Docs)

unique_terms= set()
for doc in Docs:
    for term in doc.split():
        unique_terms.add(term)

inverted_index = {}
for i, doc in enumerate(Docs):
    for term in unique_terms:
        if term in inverted_index:
            inverted_index[term].add(i)
        else: inverted_index[term] = {i}

term_=input("Enter the word or the term:")
posting_list = inverted_index[term_]
print(posting_list)
