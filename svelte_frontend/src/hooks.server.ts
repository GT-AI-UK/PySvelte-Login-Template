import type { Handle } from '@sveltejs/kit';

const VITE_BASE_URL = import.meta.env.VITE_BASE_URL;
const VITE_API_URL = import.meta.env.VITE_API_URL;

// src/hooks.server.ts
export const handle: Handle = async ({ event, resolve }) => {
    const url = event.url.pathname;
    const cookies = event.request.headers.get('cookie') || '';

    if (url !== '/login' && url !== '/favicon.ico') {
        const response = await fetch(`${VITE_API_URL}/auth/check`, {
            headers: { cookie: cookies }
        });

        if (!response.ok) {
            let loginUrl = `${VITE_BASE_URL}/login`
            loginUrl = ((url === '/') ? loginUrl : `${loginUrl}?redirect=${encodeURIComponent(url)}`)
            return Response.redirect(loginUrl, 302);
        }
    }

    return await resolve(event);
};
