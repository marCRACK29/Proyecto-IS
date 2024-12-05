INSERT INTO patient (rut, name) VALUES

('000000001', 'Paciente 1'),
('000000002', 'Paciente 2'),
('000000003', 'Paciente 3'),
('000000004', 'Paciente 4'),
('000000005', 'Paciente 5'),
('000000006', 'Paciente 6'),
('000000007', 'Paciente 7'),
('000000008', 'Paciente 8'),
('000000009', 'Paciente 9');

--

INSERT INTO medic (rut, name, area) VALUES

('100000000', 'Medico 1', 'Especialidad 1'),
('200000000', 'Medico 2', 'Especialidad 2'),
('300000000', 'Medico 3', 'Especialidad 3'),
('400000000', 'Medico 4', 'Especialidad 4'),
('500000000', 'Medico 5', 'Especialidad 5'),
('600000000', 'Medico 6', 'Especialidad 6'),
('700000000', 'Medico 7', 'Especialidad 7'),
('800000000', 'Medico 8', 'Especialidad 8'),
('900000000', 'Medico 9', 'Especialidad 9');

--

INSERT INTO block (start, finish) VALUES

('2023-10-03 08:00:00', '2023-10-03 09:00:00'),
('2023-10-03 09:00:00', '2023-10-03 10:00:00'),
('2023-10-03 10:00:00', '2023-10-03 11:00:00'),
('2023-10-03 11:00:00', '2023-10-03 12:00:00'),
('2023-10-03 12:00:00', '2023-10-03 13:00:00'),
('2023-10-03 13:00:00', '2023-10-03 14:00:00'),
('2023-10-03 14:00:00', '2023-10-03 15:00:00'),
('2023-10-03 15:00:00', '2023-10-03 16:00:00'),
('2023-10-03 16:00:00', '2023-10-03 17:00:00'),
('2023-10-03 17:00:00', '2023-10-03 18:00:00'),
('2023-10-03 18:00:00', '2023-10-03 19:00:00'),

('2023-10-04 08:00:00', '2023-10-04 09:00:00'),
('2023-10-04 09:00:00', '2023-10-04 10:00:00'),
('2023-10-04 10:00:00', '2023-10-04 11:00:00'),
('2023-10-04 11:00:00', '2023-10-04 12:00:00'),
('2023-10-04 12:00:00', '2023-10-04 13:00:00'),
('2023-10-04 13:00:00', '2023-10-04 14:00:00'),
('2023-10-04 14:00:00', '2023-10-04 15:00:00'),
('2023-10-04 15:00:00', '2023-10-04 16:00:00'),
('2023-10-04 16:00:00', '2023-10-04 17:00:00'),
('2023-10-04 17:00:00', '2023-10-04 18:00:00'),
('2023-10-04 18:00:00', '2023-10-04 19:00:00'),

('2023-10-05 08:00:00', '2023-10-05 09:00:00'),
('2023-10-05 09:00:00', '2023-10-05 10:00:00'),
('2023-10-05 10:00:00', '2023-10-05 11:00:00'),
('2023-10-05 11:00:00', '2023-10-05 12:00:00'),
('2023-10-05 12:00:00', '2023-10-05 13:00:00'),
('2023-10-05 13:00:00', '2023-10-05 14:00:00'),
('2023-10-05 14:00:00', '2023-10-05 15:00:00'),
('2023-10-05 15:00:00', '2023-10-05 16:00:00'),
('2023-10-05 16:00:00', '2023-10-05 17:00:00'),
('2023-10-05 17:00:00', '2023-10-05 18:00:00'),
('2023-10-05 18:00:00', '2023-10-05 19:00:00'),

