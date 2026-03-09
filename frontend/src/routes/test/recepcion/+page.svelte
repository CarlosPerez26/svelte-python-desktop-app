<script lang="ts">
    import { onMount } from 'svelte';

    // --- ESTADO GLOBAL ---
    let deliveryType = $state('EXTERNAL_PROVIDER'); // 'EXTERNAL_PROVIDER' | 'INTERNAL_LOGISTICS'
    let batchId = $state('');
    let conductor = $state('');
    let providerName = $state('');
    let providerId = $state('');
    let receptionDate = $state(new Date().toISOString().slice(0, 10));

    // --- MAESTROS DE REFERENCIA (SUGERENCIAS INMUTABLES) ---
    const TARE_DEFAULTS = { 'JUMBO': 2.5, 'PALLET': 15.0, 'CAJA_PLASTICA': 1.2, 'OTRO': 0.0 };
    const MARKET_PRICES = { 'Cartón': 0.50, 'Aluminio': 1.20, 'Cobre': 5.80, 'Mixto': 0.15 };

    // --- LISTA DE ÍTEMS (SNAPSHOTS) ---
    let items = $state([
        { container_type: 'JUMBO', material_type: 'Cartón', gross_weight: 0, tare_weight: 2.5, unit_price: 0.50 }
    ]);
    
    let loading = $state(false);
    let responseMessage = $state('');

    // --- LÓGICA DE NEGOCIO ---
    let totalNetWeight = $derived(items.reduce((s, i) => s + (i.gross_weight - i.tare_weight), 0));
    let totalValue = $derived(items.reduce((s, i) => s + ((i.gross_weight - i.tare_weight) * i.unit_price), 0));

    function addItem() {
        items.push({ 
            container_type: 'JUMBO', 
            material_type: 'Cartón', 
            gross_weight: 0, 
            tare_weight: 2.5, 
            unit_price: 0.50 
        });
    }

    function removeItem(index: number) {
        if (items.length > 1) items.splice(index, 1);
    }

    function onMaterialOrTypeChange(index: number) {
        const item = items[index];
        item.tare_weight = TARE_DEFAULTS[item.container_type];
        item.unit_price = MARKET_PRICES[item.material_type] || 0;
    }

    async function registerReception() {
        loading = true;
        const payload = {
            id: batchId,
            delivery_type: deliveryType,
            provider_name: providerName,
            provider_id: providerId,
            conductor: deliveryType === 'INTERNAL_LOGISTICS' ? conductor : null,
            reception_date: new Date(receptionDate).toISOString(),
            items: items,
            status: "RAW"
        };

        try {
            const res = await fetch('http://localhost:8000/api/batches', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            if (res.ok) {
                responseMessage = `✅ REGISTRO SELLADO: ${batchId}`;
                // Reset form
                batchId = ''; conductor = ''; providerName = ''; providerId = '';
                items = [{ container_type: 'JUMBO', material_type: 'Cartón', gross_weight: 0, tare_weight: 2.5, unit_price: 0.50 }];
            } else {
                const err = await res.json();
                responseMessage = `❌ ERROR: ${err.detail}`;
            }
        } catch (err) {
            responseMessage = `❌ FALLO DE CONEXIÓN CON EL NODO CENTRAL`;
        } finally {
            loading = false;
        }
    }
</script>

<div class="min-h-screen bg-[#050505] text-gray-200 font-sans p-4 lg:p-8">
    
    <!-- CONTENEDOR PRINCIPAL -->
    <div class="max-w-[1600px] mx-auto grid grid-cols-12 gap-6">
        
        <!-- HEADER (12 Cols) -->
        <header class="col-span-12 flex flex-col lg:flex-row justify-between items-start lg:items-center bg-gray-900/20 border border-gray-800/50 p-8 rounded-[3rem] backdrop-blur-xl mb-4 gap-6">
            <div>
                <div class="flex items-center gap-3 mb-2">
                    <span class="w-3 h-3 rounded-full bg-blue-500 animate-pulse"></span>
                    <h1 class="text-4xl font-black tracking-tighter text-white uppercase">Nexus <span class="text-blue-500">OES</span></h1>
                </div>
                <p class="text-gray-500 font-mono text-[10px] tracking-[0.4em] uppercase">Módulo de Recepción e Inmutabilidad Fiscal</p>
            </div>

            <!-- Switcher de Tipo de Entrega -->
            <div class="flex bg-black p-1.5 rounded-[2rem] border border-gray-800 shadow-inner w-full lg:w-auto">
                <button 
                    onclick={() => deliveryType = 'EXTERNAL_PROVIDER'}
                    class="flex-1 lg:flex-none px-8 py-3 rounded-2xl text-[10px] font-black transition-all {deliveryType === 'EXTERNAL_PROVIDER' ? 'bg-emerald-600 text-white shadow-xl shadow-emerald-900/20' : 'text-gray-600 hover:text-gray-400'}"
                >PROVEEDOR EXTERNO</button>
                <button 
                    onclick={() => deliveryType = 'INTERNAL_LOGISTICS'}
                    class="flex-1 lg:flex-none px-8 py-3 rounded-2xl text-[10px] font-black transition-all {deliveryType === 'INTERNAL_LOGISTICS' ? 'bg-blue-600 text-white shadow-xl shadow-blue-900/20' : 'text-gray-600 hover:text-gray-400'}"
                >LOGÍSTICA INTERNA</button>
            </div>
        </header>

        <!-- PANEL LATERAL: IDENTIDAD (4 Cols) -->
        <aside class="col-span-12 lg:col-span-4 space-y-6">
            
            <!-- Tarjeta de Responsabilidad -->
            <div class="bg-gray-900/30 border border-gray-800 p-8 rounded-[2.5rem] space-y-8 relative overflow-hidden group">
                <div class="absolute top-0 right-0 p-8 opacity-10 group-hover:opacity-20 transition-opacity">
                    <span class="text-8xl font-black">ID</span>
                </div>

                <div class="space-y-6 relative z-10">
                    <h3 class="text-[10px] font-black {deliveryType === 'EXTERNAL_PROVIDER' ? 'text-emerald-500' : 'text-blue-500'} uppercase tracking-[0.4em]">
                        {deliveryType === 'EXTERNAL_PROVIDER' ? 'Responsable Global (Beneficiario)' : 'Gestión Logística Nexus'}
                    </h3>

                    <div class="space-y-5">
                        <div class="group/input">
                            <label class="text-[10px] text-gray-600 font-bold uppercase ml-4 mb-1 block">Nro Ticket / Remisión</label>
                            <input bind:value={batchId} class="w-full bg-black/50 border-gray-800 border-2 rounded-2xl px-6 py-4 outline-none focus:border-blue-600 transition-all font-mono text-xl text-white" placeholder="000-000"/>
                        </div>

                        <div class="group/input">
                            <label class="text-[10px] text-gray-600 font-bold uppercase ml-4 mb-1 block">Nombre Fiscal / Beneficiario</label>
                            <input bind:value={providerName} class="w-full bg-black/50 border-gray-800 border-2 rounded-2xl px-6 py-4 outline-none focus:border-emerald-600 transition-all text-white" placeholder="Persona o Empresa"/>
                        </div>

                        <div class="group/input">
                            <label class="text-[10px] text-gray-600 font-bold uppercase ml-4 mb-1 block">Cédula / RUC / Pasaporte</label>
                            <input bind:value={providerId} class="w-full bg-black/50 border-gray-800 border-2 rounded-2xl px-6 py-4 outline-none focus:border-emerald-600 transition-all font-mono text-white" placeholder="Identidad Legal"/>
                        </div>

                        {#if deliveryType === 'INTERNAL_LOGISTICS'}
                            <div class="space-y-1 animate-in slide-in-from-top-4 duration-500">
                                <label class="text-[10px] text-gray-600 font-bold uppercase ml-4 mb-1 block text-blue-400">Operario / Conductor</label>
                                <input bind:value={conductor} class="w-full bg-black/50 border-blue-900/20 border-2 rounded-2xl px-6 py-4 outline-none focus:border-blue-600 text-white" placeholder="Nombre Conductor"/>
                            </div>
                        {/if}

                        <div class="pt-4 border-t border-gray-800/50">
                            <label class="text-[10px] text-gray-600 font-bold uppercase ml-4 mb-1 block">Fecha de Recepción Oficial</label>
                            <input type="date" bind:value={receptionDate} class="w-full bg-transparent border-none px-4 py-2 text-gray-400 outline-none text-lg"/>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Resumen de Totales (Mobile) -->
            <div class="lg:hidden bg-emerald-600 p-8 rounded-[2.5rem] text-white flex justify-between items-center">
                <div>
                    <p class="text-[10px] font-black uppercase opacity-60">Total Neto</p>
                    <p class="text-3xl font-black font-mono">{totalNetWeight.toFixed(1)} kg</p>
                </div>
                <div class="text-right">
                    <p class="text-[10px] font-black uppercase opacity-60">Liquidación</p>
                    <p class="text-3xl font-black font-mono">${totalValue.toFixed(2)}</p>
                </div>
            </div>
        </aside>

        <!-- PANEL PRINCIPAL: PESAJE (8 Cols) -->
        <main class="col-span-12 lg:col-span-8 flex flex-col gap-6">
            
            <div class="bg-gray-900/20 border border-gray-800 p-8 lg:p-12 rounded-[3.5rem] flex-1 flex flex-col min-h-[800px]">
                
                <!-- Barra de Acciones y Totales -->
                <div class="flex flex-col md:flex-row justify-between items-center mb-12 gap-8 bg-black/40 p-8 rounded-[2.5rem] border border-gray-800/50">
                    <div class="flex gap-12">
                        <div class="space-y-1">
                            <p class="text-[10px] text-gray-600 font-black uppercase tracking-[0.2em]">Peso Neto Acumulado</p>
                            <p class="text-5xl font-mono font-black text-white">{totalNetWeight.toFixed(1)} <span class="text-sm text-gray-700">KG</span></p>
                        </div>
                        <div class="space-y-1 border-l border-gray-800 pl-12">
                            <p class="text-[10px] text-emerald-500 font-black uppercase tracking-[0.2em]">Total Inmutable</p>
                            <p class="text-5xl font-mono font-black text-emerald-400">${totalValue.toFixed(2)}</p>
                        </div>
                    </div>
                    <button 
                        onclick={addItem} 
                        class="w-full md:w-auto bg-white text-black hover:bg-blue-500 hover:text-white px-10 py-5 rounded-3xl font-black text-xs tracking-widest transition-all hover:scale-105 active:scale-95"
                    >+ AÑADIR ÍTEM DE PESAJE</button>
                </div>

                <!-- Lista de Ítems (Snapshots) -->
                <div class="flex-1 space-y-4 overflow-y-auto pr-4 custom-scrollbar">
                    {#each items as item, i}
                        <div class="grid grid-cols-12 gap-4 items-center bg-gray-950/80 p-6 rounded-[2.5rem] border border-gray-900 group hover:border-gray-700 transition-all animate-in zoom-in-95 duration-300">
                            
                            <!-- Material y Envase -->
                            <div class="col-span-12 md:col-span-4 grid grid-cols-2 gap-3">
                                <div class="space-y-1">
                                    <label class="text-[9px] text-gray-700 font-black uppercase ml-2">Material</label>
                                    <select 
                                        bind:value={item.material_type} 
                                        onchange={() => onMaterialOrTypeChange(i)} 
                                        class="w-full bg-black border-gray-900 border rounded-2xl px-4 py-3 text-xs font-bold text-blue-400 outline-none"
                                    >
                                        {#each Object.keys(MARKET_PRICES) as mat} <option value={mat}>{mat}</option> {/each}
                                    </select>
                                </div>
                                <div class="space-y-1">
                                    <label class="text-[9px] text-gray-700 font-black uppercase ml-2">Envase</label>
                                    <select 
                                        bind:value={item.container_type} 
                                        onchange={() => onMaterialOrTypeChange(i)} 
                                        class="w-full bg-black border-gray-900 border rounded-2xl px-4 py-3 text-[9px] font-black text-gray-400 outline-none"
                                    >
                                        {#each Object.keys(TARE_DEFAULTS) as type} <option value={type}>{type}</option> {/each}
                                    </select>
                                </div>
                            </div>

                            <!-- Pesos -->
                            <div class="col-span-12 md:col-span-4 grid grid-cols-2 gap-3">
                                <div class="space-y-1">
                                    <label class="text-[9px] text-gray-700 font-black uppercase text-center block">Bruto (KG)</label>
                                    <input type="number" bind:value={item.gross_weight} class="w-full bg-black border-gray-900 border-2 rounded-2xl py-3 text-xl text-center font-mono font-black text-white focus:border-blue-500 transition-colors outline-none"/>
                                </div>
                                <div class="space-y-1">
                                    <label class="text-[9px] text-gray-800 font-black uppercase text-center block italic">Tara Snapshot</label>
                                    <input type="number" bind:value={item.tare_weight} class="w-full bg-black border-gray-900 border-2 rounded-2xl py-3 text-sm text-center text-gray-600 font-mono outline-none"/>
                                </div>
                            </div>

                            <!-- Precio y Subtotal -->
                            <div class="col-span-12 md:col-span-3 flex items-center gap-4">
                                <div class="flex-1 space-y-1">
                                    <label class="text-[9px] text-emerald-800 font-black uppercase text-center block italic">$/KG Pactado</label>
                                    <input type="number" step="0.01" bind:value={item.unit_price} class="w-full bg-emerald-500/5 border-emerald-900/20 border-2 rounded-2xl py-3 text-xl text-center text-emerald-400 font-mono font-black outline-none"/>
                                </div>
                                <div class="text-right min-w-[80px]">
                                    <p class="text-[8px] text-gray-700 font-black uppercase">Subtotal</p>
                                    <p class="text-sm font-mono font-bold text-white">${((item.gross_weight - item.tare_weight) * item.unit_price).toFixed(2)}</p>
                                </div>
                            </div>

                            <!-- Eliminar -->
                            <div class="col-span-12 md:col-span-1 text-right">
                                {#if items.length > 1}
                                    <button onclick={() => removeItem(i)} class="text-gray-800 hover:text-red-600 p-2 transition-colors">✕</button>
                                {/if}
                            </div>
                        </div>
                    {/each}
                </div>

                <!-- Botón de Sello Inmutable -->
                <button 
                    onclick={registerReception}
                    disabled={loading || !batchId || totalNetWeight <= 0 || !providerId}
                    class="w-full mt-10 py-8 rounded-[3rem] font-black text-2xl bg-gradient-to-r from-blue-700 via-blue-600 to-emerald-600 shadow-3xl shadow-blue-900/20 disabled:opacity-5 transition-all hover:scale-[1.01] active:scale-95 text-white relative overflow-hidden group"
                >
                    <span class="relative z-10">{loading ? 'SELLANDO REGISTRO EN NODO...' : 'LIQUIDAR Y CERRAR RECEPCIÓN INMUTABLE'}</span>
                    <div class="absolute inset-0 bg-white/10 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700"></div>
                </button>
            </div>

            <!-- Feedback de Sistema -->
            {#if responseMessage}
                <div class="p-8 rounded-[2.5rem] border-2 text-center font-black text-xl animate-in slide-in-from-bottom-8 duration-500 {responseMessage.includes('✅') ? 'bg-emerald-500/5 border-emerald-500/20 text-emerald-400' : 'bg-red-500/5 border-red-500/20 text-red-400'}">
                    {responseMessage}
                </div>
            {/if}
        </main>
    </div>
</div>

<style>
    :global(body) { background-color: #050505; margin: 0; cursor: crosshair; }
    .custom-scrollbar::-webkit-scrollbar { width: 4px; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: #111; border-radius: 10px; }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #1a1a1a; }
</style>
