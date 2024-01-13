const API_URL = import.meta.env.VITE_API_URL;

// Function to make a GET request
export async function apiGet(fetch: any, route: string, cookies?: string) {
    const url = `${API_URL}${route}`;
    const headers: HeadersInit = {};

    // Check if running on the server
    if (typeof window === 'undefined' && cookies) {
        // Server-side: Include cookies manually
        headers['Cookie'] = cookies;
    }

    const response = await fetch(url, {
        method: 'GET',
        headers: headers,
        // Client-side: Include credentials for browser to handle cookies
        credentials: typeof window !== 'undefined' ? 'include' : undefined
    });
    return response;
}

// Function to make a POST request
export async function apiPost(fetch: any, route: string, body: any, cookies: string | null) {
    const url = `${API_URL}${route}`;
    const headers: HeadersInit = {
        'Content-Type': 'application/json'
    };

    // Check if running on the server
    if (typeof window === 'undefined' && cookies) {
        // Server-side: Include cookies manually
        headers['Cookie'] = cookies;
    }

    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(body),
        // Client-side: Include credentials for browser to handle cookies
        credentials: typeof window !== 'undefined' ? 'include' : undefined
    });
    return response;
}

// ... other functions
