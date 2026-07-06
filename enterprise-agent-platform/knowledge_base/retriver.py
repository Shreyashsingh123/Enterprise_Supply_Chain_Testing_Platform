# knowledge_base/retriever.py

import chromadb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

client = chromadb.PersistentClient(
    path=str(BASE_DIR / "vector_store")
)


def retrieve(
    collection_name: str,
    query: str,
    n_results: int = 5
):

    collection = client.get_collection(
        name=collection_name
    )

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results["documents"][0]


def retrieve_suppliers(
    query: str,
    n_results: int = 5
):

    return retrieve(
        "suppliers",
        query,
        n_results
    )


def retrieve_inventory(
    query: str,
    n_results: int = 5
):

    return retrieve(
        "inventory",
        query,
        n_results
    )


def retrieve_orders(
    query: str,
    n_results: int = 5
):

    return retrieve(
        "orders",
        query,
        n_results
    )


def retrieve_shipments(
    query: str,
    n_results: int = 5
):

    return retrieve(
        "shipments",
        query,
        n_results
    )

def retrieve_disruptions(
    query: str,
    n_results: int = 5
):

    return retrieve(
        "disruptions",
        query,
        n_results
    )


def retrieve_all(
    query: str,
    n_results: int = 3
):

    collections = [
        "suppliers",
        "inventory",
        "orders",
        "shipments",
        "disruptions"
    ]

    all_results = {}

    for collection_name in collections:

        try:

            all_results[collection_name] = retrieve(
                collection_name,
                query,
                n_results
            )

        except Exception as e:

            all_results[collection_name] = [
                f"Error: {str(e)}"
            ]

    return all_results