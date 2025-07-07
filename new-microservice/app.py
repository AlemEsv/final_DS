from flask import Flask, jsonify, request
import psycopg2
import os
import time
import requests

app = Flask(__name__)

def get_db_connection():
    """Conexión a PostgreSQL"""
    for attempt in range(3):
        try:
            conn = psycopg2.connect(
                host=os.getenv('POSTGRES_HOST', 'localhost'),
                database=os.getenv('POSTGRES_DB', 'db'),
                user=os.getenv('POSTGRES_USER', 'user'),
                password=os.getenv('POSTGRES_PASSWORD', 'pass')
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"Intento {attempt + 1}: Error conectando a DB: {e}")
            time.sleep(5)
    raise Exception("No se pudo conectar a la base de datos")

@app.route('/')
@app.route('/api')
def home():
    return jsonify({
        "service": "new-microservice",
        "status": "running",
        "message": "Microservicio funcionando"
    })

@app.route('/api/users')
def get_users_from_legacy():
    """Proxy para obtener usuarios desde la aplicación legacy"""
    try:
        # Como están en el mismo pod, puede usar localhost
        legacy_url = os.getenv('LEGACY_APP_URL', 'http://localhost:5000')
        response = requests.get(f"{legacy_url}/users")
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                "service": "new-microservice",
                "source": "app-legacy",
                "data": data
            })
        else:
            return jsonify({"error": "No se pudo obtener datos de legacy"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/status')
def status():
    return jsonify({
        "service": "new-microservice",
        "api_key": os.getenv('API_KEY', 'not-set'),
        "legacy_url": os.getenv('LEGACY_APP_URL', 'not-set')
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "service": "new-microservice"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)