SELECT 'fecha', 'is_sugar', 'duracion', 'uuid', 'fecha_act', 'serial_number', 'departamento',
'tipo_institucion', 'codigo_institucion', 'perfil', 'grado', 'fecha_nac', 'modelo_equipo'
UNION ALL 
SELECT DATE(FROM_UNIXTIME(s.timestamp)) as fecha, s.is_sugar, SUM(s.spent_time)/60 as duracion, t.*
FROM sessions s
JOIN tilo t ON s.serial_number = t.serial_number 
GROUP BY s.serial_number, DATE(FROM_UNIXTIME(s.timestamp)), is_sugar
