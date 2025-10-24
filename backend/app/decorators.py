"""
Decorators personalizzati per l'applicazione Flask
"""
from functools import wraps
from flask import session, redirect, url_for, flash, jsonify


def login_required(f):
    """
    Decorator per proteggere le route web
    Verifica che l'utente sia loggato prima di accedere alla pagina
    Redirige alla pagina di login se l'utente non è autenticato
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Controlla se 'username' è nella sessione
        if 'username' not in session:
            flash('Devi effettuare il login per accedere a questa pagina', 'warning')
            return redirect(url_for('web.home'))
        return f(*args, **kwargs)
    return decorated_function


def api_login_required(f):
    """
    Decorator per proteggere le API endpoints
    Verifica che l'utente sia loggato prima di accedere all'API
    Ritorna errore JSON 401 se l'utente non è autenticato
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Controlla se 'username' è nella sessione
        if 'username' not in session:
            return jsonify({
                "success": False,
                "message": "Autenticazione richiesta"
            }), 401
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    """
    Decorator per proteggere le route riservate agli admin
    Verifica che l'utente sia loggato E sia un amministratore
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Controlla se l'utente è loggato
        if 'username' not in session:
            flash('Devi effettuare il login per accedere a questa pagina', 'warning')
            return redirect(url_for('web.home'))
        
        # Controlla se l'utente è admin
        if not session.get('is_admin', False):
            flash('Non hai i permessi per accedere a questa pagina', 'danger')
            return redirect(url_for('web.home'))
        
        return f(*args, **kwargs)
    return decorated_function
