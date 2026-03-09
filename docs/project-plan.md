# Plan de Proyecto: Nexus OES (Operational Execution System)

## 1. Visión y Filosofía
Nexus OES es un sistema de gestión orientado a **procesos operativos e industriales** con trazabilidad total de materiales y eventos físicos.
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
*   **Modelo RACI:** Asignación de responsabilidades por paso de proceso: **R**esponsible (Ejecuta), **A**ccountable (Aprueba), **C**onsulted, **I**nformed.

### Anillo 4: Acceso Programático (API Keys)
*   **Tokens Bearer:** Generación de llaves para integraciones externas (IoT, Balanzas, Scanners). Cada acción vía API Key queda vinculada al usuario responsable.

## 3. Arquitectura de Procesos y Trazabilidad

### A. Modelado de Procesos (Plantillas)
*   Los procesos se definen como **Plantillas Versionadas**. Una modificación en la plantilla no afecta a las instancias que ya están en curso (Preservación del historial).

### B. Ejecución e Inmutabilidad
*   **Documento Objeto:** Cada ejecución genera un registro único. Una vez completado, los datos son inmodificables.
*   **Snapshots Inmutables:** Los valores de pesaje, taras y precios se guardan como "fotos" literales del momento del evento, protegiendo el histórico contra cambios futuros en maestros globales.

### C. Gestión de Desviaciones
*   Bloqueo de acciones fuera de secuencia. Requiere un flujo de autorización especial por un perfil con permiso de "Desviación" (Accountable).

## 4. Ecosistema de Operación Local (Offline-First)

### A. Despliegue Intranet (PWA Local)
*   Instalación desde la IP del servidor local. Consumo cero de datos externos. Interfaz industrial de alta visibilidad.

### B. Identificación Ágil (QR + PIN)
*   Escaneo de lote + PIN de 4 dígitos para una atribución rápida ("Quién hizo Qué").

### C. Notificaciones Híbridas
*   El servidor utiliza su propia salida a internet para enviar alertas críticas (Telegram/WhatsApp/Email) al detectar hitos como "Lote Terminado".

## 5. Fase 1: Panel de Control de Supervisor (V1 - Tracer Bullet)
Implementación inicial para demostrar valor inmediato:
*   **Recepción e Identidad Fiscal:** Registro de entradas vinculando la responsabilidad legal al Beneficiario Global.
*   **Consolidación de Liquidación:** Pesaje por unidades físicas (Jumbos, Pallets) con precios negociados por material.
*   **Control de Activos:** Monitoreo de envases ocupados en bodega para asegurar disponibilidad operativa.

## 6. Inteligencia y Rentabilidad (BI)
*   **Costos Reales (MOD):** Vinculación de tiempos (QR+PIN) con tablas de costos/hora.
*   **Módulo de Ventas:** Registro de demanda externa y priorización de lotes.
*   **Motor Predictivo (Forecast):** Uso de series de tiempo (Python) para proyectar fin de lote y picos de demanda.

## 7. Stack Tecnológico
*   **Backend:** Python 3.12+, FastAPI, SQLAlchemy 2.0 (Async), Pydantic v2.
*   **Ciencia de Datos:** Pandas, NumPy y Scikit-learn.
*   **Frontend:** SvelteKit (Svelte 5) + Vite PWA Plugin + Chart.js.
*   **Comunicación:** REST API + WebSockets para tiempo real.

## 8. Roadmap
1.  **Módulo de Recepción e Inmutabilidad (Completado):** Consolidación de ingresos y activos.
2.  **Módulo de Transformación (Compactación):** Producción de Pacas (PT) y liberación de envases.
3.  **Core Operativo (QR+PIN):** Despliegue de la máquina de estados en planta.
4.  **Inteligencia Financiera:** Cálculo de MOD y márgenes.
5.  **Optimización PWA:** Despliegue final en Intranet local.
