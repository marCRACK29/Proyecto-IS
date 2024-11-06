CREATE TABLE "IS".paciente (
	rut_p varchar(9) NOT NULL,
	nombre varchar(90) NULL,
	CONSTRAINT paciente_pkey PRIMARY KEY (rut_p)
);

CREATE TABLE "IS".medico (
	rut_m varchar(9) NOT NULL,
	nombre varchar(90) NULL,
	especialidad varchar(50) NULL,
	CONSTRAINT medico_pkey PRIMARY KEY (rut_m)
);

CREATE TABLE "IS".bloque (
	id_b int4 NOT NULL,
	dia varchar(1) NULL,
	h_i time NULL,
	h_t time NULL,
	CONSTRAINT bloque_dia_check CHECK (((dia)::text = ANY ((ARRAY['L'::character varying, 'M'::character varying, 'X'::character varying, 'J'::character varying, 'V'::character varying])::text[]))),
	CONSTRAINT bloque_pkey PRIMARY KEY (id_b)
);

CREATE TABLE "IS".horario (
	rut_m varchar(9) NOT NULL,
	id_b int4 NOT NULL,
	CONSTRAINT horario_pkey PRIMARY KEY (rut_m, id_b),
	CONSTRAINT horario_id_b_fkey FOREIGN KEY (id_b) REFERENCES "IS".bloque(id_b),
	CONSTRAINT horario_rut_m_fkey FOREIGN KEY (rut_m) REFERENCES "IS".medico(rut_m)
);

CREATE TABLE "IS".cita (
	id_c int4 NOT NULL,
	rut_m varchar(9) NOT NULL,
	id_b int4 NOT NULL,
	rut_p varchar(9) NOT NULL,
	CONSTRAINT cita_pkey PRIMARY KEY (id_c),
	CONSTRAINT cita_rut_m_fkey FOREIGN KEY (rut_m,id_b) REFERENCES "IS".horario(rut_m,id_b),
	CONSTRAINT cita_rut_p_fkey FOREIGN KEY (rut_p) REFERENCES "IS".paciente(rut_p)
);