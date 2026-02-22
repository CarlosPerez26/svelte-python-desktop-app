<script lang="ts">
    let { data } = $props();
</script>

<div class="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
    <div class="max-w-md w-full bg-gray-800 rounded-xl shadow-2xl p-8 border border-gray-700">
        <h1 class="text-3xl font-bold mb-6 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-emerald-400">
            SvelteKit + FastAPI
        </h1>
        
        <div class="space-y-4">
            <div class="p-4 bg-gray-700/50 rounded-lg border border-gray-600">
                <p class="text-sm text-gray-400 uppercase tracking-wider font-semibold mb-1">Respuesta del Backend:</p>
                <p class="text-lg text-emerald-300 font-mono">
                    {data.backendData.message}
                </p>
            </div>
            
            <p class="text-gray-400 text-sm">
                Esta página está usando <span class="text-blue-400 font-semibold">Svelte 5</span> y 
                obteniendo datos de un servidor <span class="text-emerald-400 font-semibold">FastAPI</span>.
            </p>
        </div>
        
        <div class="mt-8 pt-6 border-t border-gray-700 flex justify-between items-center text-xs text-gray-500">
            <span>Estado: <span class="text-emerald-500">Conectado</span></span>
            <span>SSR Habilitado</span>
        </div>
    </div>
</div>
