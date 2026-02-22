# sv - Frontend SvelteKit

Todo lo que necesitas para construir un proyecto Svelte, impulsado por [`sv`](https://github.com/sveltejs/cli).

## Creación de un proyecto

Si estás leyendo esto, probablemente ya hayas completado este paso. ¡Felicidades!

```sh
# crear un nuevo proyecto
npx sv create mi-app
```

Para recrear este proyecto con la misma configuración:

```sh
# recrear este proyecto
bun x sv create --template minimal --types ts --add prettier eslint tailwindcss="plugins:forms" sveltekit-adapter="adapter:node" --install bun .
```

## Desarrollo

Una vez que hayas creado un proyecto y hayas instalado las dependencias con `npm install` (o `pnpm install` o `yarn` o `bun install`), inicia un servidor de desarrollo:

```sh
npm run dev

# o inicia el servidor y abre la aplicación en una nueva pestaña del navegador
npm run dev -- --open
```

## Construcción

Para crear una versión de producción de tu aplicación:

```sh
npm run build
```

Puedes previsualizar la versión de producción con `npm run preview`.

> Para desplegar tu aplicación, puede que necesites instalar un [adaptador](https://svelte.dev/docs/kit/adapters) para tu entorno de destino.