('2023-10-06 08:00:00', '2023-10-06 09:00:00'),
('2023-10-06 09:00:00', '2023-10-06 10:00:00'),
('2023-10-06 10:00:00', '2023-10-06 11:00:00'),
('2023-10-06 11:00:00', '2023-10-06 12:00:00'),
('2023-10-06 12:00:00', '2023-10-06 13:00:00'),
('2023-10-06 13:00:00', '2023-10-06 14:00:00'),
('2023-10-06 14:00:00', '2023-10-06 15:00:00'),
('2023-10-06 15:00:00', '2023-10-06 16:00:00'),
('2023-10-06 16:00:00', '2023-10-06 17:00:00'),
('2023-10-06 17:00:00', '2023-10-06 18:00:00'),
('2023-10-06 18:00:00', '2023-10-06 19:00:00');

--

INSERT INTO agenda (rutM, start) VALUES

-- M.1

('100000000', '2023-10-03 08:00:00'),
('100000000', '2023-10-03 09:00:00'),
('100000000', '2023-10-03 10:00:00'),
('100000000', '2023-10-03 11:00:00'),
('100000000', '2023-10-03 12:00:00'),
('100000000', '2023-10-03 13:00:00'),
('100000000', '2023-10-03 14:00:00'),
('100000000', '2023-10-03 15:00:00'),
('100000000', '2023-10-03 16:00:00'),
('100000000', '2023-10-03 17:00:00'),
('100000000', '2023-10-03 18:00:00'),

('100000000', '2023-10-04 08:00:00'),
('100000000', '2023-10-04 09:00:00'),
('100000000', '2023-10-04 10:00:00'),
('100000000', '2023-10-04 11:00:00'),
('100000000', '2023-10-04 12:00:00'),
('100000000', '2023-10-04 13:00:00'),
('100000000', '2023-10-04 14:00:00'),
('100000000', '2023-10-04 15:00:00'),
('100000000', '2023-10-04 16:00:00'),
('100000000', '2023-10-04 17:00:00'),
('100000000', '2023-10-04 18:00:00'),

('100000000', '2023-10-05 08:00:00'),
('100000000', '2023-10-05 09:00:00'),
('100000000', '2023-10-05 10:00:00'),
('100000000', '2023-10-05 11:00:00'),
('100000000', '2023-10-05 12:00:00'),
('100000000', '2023-10-05 13:00:00'),
('100000000', '2023-10-05 14:00:00'),
('100000000', '2023-10-05 15:00:00'),
('100000000', '2023-10-05 16:00:00'),
('100000000', '2023-10-05 17:00:00'),
('100000000', '2023-10-05 18:00:00'),

('100000000', '2023-10-06 08:00:00'),
('100000000', '2023-10-06 09:00:00'),
('100000000', '2023-10-06 10:00:00'),
('100000000', '2023-10-06 11:00:00'),
('100000000', '2023-10-06 12:00:00'),
('100000000', '2023-10-06 13:00:00'),
('100000000', '2023-10-06 14:00:00'),
('100000000', '2023-10-06 15:00:00'),
('100000000', '2023-10-06 16:00:00'),
('100000000', '2023-10-06 17:00:00'),
('100000000', '2023-10-06 18:00:00'),

-- M.2

('200000000', '2023-10-03 08:00:00'),
('200000000', '2023-10-03 09:00:00'),
('200000000', '2023-10-03 10:00:00'),
('200000000', '2023-10-03 11:00:00'),
('200000000', '2023-10-03 12:00:00'),
('200000000', '2023-10-03 13:00:00'),
('200000000', '2023-10-03 14:00:00'),
('200000000', '2023-10-03 15:00:00'),
('200000000', '2023-10-03 16:00:00'),
('200000000', '2023-10-03 17:00:00'),
('200000000', '2023-10-03 18:00:00'),

('200000000', '2023-10-04 08:00:00'),
('200000000', '2023-10-04 09:00:00'),
('200000000', '2023-10-04 10:00:00'),
('200000000', '2023-10-04 11:00:00'),
('200000000', '2023-10-04 12:00:00'),
('200000000', '2023-10-04 13:00:00'),
('200000000', '2023-10-04 14:00:00'),
('200000000', '2023-10-04 15:00:00'),
('200000000', '2023-10-04 16:00:00'),
('200000000', '2023-10-04 17:00:00'),
('200000000', '2023-10-04 18:00:00'),

