import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
    try {
        // Al usar el fetch que viene en los argumentos de la función load, 
        // SvelteKit serializa la respuesta para evitar fetch duplicados en el cliente.
        const response = await fetch('http://localhost:8000/api/data');
        if (!response.ok) throw new Error('Error al obtener datos');
        
        const backendData = await response.json();
        return { backendData };
    } catch (error) {
        console.error('Error fetching data from backend:', error);
        return {
            backendData: { message: 'Servidor no disponible' }
        };
    }
};
