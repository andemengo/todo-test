# Todo App

Applicazione Todo List costruita con Flask (backend) e template Jinja2 + Tailwind CSS (frontend).

## Struttura del Progetto

```
todo-test/
├── backend/              # Backend Flask
│   ├── app/             # Codice applicazione
│   ├── requirements.txt # Dipendenze Python
│   ├── run.py          # Entry point
│   └── README.md       # Documentazione backend
├── frontend/            # Frontend
│   ├── templates/      # Template Jinja2
│   ├── static/         # CSS, JS, immagini
│   └── README.md       # Documentazione frontend
├── .env                # Variabili d'ambiente
├── package.json        # Dipendenze Node.js (Tailwind)
└── README.md          # Questo file
```

## Setup Completo

### 1. Clona il repository

```bash
git clone <repository-url>
cd todo-test
```

### 2. Configura le variabili d'ambiente

Crea il file `.env` dalla copia di esempio:

```bash
cp .env.example .env
```

Poi modifica `.env` e inserisci la tua `SECRET_KEY`:

```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=true
```

### 3. Setup Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Setup Frontend (opzionale - solo se usi Tailwind)

```bash
cd ..  # torna alla root
npm install
```

## Avvio dell'Applicazione

### Backend

```bash
cd backend
source venv/bin/activate
python3 run.py
```

L'app sarà disponibile su: `http://localhost:5000`

### Frontend Development (opzionale)

Se vuoi modificare gli stili Tailwind, in un altro terminale:

```bash
npm run dev  # watch mode per Tailwind
```

## Tecnologie

- **Backend:** Flask 3.1.2, Python
- **Frontend:** Jinja2 templates, Tailwind CSS
- **Autenticazione:** Session-based con decoratori custom
- **Styling:** Tailwind CSS

## Documentazione

- [Backend README](backend/README.md) - Dettagli sul backend Flask
- [Frontend README](frontend/README.md) - Dettagli su template e asset statici
- [JINJA2_GUIDE.md](JINJA2_GUIDE.md) - Guida all'uso di Jinja2

## License

MIT
