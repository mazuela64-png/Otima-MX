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
    contactado_linkedin BOOLEAN DEFAULT FALSE,
    conexion_aceptada BOOLEAN DEFAULT FALSE,
    estatus_seguimiento VARCHAR(100) DEFAULT 'Pendiente de Cita', -- Pendiente de Cita, Cita Agendada, Presentación Realizada
    fecha_cita_propuesta DATE NULL,
    canal_acercamiento VARCHAR(50) DEFAULT 'LinkedIn',
    fecha_contacto DATE,
    fecha_seguimiento DATE,
    notas_estrategia TEXT,
    FOREIGN KEY (laboratorio_id) REFERENCES laboratorios(id)
);

-- Módulos O'tima
CREATE TABLE modulos_ofertados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_modulo VARCHAR(100) NOT NULL, 
    descripcion VARCHAR(255)
);
