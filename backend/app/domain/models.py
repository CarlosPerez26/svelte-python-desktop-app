from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List, Dict, Any
from enum import Enum

class BatchStatus(str, Enum):
    RAW = "RAW"              # Materia Prima suelta
    WIP = "WIP"              # Producto semi-elaborado/limpieza
    FINISHED = "FINISHED"    # Producto terminado (Paca/Unidad)
    WASTE = "WASTE"          # Merma/Basura

class ResourceType(str, Enum):
    HUMAN_DIRECT = "HUMAN_DIRECT"      # Operario en línea
    HUMAN_INDIRECT = "HUMAN_INDIRECT"  # Montacarguista/Supervisor
    MACHINE = "MACHINE"                # Compactadora/Báscula

@dataclass
class Location:
    id: str
    name: str
    type: str # ["ALMACEN_MP", "AREA_PROCESO", "ALMACEN_PT"]

@dataclass
class Resource:
    id: str
    name: str
    type: ResourceType

@dataclass
class Batch:
    id: str                   # Identificador (QR/Spray/ID Camión)
    material_type: str        # Aluminio, Cobre, Cartón, etc.
    status: BatchStatus
    current_location_id: str
    weight: float             # Peso actual (Variable según el hito)
    parent_id: Optional[str] = None # Para trazabilidad (de qué camión o lote viene)
    metadata: Dict[str, Any] = field(default_factory=dict) # Atributos dinámicos (calidad, color)

@dataclass
class OperationEvent:
    id: str
    batch_id: str
    operation_type: str       # ["RECEPCION", "CLASIFICACION", "COMPACTACION", "PESAJE"]
    operator_id: str
    machine_id: Optional[str] = None
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    weight_in: Optional[float] = None
    weight_out: Optional[float] = None
    consumables: Dict[str, Any] = field(default_factory=dict) # {"alambre_m": 5, "spray": "rojo"}
    
    @property
    def duration_minutes(self) -> Optional[float]:
        if self.end_time and self.start_time:
            return (self.end_time - self.start_time).total_seconds() / 60
        return None
