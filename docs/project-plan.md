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

## 4. Ecosistema de Operación Local e Inclusivo (Offline-First)

Para garantizar la continuidad operativa en entornos industriales sin dependencia de internet, el sistema se despliega bajo un modelo de **Intranet Privada**.

### A. Acceso y Despliegue (PWA Local)
*   **Instalación sin Datos:** El servidor funciona como un nodo central en la red local (WiFi/Intranet). El trabajador accede vía IP (ej. `http://192.168.1.50`) e instala la aplicación como una **PWA (Progressive Web App)** en su pantalla de inicio.
*   **Consumo Cero:** Una vez instalada, la app funciona como una aplicación nativa consumiendo recursos locales, sin requerir salida a internet ni consumo de datos móviles del trabajador.
*   **Interfaz Industrial:** Diseñada para alta visibilidad y uso con guantes o en condiciones de baja iluminación.

### B. Flujo de Identificación y Registro (QR + PIN)
*   **Acción Rápida:** El trabajador escanea un **Código de Barras o QR** del producto o lote.
*   **Identificación por PIN:** Tras el escaneo, el sistema solicita un **PIN de 4 dígitos**. Esto vincula la acción al trabajador responsable de forma ágil sin necesidad de teclados complejos o logins prolongados.
*   **Atribución de Tareas:** El sistema registra automáticamente "Quién hizo Qué" en cada paso del proceso definido en la plantilla.

### C. Inteligencia Operativa y Notificaciones
*   **Cálculo Automático de Productividad:** El backend calcula el tiempo de producción (Lead Time) comparando las marcas de tiempo (`timestamps`) entre los escaneos de inicio y fin de proceso.
*   **Notificaciones Híbridas:** 
    *   **El Trabajador:** Opera 100% localmente.
    *   **El Servidor:** Detecta eventos críticos (ej: "Lote Terminado"). Mediante un script de Python, el servidor utiliza su propia salida a internet para enviar mensajes automáticos (Telegram/WhatsApp/Email) al supervisor solicitando validación de calidad o fin de proceso.

## 5. Capa de Inteligencia y Rentabilidad (Business Intelligence)

Para elevar el sistema de un nivel táctico a uno estratégico, se implementa una capa de análisis de datos orientada a la toma de decisiones financieras y comerciales.

### A. Módulo Financiero y de Costos Reales
*   **Costo de Mano de Obra Directa (MOD):** Vinculación automática de los tiempos registrados por el trabajador (via QR+PIN) con tablas de costos/hora, permitiendo conocer el costo real de labor por cada producto o lote en tiempo real.
*   **Margen de Contribución:** Cruce de datos entre el costo de materiales (trazabilidad) y mano de obra para determinar la rentabilidad real de cada orden de producción.

### B. Gestión de Ventas y Demanda
*   **Integración de Pedidos:** Módulo para registrar la demanda externa (ventas). El sistema contrasta los pedidos pendientes contra la capacidad instalada medida en planta.
*   **Priorización Inteligente:** Algoritmos que sugieren qué lotes producir primero basándose en fechas de entrega, rentabilidad y disponibilidad de materiales.

### C. Motor de Forecast y Proyecciones (Predictivo)
*   **Estimación de Fin de Lote:** Basado en el rendimiento histórico de los trabajadores y el ritmo actual, el sistema proyecta la hora/fecha exacta de finalización de un proceso.
*   **Pronóstico de Demanda:** Uso de series de tiempo (Python Data Science) para predecir picos de demanda estacionales y sugerir niveles de inventario óptimos.

## 6. Stack Tecnológico
*   **Backend:** Python 3.12+, FastAPI, SQLAlchemy 2.0 (Async), Pydantic v2.
*   **Ciencia de Datos:** Pandas, NumPy y Scikit-learn (Para el motor de Forecast y análisis financiero).
*   **Base de Datos:** PostgreSQL (Integridad referencial estricta).
*   **Frontend:** SvelteKit (Svelte 5) + Vite PWA Plugin + Chart.js/LayerChart (Para visualización de KPIs y tendencias).
*   **Notificaciones:** Clientes asíncronos en Python (Httpx) para integración con APIs de mensajería externa.
*   **Comunicación:** REST API + WebSockets para actualizaciones de estado en tiempo real.

## 7. Fases de Desarrollo (Roadmap)
1.  **Cimientos (Seguridad):** Auth, Anillos 1 y 2, Usuario ROOT.
2.  **Motor de Procesos (Core):** Definición de Plantillas y Máquina de Estados (QR + PIN).
3.  **Trazabilidad y Costos:** Gestión de materiales y cálculo de MOD inicial.
4.  **Módulo de Ventas y Demanda:** Registro de pedidos y flujo de priorización.
5.  **Capa de Inteligencia (BI):** Forecast predictivo, dashboards financieros y KPIs de rentabilidad (ROI/OEE).
6.  **Optimización PWA:** Despliegue final en Intranet con soporte offline total.
