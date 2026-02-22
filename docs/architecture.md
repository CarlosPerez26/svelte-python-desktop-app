# Arquitectura del Sistema

Esta aplicación sigue una arquitectura de separación clara de responsabilidades (Separation of Concerns).

## Componentes Core

### 1. Backend (El Cerebro)
*   **Tecnología:** Python (FastAPI).
*   **Responsabilidades:** Lógica de negocio, procesamiento de datos, persistencia y seguridad.
*   **Comunicación:** API RESTful con soporte para CORS.

### 2. Frontend (La Interfaz)
*   **Tecnología:** SvelteKit (Svelte 5 + TailwindCSS).
*   **Responsabilidades:** Interfaz de usuario, renderizado en el servidor (SSR) para velocidad y SEO, y gestión de estado reactiva.

### 3. Capa de Escritorio (Futuro)
*   **Tecnología:** Tauri (Rust).
*   **Objetivo:** Empaquetar el frontend y el backend en un ejecutable ligero y nativo.

## Flujo de Datos
1.  El usuario interactúa con el frontend (SvelteKit).
2.  SvelteKit realiza peticiones (vía SSR o cliente) al backend (FastAPI).
3.  FastAPI procesa la solicitud y devuelve JSON.
4.  El frontend actualiza la interfaz de forma reactiva.
