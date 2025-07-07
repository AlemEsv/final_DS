from flask import Flask, jsonify
import psycopg2
import os
import time

# Despliegue de una aplicación mediante flask
app = Flask(__name__)

def get_db_connection():
    """Conexión a PostgreSQL"""
    for attempt in range(3):
        try:
            # Crea la conexión mediante psycopg a una base de datos de postgreSQL mediante psycopg2
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
def home():
    return jsonify({
        "service": "app-legacy",
        "status": "running",
        "message": "Aplicacion legacy funcionando"
    })

@app.route('/users')
def get_users():
    """Obtener todos los usuarios"""
    try:
        # Conexión con la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        # selecciona la tabla de usuarios (admin, test-user)
        cursor.execute("SELECT id, username, email, created_at FROM users")

        # guarda en una lista los usuarios
        users = cursor.fetchall()

        # termina la conexión con la base de datos
        cursor.close()
        connection.close()
        
        users_list = []
        # guarda en una lista diccionarios con los datos de la base de datos
        for user in users:
            users_list.append({
                "id": user[0],
                "username": user[1],
                "email": user[2],
                "created_at": str(user[3])
            })
        
        return jsonify({
            "service": "app-legacy",
            "users": users_list
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Verificar estado del servicio desplegado
@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "app-legacy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)