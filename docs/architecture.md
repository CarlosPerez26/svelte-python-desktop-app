# Arquitectura del Sistema: Nexus OES

Esta arquitectura se basa en la **Separación de Responsabilidades** (Separation of Concerns) y el principio de **Unidad de Verdad** en el Backend.

## 1. El Cerebro (Backend - FastAPI)
El backend es el núcleo de la inteligencia y el guardián de la integridad de los datos.

*   **Motor de Máquina de Estados (FSM):** Gestiona la lógica de las plantillas de proceso y valida cada transición de estado de las instancias.
*   **Gestión de Evidencias:** Capa encargada de recibir hashes y archivos que respaldan la trazabilidad.
*   **Middleware de Seguridad (Anillos):**
    *   **Capa de Autenticación:** Verifica identidad vía JWT o API Keys.
    *   **Capa de Autorización RACI:** Evalúa si el usuario actual tiene el rol (`Responsible` o `Accountable`) para el paso actual del proceso.
*   **Persistencia Inmutable:** Uso de PostgreSQL con una estrategia de "Solo Inserción" para auditoría operativa, donde los registros históricos no se editan.

## 2. El Reflejo (Frontend - SvelteKit)
El frontend no toma decisiones de negocio; simplemente muestra lo que el backend autoriza y captura datos de entrada.

*   **Arquitectura Reactiva:** Svelte 5 para una interfaz fluida que responde a cambios de estado en tiempo real (WebSockets).
*   **Captura de Datos Operativos:** Formularios dinámicos basados en la "Plantilla de Proceso" actual.
*   **Visualización de Trazabilidad:** Componentes de línea de tiempo y grafos para mostrar el origen y destino de los materiales.

## 3. Modelo de Comunicación (Capa de Transporte)
*   **API RESTful:** Para operaciones estándar (CRUD de catálogos, login, configuración).
*   **WebSockets (SSE Opcional):** Para notificaciones en tiempo real sobre cambios de estado en líneas de producción o procesos compartidos.
*   **Event Log:** Registro interno de cada petición para auditoría de trazabilidad técnica.

## 4. Flujo de un "Evento Operativo Física"
1.  **Captura:** El operario escanea un código (Fisico -> Digital).
2.  **Validación:** El frontend envía la intención al backend.
3.  **Evaluación de Seguridad:** El backend verifica:
    *   ¿Token válido?
    *   ¿Usuario activo?
    *   ¿El proceso permite este paso?
    *   ¿El usuario es el `Responsible` asignado?
4.  **Ejecución y Persistencia:** Si todo es correcto, el backend registra el evento como un nuevo "Hito inmutable" y actualiza el estado del objeto.
5.  **Reflejo:** El frontend actualiza la UI confirmando el registro exitoso.

## 5. Estrategia de Versionamiento de Procesos
*   Cada `ProcessTemplate` tiene un `version_id`.
*   Cuando un proceso inicia, se vincula a una versión específica de la plantilla.
*   Si la plantilla cambia, las instancias antiguas siguen ejecutándose bajo la versión original para garantizar la coherencia de los datos históricos.
