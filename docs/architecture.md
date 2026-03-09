# Arquitectura del Sistema: Nexus OES (V2)

Esta arquitectura se basa en la **Separación Radical de Responsabilidades** y el principio de **Unidad de Verdad Inmutable** en el Backend.

## 1. El Cerebro (Backend Abstracto - FastAPI)
El backend está diseñado como un motor industrial genérico. No "sabe" qué material se está procesando, solo gestiona flujos de masa y valor.

*   **Entidades de Flujo Universal:**
    *   **Batch (Lote/Carga):** Unidad lógica que agrupa masa y valor. Posee un estado (`RAW`, `WIP`, `FINISHED`) y una ubicación.
    *   **ContainerSnapshot (Hito de Pesaje):** Registro inmutable de una unidad física (Jumbo, Pallet, Caja). Captura el valor **literal** de tara, peso bruto y precio unitario en el momento exacto del evento.
    *   **EventLog:** Registro histórico de transformaciones (División, Mezclado, Compactación).
*   **Inmutabilidad Operativa:** Una vez que un Batch se cierra, sus valores económicos y de pesaje se "congelan". Cualquier cambio en los maestros globales (precios de mercado, taras estándar) **no afecta** a los registros pasados.
*   **Gestión de Activos:** Seguimiento de envases ocupados en bodega para indicadores de disponibilidad de herramientas de transporte.

## 2. El Reflejo (Frontend Especializado - SvelteKit)
El frontend es la capa de **Especialización de Negocio**. Es aquí donde el sistema se adapta a la industria específica (Reciclaje, Minería, Manufactura).

*   **Lenguaje de Dominio:** Traduce los términos abstractos del backend a términos operativos ("Jumbos", "Conductores", "Liquidación de Cobre").
*   **Lógica de Consolidación:** Agrupa el pesaje físico (múltiples Jumbos) con la negociación económica (un precio por tipo de material) para optimizar el flujo del supervisor.
*   **Gestión de Responsabilidad:** Diferenciación entre Logística Interna (Empresa) y Entrega de Proveedor (Responsabilidad Global del Beneficiario).

## 3. Modelo de Datos Inmutable
Para garantizar la auditoría, el sistema utiliza **Snapshots**. En lugar de referenciar una tabla de "Precios de Hoy", el registro de cada compra guarda el precio pactado como un valor estático. Esto permite reconstruir la historia financiera exacta de cualquier fecha pasada.

## 4. Independencia de Infraestructura
Los modelos de dominio son clases puras de Python. Esto permite que el sistema pueda migrar de una base de datos a otra (SQL, NoSQL, In-memory) sin alterar la lógica de cálculo de eficiencia o liquidación.
