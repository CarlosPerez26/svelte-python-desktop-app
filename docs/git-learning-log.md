# Bitácora de Aprendizaje y Configuración Git

Este documento registra el proceso de aprendizaje, los desafíos superados y la configuración paso a paso del proyecto.

## Proceso de Configuración (Sesión Interactiva)

### 1. Creación del Repositorio en GitHub
*   **Acción del Usuario:** Creó un nuevo repositorio vacío en GitHub.com.
*   **URL:** `https://github.com/CarlosPerez26/svelte-python-desktop-app.git`

### 2. Configuración de la Identidad Git
```bash
git config --global user.email "carlos.perez0826@proton.me"
git config --global user.name "carlos.perez0826"
```

### 3. Creación de la Estructura Inicial
Se crearon las carpetas `/frontend` y `/backend` con archivos base (`.gitignore`, `README.md`, `main.py`).

### 4. Inicialización Git Local y Primer Commit
```bash
git init
git add .
git commit -m "feat: Initial project structure for SvelteKit and Python"
```

### 5. Conexión Remota y Primer Push
```bash
git remote add origin https://github.com/CarlosPerez26/svelte-python-desktop-app.git
git branch -M main
git push -u origin main
```

### 6. Configuración de PAT (Personal Access Token)
Se utilizó un **Fine-grained PAT** con permisos de `Contents: Read and write` para la autenticación segura.

### 7. Configuración del Credential Helper (Linux/Contenedor)
```bash
git config --global credential.helper store
```
*   **Aprendizaje:** Guarda el PAT en `~/.git-credentials`. Útil en entornos de desarrollo temporales.

### 8. Configuración del Frontend SvelteKit
Se inicializó con `bun x sv create .` seleccionando: Skeleton project, TypeScript, ESLint, Prettier y Tailwind CSS.

### 9. Traducción de Documentación
Se tradujeron los READMEs iniciales al español para mantener la consistencia del proyecto.

### 10. Gestión de Dependencias y Tauri
Se instalaron dependencias del frontend y se decidió posponer la integración de Tauri, eliminando el CLI para mantener el proyecto limpio.

### 11. Primera Prueba de Integración Exitosa (Backend + Frontend)
*   **Backend:** Configuración de `CORSMiddleware` para permitir peticiones desde `localhost:5173`.
*   **Frontend:** Implementación de SSR mediante la función `load` en `+page.ts`.
*   **Resultado:** El frontend consume y muestra datos de FastAPI correctamente.

---

## Conceptos Aprendidos:
*   **CORS:** Por qué es necesario cuando el front y el back están en puertos/dominios distintos.
*   **SSR (Server Side Rendering):** Cómo SvelteKit puede pedir datos al backend antes de enviar la página al navegador.
*   **Flujo Git:** La importancia de commits atómicos y descriptivos.
*   **PAT:** Manejo de seguridad en la autenticación con GitHub.
