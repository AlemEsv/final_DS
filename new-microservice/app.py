from flask import Flask, jsonify, request
import psycopg2
import os
import time

app = Flask(__name__)
@app.route('/api')
def home():
    return jsonify({
        "service": "new-microservice",
        "status": "running",
        "message": "Microservicio funcionando"
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "service": "new-microservice"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)