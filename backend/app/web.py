from flask import Blueprint, render_template, session
from .decorators import login_required

web_bp = Blueprint('web', __name__)

@web_bp.get('/')
def home():
    # Dati da passare al template Jinja2
    context = {
        'page_title': 'Login',
        'app_name': 'Todo List',
        'app_subtitle': 'Organizza le tue attività con stile',
        'welcome_message': 'Benvenuto!',
        'welcome_subtitle': 'Effettua il login per iniziare',
        'company_name': 'Andrea Mengoli',
        'form_labels': {
            'email': 'Email',
            'password': 'Password'
        },
        'form_placeholders': {
            'email': 'user@email.io',
            'password': '••••••••'
        }
    }
    return render_template('home.html', **context)


@web_bp.route('/todolist')
@login_required
def todo_list():
    """
    Pagina lista attività - accessibile solo se loggato
    Mostra le attività dell'utente dalla sessione
    """
    context = {
        'page_title': 'La mia lista attività',
        'username': session.get('username'),
        'nome_completo': session.get('nome_completo'),
        'email': session.get('email'),
        'userId': session.get('userId')
    }
    
    return render_template('todolist.html', **context)
