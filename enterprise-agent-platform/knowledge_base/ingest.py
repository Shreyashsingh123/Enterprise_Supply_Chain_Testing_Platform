import os
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "synthetic_data"
PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", str(BASE_DIR / "vector_store"))
Path(PERSIST_DIR).mkdir(parents=True, exist_ok=True)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path=PERSIST_DIR)

def ingest_csv(
    csv_path: str,
    collection_name: str,
    prefix: str,
    text_builder
):

    print(f"\nLoading {collection_name}...")

    collection = client.get_or_create_collection(
        name=collection_name
    )

    df = pd.read_csv(csv_path)

    documents = []
    ids = []

    for idx, row in df.iterrows():

        text = text_builder(row)

        documents.append(text)

        ids.append(
            f"{prefix}_{idx}"
        )

    print(
        f"Creating embeddings for {len(documents)} records..."
    )

    embeddings = []

    batch_size = 500

    for i in range(
        0,
        len(documents),
        batch_size
    ):

        batch = documents[i:i + batch_size]

        batch_embeddings = model.encode(
            batch,
            show_progress_bar=False
        ).tolist()

        embeddings.extend(
            batch_embeddings
        )

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    print(
        f"Stored {len(documents)} records in {collection_name}"
    )


ingest_csv(
    csv_path=DATA_DIR / "suppliers.csv",
    collection_name="suppliers",
    prefix="supplier",
    text_builder=lambda row: f"""
    Supplier ID: {row['supplier_id']}
    Name: {row['name']}
    Country: {row['country']}
    Risk Score: {row['risk_score']}
    """
)

ingest_csv(
    csv_path=DATA_DIR / "inventory.csv",
    collection_name="inventory",
    prefix="inventory",
    text_builder=lambda row: f"""
    SKU: {row['sku']}
    Product: {row['product']}
    Current Stock: {row['current_stock']}
    Reorder Point: {row['reorder_point']}
    """
)

ingest_csv(
    csv_path=DATA_DIR / "orders.csv",
    collection_name="orders",
    prefix="order",
    text_builder=lambda row: f"""
    Order ID: {row['order_id']}
    Customer: {row['customer']}
    Quantity: {row['quantity']}
    Status: {row['status']}
    """
)

ingest_csv(
    csv_path=DATA_DIR / "shipments.csv",
    collection_name="shipments",
    prefix="shipment",
    text_builder=lambda row: f"""
    Shipment ID: {row['shipment_id']}
    Origin: {row['origin']}
    Destination: {row['destination']}
    Delay Days: {row['delay_days']}
    """
)


ingest_csv(
    csv_path=DATA_DIR / "disruptions.csv",
    collection_name="disruptions",
    prefix="disruption",
    text_builder=lambda row: f"""
    Event ID: {row['event_id']}
    Event Type: {row['event_type']}
    Severity: {row['severity']}
    Impact Score: {row['impact_score']}
    """
)

print("\n✅ All datasets ingested successfully")