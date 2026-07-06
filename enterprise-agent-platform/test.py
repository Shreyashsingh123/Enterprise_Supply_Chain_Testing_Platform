# test_retriever.py

from knowledge_base.retriver import retrieve_all

results = retrieve_all(
    "high risk supplier"
)

for collection, docs in results.items():

    print(f"\n{'='*50}")
    print(collection.upper())
    print('='*50)

    for doc in docs:
        print(doc)
        print("-"*50)