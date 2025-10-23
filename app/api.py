from flask import Blueprint, jsonify, redirect, request, current_app, session, url_for
from datetime import datetime
from .decorators import api_login_required

api_bp = Blueprint('api', __name__)

USERS = {
    'andrea': {
        'userId': 1,
        'password': 'andrea123',
        'nome_completo': 'Andrea Rossi',
        'email': 'andrea@example.com'
    },
    'mario': {
        'userId': 2,
        'password': 'mario456',
        'nome_completo': 'Mario Bianchi',
        'email': 'mario@example.com'
    },
    'giulia': {
        'userId': 3,
        'password': 'giulia789',
        'nome_completo': 'Giulia Verdi',
        'email': 'giulia@example.com'
    },
    'lucas': {
        'userId': 4,
        'password': 'lucas321',
        'nome_completo': 'Luca Sartori',
        'email': 'lucas@example.com'
    },
    'nexent': {
        'userId': 5,
        'password': 'nexent2024',
        'nome_completo': 'Nexent Team',
        'email': 'nexent@nexent.io'
    },
    'pawelpuzza': {
        'userId': 6,
        'password': 'pawelpass',
        'nome_completo': 'Pawel Puzza',
        'email': 'pawelpuzza@example.com'
    },
    'francesca': {
        'userId': 7,
        'password': 'fra456',
        'nome_completo': 'Francesca Neri',
        'email': 'francesca@example.com'
    },
    'matteo': {
        'userId': 8,
        'password': 'matteo789',
        'nome_completo': 'Matteo Galli',
        'email': 'matteo@example.com'
    },
    'giorgio': {
        'userId': 9,
        'password': 'giorgio321',
        'nome_completo': 'Giorgio Rinaldi',
        'email': 'giorgio@example.com'
    },
    'elena': {
        'userId': 10,
        'password': 'elena654',
        'nome_completo': 'Elena Russo',
        'email': 'elena@example.com'
    }
}

@api_bp.route('/login', methods=['POST'])
def login():
    # Se l'utente è già loggato, reindirizza alla home
    if 'username' in session:
        user_data = USERS.get(session['username'])
        return jsonify({
            "success": True,
            "message": "Sei già loggato!",
            "user": {
                "username": session['username'],
                "userId": session['userId'],
                "nome_completo": session['nome_completo'],
                "email": session['email']
            }
        }), 200
    
    try:
        # Leggi i dati JSON inviati dal frontend
        payload = request.get_json(silent=True) or {}
        email = payload.get('email', '').strip().lower()
        password = payload.get('password', '').strip()
        
        # Cerca l'utente tramite email
        username_found = None
        for username, user_data in USERS.items():
            if user_data['email'].lower() == email:
                username_found = username
                break
        
        # Verifica se l'utente esiste e la password è corretta
        if username_found and USERS[username_found]['password'] == password:
            user_data = USERS[username_found]
            session['username'] = username_found
            session['nome_completo'] = user_data['nome_completo']
            session['email'] = user_data['email']
            session['userId'] = user_data['userId']
                
            return jsonify({
                "success": True,
                "message": "Login effettuato con successo!",
                "user": {
                    "username": username_found,
                    "userId": user_data['userId'],
                    "nome_completo": user_data['nome_completo'],
                    "email": user_data['email']
                }
            }), 200

        # Credenziali non valide
        return jsonify({
            "success": False,
            "message": "Credenziali non valide. Riprova."
        }), 401

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@api_bp.route('/logout', methods=['POST'])
def logout():
    username = session.get('username')
    
    # Pulisce la sessione
    session.clear()
    
    return jsonify({
        "success": True,
        "message": f"Logout effettuato con successo per l'utente {username}."
    }), 200


@api_bp.route('/me', methods=['GET'])
@api_login_required
def get_current_user():
    """
    API protetta - ritorna i dati dell'utente loggato
    Richiede autenticazione
    """
    return jsonify({
        "success": True,
        "user": {
            "username": session.get('username'),
            "userId": session.get('userId'),
            "nome_completo": session.get('nome_completo'),
            "email": session.get('email')
        }
    }), 200

