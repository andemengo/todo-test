# Todo App con Flask e Jinja2

## 📁 Struttura del Progetto

```
Todo_day2/
├── app/
│   ├── __init__.py          # Inizializzazione Flask app
│   ├── config.py            # Configurazione centralizzata
│   ├── web.py               # Routes per le pagine web
│   ├── api.py               # API endpoints (login, message, etc.)
│   ├── templates/           # Template Jinja2
│   │   ├── base.html        # Layout base (DRY principle)
│   │   ├── home.html        # Homepage con login
│   │   └── components/      # Componenti riutilizzabili
│   │       ├── alerts.html  # Alert (error, success, info)
│   │       ├── button.html  # Bottoni (primary, secondary, submit)
│   │       └── card.html    # Card container
│   └── static/
│       ├── css/
│       └── javascript/
│           └── script.js    # Logica client-side
├── run.py                   # Entry point dell'applicazione
├── requirements.txt         # Dipendenze Python
└── README.md               # Documentazione

```

## 🎨 Architettura Jinja2

### 1. **Template Base (`base.html`)**
Layout principale che definisce la struttura HTML comune:
- `{% block title %}` - Titolo della pagina
- `{% block content %}` - Contenuto principale
- `{% block extra_head %}` - CSS/meta tags aggiuntivi
- `{% block extra_scripts %}` - JavaScript aggiuntivi

### 2. **Template Figlio (`home.html`)**
Estende `base.html` usando:
```jinja
{% extends "base.html" %}
```

### 3. **Componenti Riutilizzabili**
Macro Jinja2 in `components/`:

#### **Alerts** (`alerts.html`)
```jinja
{{ error_alert('errorMessage') }}
{{ success_alert('Login effettuato!', 'loggedUser') }}
{% call info_alert('Benvenuto!') %}
    <span>Effettua il login</span>
{% endcall %}
```

#### **Buttons** (`button.html`)
```jinja
{{ primary_button('myBtn', 'Accedi', icon_path) }}
{{ secondary_button('cancelBtn', 'Annulla') }}
{{ submit_button('submitBtn', 'Login', icon_path) }}
```

#### **Card** (`card.html`)
```jinja
{% call render_card('Titolo', 'Sottotitolo') %}
    <!-- Contenuto del card -->
{% endcall %}
```

## 🔧 Come Funziona

### **Backend → Frontend (Flask → Jinja2)**

**1. Route in `web.py`:**
```python
@web_bp.get('/')
def home():
    context = {
        'app_name': 'Todo List',
        'welcome_message': 'Benvenuto!',
        'form_labels': {'email': 'Email'}
    }
    return render_template('home.html', **context)
```

**2. Template usa le variabili:**
```jinja
<h1>{{ app_name }}</h1>
<p>{{ welcome_message }}</p>
<label>{{ form_labels.email }}</label>
```

### **Vantaggi di questa Architettura**

✅ **DRY (Don't Repeat Yourself)**: Componenti riutilizzabili
✅ **Manutenibilità**: Modifica un componente → aggiorna ovunque
✅ **Separazione**: Backend (Python) → Frontend (Jinja2)
✅ **Flessibilità**: Facile aggiungere nuove pagine
✅ **Leggibilità**: Codice pulito e organizzato

## 🚀 Comandi Utili

### Avvio del server
```bash
python3 run.py
```

### Installare dipendenze
```bash
pip install -r requirements.txt
```

## 📝 API Endpoints

### `/api/login` (POST)
**Request:**
```json
{
  "username": "nexent@nexent.io",
  "password": "pawelpuzza"
}
```

**Response (Success):**
```json
{
  "success": true,
  "message": "Login effettuato con successo!",
  "user": "nexent@nexent.io"
}
```

**Response (Error):**
```json
{
  "success": false,
  "message": "Credenziali non valide. Riprova."
}
```

## 🎯 Best Practices Jinja2 Implementate

1. **Template Inheritance**: `{% extends %}` per riutilizzare layout
2. **Macro**: Componenti riutilizzabili con parametri
3. **Call Blocks**: `{% call %}` per passare contenuto ai macro
4. **Context Variables**: Passaggio dati da Flask a template
5. **Configurazione Jinja2**: `trim_blocks` e `lstrip_blocks` per HTML pulito
6. **Separazione**: Logica business (Python) vs presentazione (Jinja2)

## 🔐 Credenziali di Test

- **Username**: `nexent@nexent.io`
- **Password**: `pawelpuzza`

---

Made with ❤️ by Nexent
