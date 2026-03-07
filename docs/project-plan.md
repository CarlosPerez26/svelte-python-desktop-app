# Plan de Proyecto: Nexus OES (Operational Execution System)

## 1. Visión y Filosofía
Sistema de gestión orientado a **procesos operativos e industriales** con trazabilidad total de materiales y eventos físicos.
*   **Filosofía:** "Backend como Cerebro, Frontend como Reflejo". El backend es el único guardián de la lógica, validaciones y estados. El frontend es un capturador de evidencias y disparador de acciones.
*   **Objeto de Negocio:** Todo evento físico (recepción, transformación, despacho) se trata como un objeto digital inmutable y auditable.

## 2. Modelo de Seguridad por Anillos

### Anillo 1: Acceso y Perímetro
*   **Autenticación:** Login con credenciales cifradas.
*   **Registro Controlado:** Usuarios creados en estado `INACTIVO`. Requieren activación manual por el usuario `ROOT`.
*   **Sesiones:** JWT para la interfaz web + Cookies seguras.

### Anillo 2: Identidad Inmutable
*   **Usuario ROOT:** Superusuario inmutable, no eliminable, creado por script de bootstrap. Único capaz de gestionar la estructura de seguridad inicial.

### Anillo 3: Autorización Híbrida (RBAC + Contextual)
*   **RBAC Tradicional:** Usuario -> Roles (Gerente, Operador, Auditor) -> Permisos.
*   **Control Contextual:** La autorización depende del **Estado del Proceso**. (Ej: Un operador solo puede "Firmar" si el proceso está en estado `PENDIENTE_FIRMA`).
*   **Modelo RACI:** Asignación de responsabilidades por paso de proceso:
    *   **R**esponsible (Ejecuta).
    *   **A**ccountable (Aprueba - Solo uno).
    *   **C**onsulted (Información previa).
    *   **I**nformed (Notificación post-evento).

### Anillo 4: Acceso Programático (API Keys)
*   **Tokens Bearer:** Generación de llaves personales para integraciones externas (IoT, Balanzas, Scanners).
*   **Herencia de Permisos:** Los tokens tienen el mismo nivel de acceso que el usuario creador.
*   **Auditoría:** Cada acción vía API Key queda vinculada al usuario responsable.

## 3. Arquitectura de Procesos y Trazabilidad

### A. Modelado de Procesos (Plantillas)
*   Los procesos se definen como **Plantillas Versionadas**.
*   Una modificación en la plantilla no afecta a las instancias que ya están en curso (Preservación del historial).

### B. Ejecución (Instancias Operativas)
*   Cada ejecución de una plantilla genera un **Documento Objeto** único.
*   **Inmutabilidad:** Una vez que un paso se marca como completado, los datos asociados no pueden modificarse.
*   **Evidencia Digital:** Capacidad de adjuntar respaldos (fotos, hashes de archivos, firmas digitales) a cada evento físico.

### C. Trazabilidad de Materiales
*   Seguimiento desde Proveedor -> Materia Prima -> Proceso de Transformación -> Producto Terminado -> Cliente.
*   Gestión de Lotes y Números de Serie.

### D. Gestión de Desviaciones
*   Si un usuario intenta ejecutar una acción fuera de la secuencia definida en la Plantilla, el sistema bloquea la acción.
*   Se activa un **Flujo de Autorización Especial** donde un perfil con permiso de "Desviación" (Accountable) debe validar el salto de paso.

## 4. Stack Tecnológico
*   **Backend:** Python 3.12+, FastAPI, SQLAlchemy 2.0 (Async), Pydantic v2.
*   **Base de Datos:** PostgreSQL (Integridad referencial estricta).
*   **Frontend:** SvelteKit (Svelte 5), TailwindCSS (Diseño limpio, industrial, de alta eficiencia).
*   **Comunicación:** REST API + WebSockets para actualizaciones de estado en tiempo real.

## 5. Fases de Desarrollo (Roadmap)
1.  **Cimientos (Seguridad):** Auth, Anillos 1 y 2, Usuario ROOT.
2.  **Motor de Procesos (Core):** Definición de Plantillas y Máquina de Estados.
3.  **Trazabilidad:** Gestión de materiales y objetos físicos.
4.  **Dashboard de Control:** Visualización de instancias activas y KPIs operativos.
