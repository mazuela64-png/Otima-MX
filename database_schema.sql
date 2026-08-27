-- Estructura de Base de Datos para O'tima México - Control Comercial

CREATE TABLE laboratorios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(150) NOT NULL,
    tipo_industria VARCHAR(50) DEFAULT 'Farmacéutica / Dispositivos Médicos',
    pais VARCHAR(50) DEFAULT 'México',
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    laboratorio_id INT,
    nombre_contacto VARCHAR(150) NOT NULL,
    cargo VARCHAR(100),
    perfil_linkedin VARCHAR(255),
    estatus VARCHAR(50) DEFAULT 'Por Contactar', -- Por Contactar, Contactado, En Conversación, Reunión Agendada, Propuesta Enviada
    canal_acercamiento VARCHAR(50) DEFAULT 'LinkedIn',
    fecha_contacto DATE,
    fecha_seguimiento DATE,
    notas_estrategia TEXT,
    FOREIGN KEY (laboratorio_id) REFERENCES laboratorios(id)
);

-- Tabla para el registro de módulos O'tima ofertados en México
CREATE TABLE modulos_ofertados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_modulo VARCHAR(100) NOT NULL, -- O'tima ETL, Cadi, O'tima Core, O'target, O'timaWeb
    descripcion VARCHAR(255)
);
