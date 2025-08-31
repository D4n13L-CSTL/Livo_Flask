CREATE TABLE usuarios (
  "id" serial PRIMARY KEY,
  "username" text,
  "email" text UNIQUE,
  "password" text,
  "tipo_de_user_id" int
);

CREATE TABLE clubes (
  "id" serial PRIMARY KEY,
  "nombre" text,
  "administrador" text,
  "email" text,
  "telefono" text,
  "fecha_create" date,
  "fecha_update" date
);

CREATE TABLE roles_de_club (
  "id" serial PRIMARY KEY,
  "nombre" text
);  

CREATE TABLE clubes_usuarios (
  "id" serial PRIMARY KEY,
  "id_usuario" int,
  "id_club" int,
  "id_rol" int
);

CREATE TABLE atletas (
  "id" serial PRIMARY KEY,
  "id_usuario" int,
  "nombres" text,
  "apellidos" text,
  "cedula" text,
  "fecha_nacimiento" date,
  "direccion" text,
  "telefono" text,
  "email" text
);

CREATE TABLE club_atleta (
  "id" serial PRIMARY KEY,
  "id_atleta" int,
  "id_club" int,
  "fecha_registro" date
);

CREATE TABLE formulario_registro_atleta (
  "id" serial PRIMARY KEY,
  "formulario" jsonb,
  "id_club" int
);

CREATE TABLE respuestas_formulario_atleta (
    id serial PRIMARY KEY,
    id_atleta int NOT NULL REFERENCES atletas(id),
    id_formulario int NOT NULL REFERENCES formulario_registro_atleta(id),
    respuestas jsonb NOT NULL,
    fecha_respuesta timestamp DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE tipo_de_user(
  id serial PRIMARY KEY,
  nombre text
)


-- Tabla de tipos de eventos
CREATE TABLE tipo_eventos (
    id_tipo SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla de eventos
CREATE TABLE eventos (
    id_evento SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    fecha DATE NOT NULL,
    hora TIME,
    id_tipo INT NOT NULL,
    FOREIGN KEY (id_tipo) REFERENCES tipo_eventos(id_tipo)
);

-- Tabla de relación entre clubes y eventos (N:M)
CREATE TABLE eventos_club (
    id_club INT NOT NULL,
    id_evento INT NOT NULL,
    PRIMARY KEY (id_club, id_evento),
    FOREIGN KEY (id_club) REFERENCES clubes(id) ON DELETE CASCADE,
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento) ON DELETE CASCADE
);

ALTER TABLE "clubes_usuarios" ADD FOREIGN KEY ("id_club") REFERENCES "clubes" ("id");

ALTER TABLE "clubes_usuarios" ADD FOREIGN KEY ("id_usuario") REFERENCES "usuarios" ("id");

ALTER TABLE "clubes_usuarios" ADD FOREIGN KEY ("id_rol") REFERENCES "roles_de_club" ("id");

ALTER TABLE "atletas" ADD FOREIGN KEY ("id_usuario") REFERENCES "usuarios" ("id");

ALTER TABLE "club_atleta" ADD FOREIGN KEY ("id_club") REFERENCES "clubes" ("id");

ALTER TABLE "club_atleta" ADD FOREIGN KEY ("id_atleta") REFERENCES "atletas" ("id");

ALTER TABLE "formulario_registro_atleta" ADD FOREIGN KEY ("id_club") REFERENCES "clubes" ("id");

ALTER TABLE "usuarios" ADD FOREIGN KEY ("tipo_de_user_id") REFERENCES "tipo_de_user" ("id");