('200000000', '2023-10-05 08:00:00'),
('200000000', '2023-10-05 09:00:00'),
('200000000', '2023-10-05 10:00:00'),
('200000000', '2023-10-05 11:00:00'),
('200000000', '2023-10-05 12:00:00'),
('200000000', '2023-10-05 13:00:00'),
('200000000', '2023-10-05 14:00:00'),
('200000000', '2023-10-05 15:00:00'),
('200000000', '2023-10-05 16:00:00'),
('200000000', '2023-10-05 17:00:00'),
('200000000', '2023-10-05 18:00:00'),

('200000000', '2023-10-06 08:00:00'),
('200000000', '2023-10-06 09:00:00'),
('200000000', '2023-10-06 10:00:00'),
('200000000', '2023-10-06 11:00:00'),
('200000000', '2023-10-06 12:00:00'),
('200000000', '2023-10-06 13:00:00'),
('200000000', '2023-10-06 14:00:00'),
('200000000', '2023-10-06 15:00:00'),
('200000000', '2023-10-06 16:00:00'),
('200000000', '2023-10-06 17:00:00'),
('200000000', '2023-10-06 18:00:00'),

-- M.3

('300000000', '2023-10-03 08:00:00'),
('300000000', '2023-10-03 09:00:00'),
('300000000', '2023-10-03 10:00:00'),
('300000000', '2023-10-03 11:00:00'),
('300000000', '2023-10-03 12:00:00'),
('300000000', '2023-10-03 13:00:00'),
('300000000', '2023-10-03 14:00:00'),
('300000000', '2023-10-03 15:00:00'),
('300000000', '2023-10-03 16:00:00'),
('300000000', '2023-10-03 17:00:00'),
('300000000', '2023-10-03 18:00:00'),

('300000000', '2023-10-04 08:00:00'),
('300000000', '2023-10-04 09:00:00'),
('300000000', '2023-10-04 10:00:00'),
('300000000', '2023-10-04 11:00:00'),
('300000000', '2023-10-04 12:00:00'),
('300000000', '2023-10-04 13:00:00'),
('300000000', '2023-10-04 14:00:00'),
('300000000', '2023-10-04 15:00:00'),
('300000000', '2023-10-04 16:00:00'),
('300000000', '2023-10-04 17:00:00'),
('300000000', '2023-10-04 18:00:00'),

('300000000', '2023-10-05 08:00:00'),
('300000000', '2023-10-05 09:00:00'),
('300000000', '2023-10-05 10:00:00'),
('300000000', '2023-10-05 11:00:00'),
('300000000', '2023-10-05 12:00:00'),
('300000000', '2023-10-05 13:00:00'),
('300000000', '2023-10-05 14:00:00'),
('300000000', '2023-10-05 15:00:00'),
('300000000', '2023-10-05 16:00:00'),
('300000000', '2023-10-05 17:00:00'),
('300000000', '2023-10-05 18:00:00'),

('300000000', '2023-10-06 08:00:00'),
('300000000', '2023-10-06 09:00:00'),
('300000000', '2023-10-06 10:00:00'),
('300000000', '2023-10-06 11:00:00'),
('300000000', '2023-10-06 12:00:00'),
('300000000', '2023-10-06 13:00:00'),
('300000000', '2023-10-06 14:00:00'),
('300000000', '2023-10-06 15:00:00'),
('300000000', '2023-10-06 16:00:00'),
('300000000', '2023-10-06 17:00:00'),
('300000000', '2023-10-06 18:00:00'),

-- M.4

('400000000', '2023-10-03 08:00:00'),
('400000000', '2023-10-03 09:00:00'),
('400000000', '2023-10-03 10:00:00'),
('400000000', '2023-10-03 11:00:00'),
('400000000', '2023-10-03 12:00:00'),
('400000000', '2023-10-03 13:00:00'),
('400000000', '2023-10-03 14:00:00'),
('400000000', '2023-10-03 15:00:00'),
('400000000', '2023-10-03 16:00:00'),
('400000000', '2023-10-03 17:00:00'),
('400000000', '2023-10-03 18:00:00'),

