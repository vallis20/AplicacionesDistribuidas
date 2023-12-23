CREATE DATABASE	Contenido;
USE Contenido;

CREATE TABLE Usuarios (
    usr_id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    passwordw VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    fecha_date_registro DATETIME DEFAULT GETDATE()
);

CREATE TABLE Streaming (
    streaming_id INT IDENTITY(1,1) PRIMARY KEY, 
    title VARCHAR(255) NOT NULL,
	formt VARCHAR(20),
    duration INT, 
	upload_date DATETIME DEFAULT GETDATE(),
);

CREATE TABLE Audio (
    audio_id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    formt VARCHAR(20),
    duration INT,  
    upload_date DATETIME DEFAULT GETDATE() 
);

CREATE TABLE Reportes (
    reportes_id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
	typeR VARCHAR(50) NOT NULL, --Facturacion, estadisticas
    upload_date DATETIME DEFAULT GETDATE() 
);

CREATE TABLE Descargas (
    download_id INT IDENTITY(1,1) PRIMARY KEY,
    fecha_descarga DATETIME DEFAULT CURRENT_TIMESTAMP,
    f_usr_id INT,
    f_streaming_id INT,
    --f_audio_id INT,
	f_reportes_id INT,
	FOREIGN KEY (f_usr_id) REFERENCES Usuarios(usr_id),
	FOREIGN KEY (f_streaming_id) REFERENCES Streaming(streaming_id),
	--FOREIGN KEY (f_audio_id) REFERENCES Audio(audio_id),
	FOREIGN KEY (f_reportes_id) REFERENCES Reportes(reportes_id),
);

-- Insertar registros en la tabla Usuarios
INSERT INTO Usuarios (username, passwordw, email, nombre, apellido) 
VALUES 
('usuario1', 'contrasena1', 'usuario1@email.com', 'Nombre1', 'Apellido1'),
('usuario2', 'contrasena2', 'usuario2@email.com', 'Nombre2', 'Apellido2'),
('usuario3', 'contrasena3', 'usuario3@email.com', 'Nombre3', 'Apellido3'),
('usuario4', 'contrasena4', 'usuario4@email.com', 'Nombre4', 'Apellido4'),
('usuario5', 'contrasena5', 'usuario5@email.com', 'Nombre5', 'Apellido5');

-- Insertar registros en la tabla Streaming
INSERT INTO Streaming (title, formt, duration) 
VALUES ('No descargo', '0', 0)

INSERT INTO Streaming (title, formt, duration) 
VALUES 
('Stream1','mp4', 120),
('Stream2','avi', 150),
('Stream3','mkv', 180),
('Stream4','mp4', 130),
('Stream5','avi', 160);

-- Insertar registros en la tabla Audio
INSERT INTO Audio (title, formt, duration) 
VALUES 
('No descargo','', 0)

INSERT INTO Audio (title, formt, duration) 
VALUES 
('Audio1','mp3', 180),
('Audio2','wav', 200),
('Audio3','mp3', 150),
('Audio4','wav', 170),
('Audio5','mp3', 190);

-- Insertar registros en la tabla Reportes

INSERT INTO Reportes (title, typeR) 
VALUES ('No descargo', '0')

INSERT INTO Reportes (title, typeR) 
VALUES 
('Reporte1', 'Facturacion'),
('Reporte2', 'Estadisticas'),
('Reporte3', 'Facturacion'),
('Reporte4', 'Estadisticas'),
('Reporte5', 'Facturacion');

-- Insertar registros en la tabla Descargas
INSERT INTO Descargas (f_usr_id, f_streaming_id, f_reportes_id) 
VALUES 
(1, 1, 6),
(2, 1, 6),
(3, 4, 1),
(4, 1, 4),
(5, 4, 1);

/*INSERT INTO Descargas (f_usr_id, f_streaming_id, f_audio_id, f_reportes_id) 
VALUES 
(1, 1, 6, 6),
(2, 1, 5, 6),
(3, 4, 2, 1),
(4, 1, 3, 4),
(5, 4, 5, 1);*/

SELECT*FROM Descargas
SELECT*FROM Usuarios

-- Consulta para mostrar datos de descargas con información relacionada
SELECT
    d.download_id,
    d.fecha_descarga,
    u.username AS usuario,
    s.title AS streaming_title,
   -- a.title AS audio_title,
    r.title AS reporte_title
FROM
    Descargas d
JOIN
    Usuarios u ON d.f_usr_id = u.usr_id
LEFT JOIN
    Streaming s ON d.f_streaming_id = s.streaming_id
--LEFT JOIN
   -- Audio a ON d.f_audio_id = a.audio_id
LEFT JOIN
    Reportes r ON d.f_reportes_id = r.reportes_id;

DROP DATABASE Contenido