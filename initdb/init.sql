-- Creacion de base de datos de usuarios
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Coloca usuarios admin y uno de prueba
INSERT INTO users (username, email) VALUES
    ('admin', 'admin@example.com'),
    ('user-test', 'test@example.com');