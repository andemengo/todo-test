// Inizializzazione
document.addEventListener('DOMContentLoaded', function() {
    console.log('Todo App inizializzata');
    
    // Elementi DOM
    const showLoginBtn = document.getElementById('showLoginBtn');
    const loginForm = document.getElementById('loginForm');
    const loginFormElement = document.getElementById('loginFormElement');
    const welcomeSection = document.getElementById('welcomeSection');
    const loggedInSection = document.getElementById('loggedInSection');
    const cancelBtn = document.getElementById('cancelBtn');
    const errorMessage = document.getElementById('errorMessage');
    const errorText = document.getElementById('errorText');
    const loggedUser = document.getElementById('loggedUser');
    const logoutBtn = document.getElementById('logoutBtn');

    // Mostra form di login
    showLoginBtn.addEventListener('click', function() {
        welcomeSection.classList.add('hidden');
        loginForm.classList.remove('hidden');
        errorMessage.classList.add('hidden');
    });

    // Annulla e torna indietro
    cancelBtn.addEventListener('click', function() {
        loginForm.classList.add('hidden');
        welcomeSection.classList.remove('hidden');
        loginFormElement.reset();
        errorMessage.classList.add('hidden');
    });

    // Submit del form di login
    loginFormElement.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Disabilita il bottone durante la richiesta
        const submitBtn = document.getElementById('submitLoginBtn');
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg> Caricamento...';

        try {
            // Chiamata API
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();

            if (data.success) {
                // Login riuscito
                errorMessage.classList.add('hidden');
                loginForm.classList.add('hidden');
                loggedInSection.classList.remove('hidden');
                loggedUser.textContent = data.user.nome_completo;
                loginFormElement.reset();
            } else {
                // Login fallito
                errorText.textContent = data.message;
                errorMessage.classList.remove('hidden');
            }
        } catch (error) {
            // Errore di rete
            errorText.textContent = 'Errore di connessione. Riprova.';
            errorMessage.classList.remove('hidden');
            console.error('Errore:', error);
        } finally {
            // Riabilita il bottone
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Login';
        }
    });

    // Logout
    logoutBtn.addEventListener('click', function() {
        loggedInSection.classList.add('hidden');
        welcomeSection.classList.remove('hidden');
        loginFormElement.reset();
        errorMessage.classList.add('hidden');
    });
});
