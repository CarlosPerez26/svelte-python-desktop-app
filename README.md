# Aplicación de Escritorio SvelteKit + Python

Este repositorio es el proyecto padre para una aplicación de escritorio de alta performance y seguridad, diseñada con una arquitectura híbrida moderna.

## Visión Arquitectónica

El proyecto se basa en la separación clara de responsabilidades, utilizando **FastAPI como el "cerebro" central** de la operación y **SvelteKit como una interfaz dinámica con SSR**.

### Componentes Core:

-   **Backend (El Cerebro):** Implementado en **Python (FastAPI)**.
    -   Gestiona la lógica de negocio, procesamiento de datos y orquestación del sistema.
    -   **Seguridad de Acceso:** Sistema de comunicación basado en API con dos niveles de acceso:
        1.  **Inicio de Sesión (Rutas Protegidas):** Control de acceso basado en estados previos y **roles de usuario** para operaciones administrativas y sensibles.
        2.  **Tokens Bearer (Acceso Rápido):** Generación y revocación dinámica de tokens Bearer para consultas rápidas de datos sin necesidad de sesión activa. Estos tokens pueden ser gestionados por usuarios con permisos específicos.
-   **Frontend (La Interfaz):** Implementado en **SvelteKit (Svelte 5 + TailwindCSS)**.
    -   Utiliza **SSR (Server-Side Rendering)** para optimizar la carga inicial y la consistencia del estado.
    -   Interfaz moderna, reactiva y estilizada con TailwindCSS.
-   **Empaquetado (Escritorio):** Futura integración con **Tauri (Rust)**.
    -   Tauri se encargará de ejecutar un **Python embebido** para correr los scripts del backend localmente junto con el servidor de SSR del frontend, permitiendo una experiencia de aplicación de escritorio nativa y ligera.

## Estructura del Proyecto

-   `/frontend`: Proyecto SvelteKit con soporte para SSR y Tailwind.
-   `/backend`: API de FastAPI, lógica de seguridad y procesamiento Python.
-   `/.agents/skills/`: Habilidades locales del agente que dictan los estándares de diseño, seguridad y arquitectura.

## Habilidades del Agente (Agent Skills)

Este proyecto utiliza un conjunto de habilidades locales del agente para potenciar el desarrollo. Estas habilidades se encuentran en el directorio `/.agents/skills/` y están versionadas como parte del proyecto para asegurar un entorno de desarrollo consistente.

-   `api-design`: Proporciona experiencia en el diseño de APIs robustas y escalables.
-   `architecture-patterns`: Ofrece orientación sobre las mejores prácticas de arquitectura de software.
-   `fastapi-python`: Experto en desarrollo de backend con Python y FastAPI.
-   `openapi-to-typescript`: Ayuda a generar tipos de TypeScript a partir de una especificación OpenAPI, facilitando la integración frontend-backend.
-   `python-backend`: Conocimiento general para el desarrollo de backend en Python.
-   `security-patterns`: Provee patrones para implementar funcionalidades de seguridad como autenticación y autorización.
-   `sveltekit-svelte5-tailwind-skill`: Habilidad especializada en el desarrollo de frontend con SvelteKit, Svelte 5 y TailwindCSS.

---

## Proceso de Configuración y Aprendizaje de Git/GitHub (Sesión Interactiva)

Esta sección documenta los pasos detallados para configurar este proyecto, con un enfoque en el aprendizaje de Git y GitHub.

### 1. Creación del Repositorio en GitHub

**Acción del Usuario:**
*   Creó un nuevo repositorio vacío en GitHub.com (sin README, .gitignore ni licencia).
*   Proporcionó la URL del repositorio: `https://github.com/CarlosPerez26/svelte-python-desktop-app.git`

### 2. Configuración de la Identidad Git

Antes de cualquier commit, se configuró la identidad del autor de los commits.

**Comandos Ejecutados:**
```bash
git config --global user.email "carlos.perez0826@proton.me"
git config --global user.name "carlos.perez0826"
```

### 3. Creación de la Estructura Inicial del Proyecto

Se crearon las carpetas para el frontend (SvelteKit) y el backend (Python), junto con archivos iniciales como `.gitignore` y `README.md` (padre).

**Comandos Ejecutados:**
```bash
mkdir -p svelte-python-desktop-app/frontend svelte-python-desktop-app/backend
# Se crearon los siguientes archivos
# svelte-python-desktop-app/README.md
# svelte-python-desktop-app/.gitignore
# svelte-python-desktop-app/backend/requirements.txt
# svelte-python-desktop-app/backend/main.py
# svelte-python-desktop-app/frontend/README.md
```

### 4. Inicialización Git Local y Primer Commit

Se inicializó Git en el directorio raíz del proyecto y se realizó el primer commit de la estructura básica.

**Comandos Ejecutados:**
```bash
cd svelte-python-desktop-app
git init
git add .
git commit -m "feat: Initial project structure for SvelteKit and Python"
```

### 5. Conexión con el Repositorio Remoto y Primer Push

Se vinculó el repositorio local con el remoto de GitHub y se subieron los cambios iniciales.

**Comandos Ejecutados:**
```bash
cd svelte-python-desktop-app
git remote add origin https://github.com/CarlosPerez26/svelte-python-desktop-app.git
git branch -M main
git push -u origin main
```
*   **Aprendizaje clave:** Se requirió autenticación con un **Token de Acceso Personal (PAT)** de GitHub, no con la contraseña de la cuenta.

