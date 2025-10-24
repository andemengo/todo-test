from app import create_app

app = create_app()

if __name__ == '__main__':
    # Usa porta 5001 invece di 5000 (5000 è occupata da ControlCenter su Mac)
    app.run(debug=True, port=5001)
