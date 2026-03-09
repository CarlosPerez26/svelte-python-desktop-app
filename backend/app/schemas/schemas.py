from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any, List
from enum import Enum
from ..domain.models import BatchStatus

class DeliveryType(str, Enum):
    EXTERNAL_PROVIDER = "EXTERNAL_PROVIDER" # Responsabilidad total del Beneficiario
    INTERNAL_LOGISTICS = "INTERNAL_LOGISTICS" # Gestión y responsabilidad de la Empresa

class ContainerSnapshot(BaseModel):
    container_type: str
    material_type: str
    gross_weight: float
    tare_weight: float
    unit_price: float

class BatchCreate(BaseModel):
    id: str                   # Identificador de la Entrega (Nro Guía o Ticket)
    delivery_type: DeliveryType = DeliveryType.EXTERNAL_PROVIDER
    
    # Identidad Global Responsable (Beneficiario)
    provider_name: str        
    provider_id: str          
    
    # Datos de Referencia (Opcionales si es externo)
    conductor: Optional[str] = None
    vehicle_plate: Optional[str] = None
    
    reception_date: datetime = Field(default_factory=datetime.now)
    items: List[ContainerSnapshot] = []
    status: BatchStatus = BatchStatus.RAW
    metadata: Dict[str, Any] = {}

class BatchResponse(BaseModel):
    id: str
    delivery_type: DeliveryType
    provider_name: str
    provider_id: str
    total_weight: float
    total_value: float
    reception_date: datetime
    created_at: datetime
