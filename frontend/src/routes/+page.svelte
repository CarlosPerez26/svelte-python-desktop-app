<script lang="ts">
    let { data } = $props();
    
    // Mock data for the dashboard skeleton
    const stats = [
        { label: 'Usuarios Activos', value: '1,284', change: '+12.5%', icon: 'users' },
        { label: 'Ingresos Mensuales', value: '$45,231', change: '+8.2%', icon: 'dollar' },
        { label: 'Tareas Completadas', value: '95%', change: '+3.1%', icon: 'check' },
        { label: 'Alertas Sistema', value: '2', change: '-50%', icon: 'alert' }
    ];

    const recentActivity = [
        { user: 'Ana García', action: 'Inició sesión', time: 'Hace 2 min' },
        { user: 'Carlos Pérez', action: 'Actualizó perfil', time: 'Hace 15 min' },
        { user: 'Sistema', action: 'Backup completado', time: 'Hace 1 hora' },
    ];
</script>

<div class="flex h-screen bg-gray-950 text-gray-100 overflow-hidden font-sans p-4">
    <!-- Sidebar -->
    <aside class="w-64 bg-gray-900 border border-gray-800 rounded-2xl flex flex-col hidden md:flex mr-4">
        <div class="p-6">
            <h2 class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-emerald-400">
                Nexus OS
            </h2>
        </div>
        <nav class="flex-1 px-4 space-y-2">
            <a href="/" class="flex items-center space-x-3 p-3 bg-gray-800 rounded-lg text-blue-400">
                <span class="w-5 h-5 opacity-80">🏠</span>
                <span class="font-medium">Dashboard</span>
            </a>
            <a href="/" class="flex items-center space-x-3 p-3 text-gray-400 hover:bg-gray-800 hover:text-white rounded-lg transition-colors">
                <span class="w-5 h-5 opacity-80">📊</span>
                <span>Analíticas</span>
            </a>
            <a href="/" class="flex items-center space-x-3 p-3 text-gray-400 hover:bg-gray-800 hover:text-white rounded-lg transition-colors">
                <span class="w-5 h-5 opacity-80">👤</span>
                <span>Usuarios</span>
            </a>
            <a href="/" class="flex items-center space-x-3 p-3 text-gray-400 hover:bg-gray-800 hover:text-white rounded-lg transition-colors">
                <span class="w-5 h-5 opacity-80">⚙️</span>
                <span>Ajustes</span>
            </a>
        </nav>
        <div class="p-4 border-t border-gray-800">
            <div class="flex items-center space-x-3 p-2">
                <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-blue-600 to-emerald-500 flex items-center justify-center text-white font-bold">
                    CP
                </div>
                <div>
                    <p class="text-sm font-medium">Carlos Pérez</p>
                    <p class="text-xs text-gray-500 text-emerald-500">En línea</p>
                </div>
            </div>
        </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 flex flex-col overflow-auto bg-gray-900 border border-gray-800 rounded-2xl">
        <!-- Header -->
        <header class="h-16 bg-gray-900/50 backdrop-blur-md border-b border-gray-800 flex items-center justify-between px-8 sticky top-0 z-10">
            <div class="flex items-center space-x-4">
                <h1 class="text-xl font-semibold">Resumen General</h1>
            </div>
            <div class="flex items-center space-x-6">
                <div class="relative hidden sm:block">
                    <input type="text" placeholder="Buscar..." class="bg-gray-800 border-none rounded-full px-4 py-1.5 text-sm focus:ring-2 focus:ring-blue-500 w-64">
                </div>
                <div class="flex items-center space-x-4">
                    <button class="text-gray-400 hover:text-white transition-colors relative">
                        🔔
                        <span class="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full"></span>
                    </button>
                    <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-medium transition-colors">
                        Nuevo Proyecto
                    </button>
                </div>
            </div>
        </header>

        <!-- Content Area -->
        <div class="p-8 space-y-8">
            <!-- Backend Status Banner -->
            <div class="bg-emerald-500/10 border border-emerald-500/20 p-4 rounded-xl flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <span class="flex h-3 w-3 relative">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
                    </span>
                    <p class="text-emerald-400 text-sm font-medium">
                        Backend Python Conectado: <span class="text-white italic">"{data.backendData.message}"</span>
                    </p>
                </div>
                <button class="text-xs text-emerald-400 hover:underline">Ver logs</button>
            </div>

            <!-- Stats Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                {#each stats as stat}
                    <div class="bg-gray-900 p-6 rounded-2xl border border-gray-800 hover:border-gray-700 transition-all group">
                        <div class="flex justify-between items-start mb-4">
                            <div class="p-3 bg-gray-800 rounded-xl group-hover:scale-110 transition-transform">
                                <span class="text-xl">{stat.icon === 'users' ? '👥' : stat.icon === 'dollar' ? '💰' : stat.icon === 'check' ? '✅' : '⚠️'}</span>
                            </div>
                            <span class="text-xs font-bold px-2 py-1 rounded-full {stat.change.startsWith('+') ? 'bg-emerald-500/10 text-emerald-500' : 'bg-red-500/10 text-red-500'}">
                                {stat.change}
                            </span>
                        </div>
                        <h3 class="text-gray-400 text-sm mb-1">{stat.label}</h3>
                        <p class="text-2xl font-bold">{stat.value}</p>
                    </div>
                {/each}
            </div>

            <!-- Detailed Section -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <!-- Activity Feed -->
                <div class="lg:col-span-1 bg-gray-900 rounded-2xl border border-gray-800 p-6">
                    <h3 class="font-bold mb-6 flex items-center justify-between">
                        Actividad Reciente
                        <span class="text-xs text-blue-400 cursor-pointer hover:underline">Ver todo</span>
                    </h3>
                    <div class="space-y-6">
                        {#each recentActivity as item}
                            <div class="flex space-x-4 items-start">
                                <div class="w-2 h-2 mt-2 rounded-full bg-blue-500"></div>
                                <div>
                                    <p class="text-sm font-medium">{item.user} <span class="text-gray-500 font-normal">{item.action}</span></p>
                                    <p class="text-xs text-gray-500 mt-1">{item.time}</p>
                                </div>
                            </div>
                        {/each}
                    </div>
                </div>

                <!-- Main Visualization Placeholder -->
                <div class="lg:col-span-2 bg-gray-900 rounded-2xl border border-gray-800 p-6 relative overflow-hidden group">
                    <div class="flex justify-between items-center mb-8">
                        <div>
                            <h3 class="font-bold text-lg">Rendimiento del Sistema</h3>
                            <p class="text-sm text-gray-500 italic">Métricas de procesamiento en tiempo real</p>
                        </div>
                        <select class="bg-gray-800 border-none text-xs rounded-lg px-2 py-1 outline-none">
                            <option>Últimas 24h</option>
                            <option>Últimos 7 días</option>
                        </select>
                    </div>
                    
                    <!-- Placeholder Chart Visual -->
                    <div class="h-48 flex items-end justify-between space-x-2">
                        {#each Array(12) as _, i}
                            <div 
                                class="w-full bg-gradient-to-t from-blue-600 to-emerald-400 rounded-t-md transition-all duration-1000"
                                style="height: {Math.floor(Math.random() * 80) + 20}%; opacity: {0.3 + (i * 0.05)}"
                            ></div>
                        {/each}
                    </div>
                    <div class="mt-4 flex justify-between text-[10px] text-gray-500 uppercase tracking-widest font-bold">
                        <span>Ene</span><span>Feb</span><span>Mar</span><span>Abr</span><span>May</span><span>Jun</span>
                        <span>Jul</span><span>Ago</span><span>Sep</span><span>Oct</span><span>Nov</span><span>Dic</span>
                    </div>
                </div>
            </div>
        </div>
    </main>
</div>

<style>
    /* Transición suave para el cambio de datos del backend */
    :global(body) {
        background-color: #030712;
    }
</style>
