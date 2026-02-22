import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
    try {
        const response = await fetch('http://localhost:8000/api/data');
        const data = await response.json();
        return {
            backendData: data
        };
    } catch (error) {
        console.error('Error fetching data from backend:', error);
        return {
            backendData: { message: 'Error al conectar con el backend' }
        };
    }
};