('400000000', '2023-10-04 08:00:00'),
('400000000', '2023-10-04 09:00:00'),
('400000000', '2023-10-04 10:00:00'),
('400000000', '2023-10-04 11:00:00'),
('400000000', '2023-10-04 12:00:00'),
('400000000', '2023-10-04 13:00:00'),
('400000000', '2023-10-04 14:00:00'),
('400000000', '2023-10-04 15:00:00'),
('400000000', '2023-10-04 16:00:00'),
('400000000', '2023-10-04 17:00:00'),
('400000000', '2023-10-04 18:00:00'),

('400000000', '2023-10-05 08:00:00'),
('400000000', '2023-10-05 09:00:00'),
('400000000', '2023-10-05 10:00:00'),
('400000000', '2023-10-05 11:00:00'),
('400000000', '2023-10-05 12:00:00'),
('400000000', '2023-10-05 13:00:00'),
('400000000', '2023-10-05 14:00:00'),
('400000000', '2023-10-05 15:00:00'),
('400000000', '2023-10-05 16:00:00'),
('400000000', '2023-10-05 17:00:00'),
('400000000', '2023-10-05 18:00:00'),

('400000000', '2023-10-06 08:00:00'),
('400000000', '2023-10-06 09:00:00'),
('400000000', '2023-10-06 10:00:00'),
('400000000', '2023-10-06 11:00:00'),
('400000000', '2023-10-06 12:00:00'),
('400000000', '2023-10-06 13:00:00'),
('400000000', '2023-10-06 14:00:00'),
('400000000', '2023-10-06 15:00:00'),
('400000000', '2023-10-06 16:00:00'),
('400000000', '2023-10-06 17:00:00'),
('400000000', '2023-10-06 18:00:00'),

-- M.5

('500000000', '2023-10-03 08:00:00'),
('500000000', '2023-10-03 09:00:00'),
('500000000', '2023-10-03 10:00:00'),
('500000000', '2023-10-03 11:00:00'),
('500000000', '2023-10-03 12:00:00'),
('500000000', '2023-10-03 13:00:00'),
('500000000', '2023-10-03 14:00:00'),
('500000000', '2023-10-03 15:00:00'),
('500000000', '2023-10-03 16:00:00'),
('500000000', '2023-10-03 17:00:00'),
('500000000', '2023-10-03 18:00:00'),

('500000000', '2023-10-04 08:00:00'),
('500000000', '2023-10-04 09:00:00'),
('500000000', '2023-10-04 10:00:00'),
('500000000', '2023-10-04 11:00:00'),
('500000000', '2023-10-04 12:00:00'),
('500000000', '2023-10-04 13:00:00'),
('500000000', '2023-10-04 14:00:00'),
('500000000', '2023-10-04 15:00:00'),
('500000000', '2023-10-04 16:00:00'),
('500000000', '2023-10-04 17:00:00'),
('500000000', '2023-10-04 18:00:00'),

('500000000', '2023-10-05 08:00:00'),
('500000000', '2023-10-05 09:00:00'),
('500000000', '2023-10-05 10:00:00'),
('500000000', '2023-10-05 11:00:00'),
('500000000', '2023-10-05 12:00:00'),
('500000000', '2023-10-05 13:00:00'),
('500000000', '2023-10-05 14:00:00'),
('500000000', '2023-10-05 15:00:00'),
('500000000', '2023-10-05 16:00:00'),
('500000000', '2023-10-05 17:00:00'),
('500000000', '2023-10-05 18:00:00'),

('500000000', '2023-10-06 08:00:00'),
('500000000', '2023-10-06 09:00:00'),
('500000000', '2023-10-06 10:00:00'),
('500000000', '2023-10-06 11:00:00'),
('500000000', '2023-10-06 12:00:00'),
('500000000', '2023-10-06 13:00:00'),
('500000000', '2023-10-06 14:00:00'),
('500000000', '2023-10-06 15:00:00'),
('500000000', '2023-10-06 16:00:00'),
('500000000', '2023-10-06 17:00:00'),
('500000000', '2023-10-06 18:00:00');