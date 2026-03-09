from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from datetime import datetime
from app.schemas.schemas import BatchCreate, BatchResponse, DeliveryType
from app.domain.models import BatchStatus

app = FastAPI(title="Nexus OES API - Inmutable V1.2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_batches: Dict[str, Dict] = {}

@app.post("/api/batches", response_model=BatchResponse)
def create_batch(batch_data: BatchCreate):
    """
    Registra el Hito de Recepción basado en el Tipo de Entrega.
    """
    if batch_data.id in db_batches:
        raise HTTPException(status_code=400, detail="El ID del ticket ya existe.")
    
    total_weight = 0
    total_value = 0
    history = []
    
    # Snapshot de los pesajes
    for item in batch_data.items:
        net_w = item.gross_weight - item.tare_weight
        sub_v = net_w * item.unit_price
        total_weight += net_w
        total_value += sub_v
        history.append({ **item.dict(), "net_weight": net_w, "subtotal": sub_v })

    # Consolidamos el Hito
    batch_record = {
        "id": batch_data.id,
        "delivery_type": batch_data.delivery_type,
        "provider_name": batch_data.provider_name,
        "provider_id": batch_data.provider_id,
        "reception_date": batch_data.reception_date or datetime.now(),
        "total_weight": total_weight,
        "total_value": total_value,
        "history": history,
        "created_at": datetime.now()
    }
    
    db_batches[batch_data.id] = batch_record
    return batch_record

@app.get("/api/batches")
def get_batches(): return list(db_batches.values())
