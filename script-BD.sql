-- Creación de tablas.

create table "proyect".paciente (
	rut_p varchar(9) primary key not null,
	nombre varchar(90) not null
);

create table "proyect".medico (
	rut_m varchar(9) primary key not null,
	nombre varchar(90) not null,
	especialidad varchar(50) not null
);

create table "proyect".bloque (
	id_b int4 primary key not null,
	dia varchar(1)not null check (dia in ('L','M','X','J','V')),
	hora_i time not null,
	hora_t time not null
);

create table "proyect".horario (
	rut_m varchar(9) not null,
	id_b int4 not null,
	estado varchar(20) default 'disponible',
	foreign key(rut_m) references medico(rut_m),
	foreign key(id_b) references bloque(id_b),
	primary key(rut_m,id_b)
);

create table "proyect".cita (
	id_c int4 primary key not null,
	rut_m varchar(9) not null,
	id_b int4 not null,
	rut_p varchar(9) not null,
	foreign key(rut_m) references medico(rut_m),
	foreign key(id_b) references bloque(id_b),
	foreign key(rut_p) references paciente(rut_p)
);


-- Poblar las tablas

insert into "proyect".bloque (id_b,dia,hora_i,hora_t) values
(1,'L','08:00','09:00'),
(2,'L','09:00','10:00'),
(3,'L','10:00','11:00'),
(4,'L','11:00','12:00'),
(5,'L','12:00','13:00'),
(6,'L','13:00','14:00'),
(7,'L','14:00','15:00'),
(8,'L','15:00','16:00'),
(9,'L','16:00','17:00'),
(10,'L','18:00','19:00'),
(11,'L','19:00','20:00'),
(12,'L','20:00','21:00'),
(13,'M','08:00','09:00'),
(14,'M','09:00','10:00'),
(15,'M','10:00','11:00'),
(16,'M','11:00','12:00'),
(17,'M','12:00','13:00'),
(18,'M','13:00','14:00'),
(19,'M','14:00','15:00'),
(20,'M','15:00','16:00'),
(21,'M','16:00','17:00'),
(22,'M','18:00','19:00'),
(23,'M','19:00','20:00'),
(24,'M','20:00','21:00'),
(25,'X','08:00','09:00'),
(26,'X','09:00','10:00'),
(27,'X','10:00','11:00'),
(28,'X','11:00','12:00'),
(29,'X','12:00','13:00'),
(30,'X','13:00','14:00'),
(31,'X','14:00','15:00'),
(32,'X','15:00','16:00'),
(33,'X','16:00','17:00'),
(34,'X','18:00','19:00'),
(35,'X','19:00','20:00'),
(36,'X','20:00','21:00'),
(37,'J','08:00','09:00'),
(38,'J','09:00','10:00'),
(39,'J','10:00','11:00'),
(40,'J','11:00','12:00'),
(41,'J','12:00','13:00'),
(42,'J','13:00','14:00'),
(43,'J','14:00','15:00'),
(44,'J','15:00','16:00'),
(45,'J','16:00','17:00'),
(46,'J','18:00','19:00'),
(47,'J','19:00','20:00'),
(48,'J','20:00','21:00'),
(49,'V','08:00','09:00'),
(50,'V','09:00','10:00'),
(51,'V','10:00','11:00'),
(52,'V','11:00','12:00'),
(53,'V','12:00','13:00'),
(54,'V','13:00','14:00'),
(55,'V','14:00','15:00'),
(56,'V','15:00','16:00'),
(57,'V','16:00','17:00'),
(58,'V','18:00','19:00'),
(59,'V','19:00','20:00'),
(60,'V','20:00','21:00');

insert into "proyect".medico (rut_m,nombre,especialidad) values
('12456832k','Juan Perez','Cardiología'),
('94321765','Maria Kolvea','Dermatología'),
('146438497','Luis Martinez','Neurología'),
('133724751','Miguel Gomez','Oftalmología'),
('164378436','Sofia Diaz','Pediatría');

insert into "proyect".paciente (rut_p,nombre) values
('21324726k','Joaquin Umana'),
('83256847','Isabel Uribe'),
('186547888','Gonzalo Tapia'),
('203119542','Victoria Concha'),
('245763289','Cristián Lopez');

insert into "proyect".horario (rut_m,id_b) values
('12456832k',1),
('12456832k',3),
('12456832k',5),
('12456832k',7),
('12456832k',9),
('12456832k',11),
('12456832k',13),
('12456832k',15),
('12456832k',17),
('12456832k',19),
('12456832k',21),
('12456832k',23),
('94321765',2),
('94321765',4),
('94321765',6),
('94321765',8),
('94321765',10),
('94321765',12),
('94321765',14),
('94321765',16),
('94321765',18),
('94321765',20),
('94321765',22),
('94321765',24),
('146438497',25),
('146438497',27),
('146438497',29),
('146438497',31),
('146438497',33),
('146438497',35),
('146438497',37),
('146438497',39),
('146438497',41),
('146438497',43),
('146438497',45),
('146438497',47),
('133724751',26),
('133724751',28),
('133724751',30),
('133724751',32),
('133724751',34),
('133724751',36),
('133724751',38),
('133724751',40),
('133724751',42),
('133724751',44),
('133724751',46),
('164378436',49),
('164378436',51),
('164378436',53),
('164378436',55),
('164378436',57);


-- Luego de poblar la base de datos, exceptuando la tabla citas. Se necesita crear una función para que al ingresar una cita, se cambie el estado de ese "cupo" en la tabla horarios.

create or replace function block_disp()
returns trigger as $$
begin 
	-- Cambia estado de disponible a no disponible
	update "proyect".horario
	set estado = 'no disponible'
	where rut_m = new.rut_m and id_b = new.id_b;
	
	return new;
end;
$$ language plpgsql;

-- Después de crear la función, se necesita un trigger para que ejecute la función cada que vez que se inserte una cita a la BD. 

create trigger trigger_block_disp
after insert on "proyect".cita
for each row 
execute procedure block_disp();


