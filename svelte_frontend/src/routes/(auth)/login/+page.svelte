<script lang="ts">
    import { goto } from '$app/navigation';
    import { apiPost } from '$lib/api'; // Import apiPost from api.ts
    import { onMount } from 'svelte'

    let redirectUrl: string | null;
    let username = '';
    let password = '';

    onMount(() => {
        const params = new URLSearchParams(window.location.search);
        redirectUrl = params.get('redirect');
    });

    async function login() {
        try {
            const response = await apiPost(fetch, '/auth/login', { username, password }, "");

            if (response.ok) {
                if (redirectUrl) {
                    goto(redirectUrl);
                } else {
                    goto('/'); // Redirect to home if no redirect URL is present
                }
            } else {
                // Handle login errors here
                console.error('Login failed');
            }
        } catch {
            console.error('api error');
        }
    }
</script>


<form on:submit|preventDefault={login}>
    <input type="text" bind:value={username} placeholder="Username">
    <input type="password" bind:value={password} placeholder="Password">
    <button type="submit">Login</button>
</form>