### 6. Configuración de PAT de Grano Fino (Fine-grained Personal Access Token)

Ante problemas de autenticación, se guio en la creación de un PAT de grano fino.

**Configuración PAT (manual en GitHub.com):**
*   **Permiso de Repositorio:** `Contents` con acceso de **"Read and write"**.
*   **Importancia:** No compartir el PAT y revocar inmediatamente si se expone.

### 7. Configuración del Credential Helper en Linux (Contenedor)

Para evitar introducir el PAT en cada `git push`, se configuró un helper de credenciales.

**Comando Ejecutado:**
```bash
git config --global credential.helper store
```
*   **Aprendizaje clave:** `credential.helper store` guarda el PAT en texto plano en `~/.git-credentials`. Se asumió este riesgo por conveniencia en un entorno de contenedor temporal.

### 8. Configuración del Frontend SvelteKit

Se inicializó el proyecto SvelteKit en el directorio `/frontend` con las siguientes especificaciones:

**Comandos Ejecutados:**
```bash
cd svelte-python-desktop-app/frontend
bun x sv create .
# Se seleccionaron las siguientes opciones interactivas:
# - Template: Skeleton project
# - TypeScript: Yes
# - ESLint: Yes
# - Prettier: Yes
# - Tailwind CSS: Yes (a través de los prompts)
# - Adapter: @sveltejs/adapter-node
# - Playwright: No
# - Vitest: No
```
*   **Instalación de dependencias SvelteKit:**
```bash
cd svelte-python-desktop-app/frontend
bun install
```

### 9. Traducción de Archivos `README.md`

Se corrigieron los archivos `README.md` (padre y `/frontend`) al español para cumplir con las convenciones del proyecto.

**Comandos Ejecutados (ejemplo para `/frontend/README.md`):**
```bash
# Leer contenido del README en inglés
read_file svelte-python-desktop-app/frontend/README.md
# Se actualizó el archivo con el contenido traducido usando 'write_file'
# ... (similar para el README principal)
```

### 10. Commits y Pushes Sucesivos

Cada paso de configuración importante y cada corrección se commiteó y se subió a GitHub.

**Comandos Ejecutados (ejemplos):**
```bash
cd svelte-python-desktop-app
git add frontend/ # o archivos específicos
git commit -m "feat: Configurar SvelteKit con adapter-node, TailwindCSS, ESLint y Prettier"
git push
git commit -m "docs: Traducir README de frontend a español"
git push
```

### 11. Reversión de la Integración Inicial de Tauri

Se intentó iniciar la integración de Tauri, pero se decidió posponerla.

**Comandos Ejecutados (para revertir la instalación del CLI):**
```bash
cd svelte-python-desktop-app/frontend
bun remove @tauri-apps/cli
```
*   **Aprendizaje clave:** Se verificó que esta remoción no requirió un commit ya que los cambios de la instalación no habían sido commiteados previamente.

### 12. Primera Prueba de Integración Exitosa (Backend + Frontend)

Se realizó la primera conexión real entre el cerebro (FastAPI) y la interfaz (SvelteKit).

**Acciones Realizadas:**
*   **Backend:**
    *   Se configuró `CORSMiddleware` en `backend/main.py` para permitir peticiones desde el origen del frontend (`http://localhost:5173`).
    *   Se verificó el funcionamiento de los endpoints `/` y `/api/data`.
*   **Frontend:**
    *   Se implementó una función `load` universal en `frontend/src/routes/+page.ts` para realizar fetch de datos durante el SSR.
    *   Se actualizó `+page.svelte` con Svelte 5 y TailwindCSS para mostrar dinámicamente la respuesta del backend.
*   **Resultado:** Conexión exitosa y visualización de datos en tiempo real.

---

## Lo que Aprendimos de Git y GitHub hasta ahora:

*   **Flujo Básico:** Inicializar, añadir, commit, conectar remoto, push.
*   **Identificación:** Importancia de `user.name` y `user.email`.
*   **Seguridad:** Uso crítico de PATs sobre contraseñas de cuenta para GitHub CLI/Git, y la necesidad de proteger/revocar PATs.
*   **PAT de Grano Fino:** Cómo configurar permisos específicos (`Contents` - Read and write) para un control más granular.
*   **Automatización de Credenciales:** Uso de `credential.helper store` en Linux para evitar la solicitud repetida de credenciales, con la advertencia de seguridad de texto plano.
*   **Estado del Repositorio:** Cómo verificar `git status` y entender cuándo hay o no hay cambios pendientes de commit/push.

---

## Próximos Pasos en Git/GitHub (a considerar)

*   **Ramificación (Branching):** Crear y trabajar en ramas para nuevas funcionalidades (`git branch`, `git checkout`).
*   **Fusión (Merging):** Integrar cambios de una rama a otra (`git merge`).
*   **Resolución de Conflictos:** Estrategias para manejar cuando dos ramas modifican el mismo código.
*   **GitHub Actions:** Entender workflows, jobs, steps y la configuración de "runners" para CI/CD.

---

Ahora que tenemos esta documentación completa, **¿qué te gustaría hacer a continuación con el proyecto?**
