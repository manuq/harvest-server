SELECT 'actividad','fecha','serial_number','duracion_sugar','uuid','fecha_act','serial_number',
'departamento','tipo_institucion', 'codigo_institucion', 'perfil','grado','fecha_nac','modelo_equipo'
UNION ALL
(select ifnull(a.activity_name, s.bundle_id), DATE(FROM_UNIXTIME(s.timestamp)) as fecha, s.serial_number, 
truncate(SUM(s.spent_time)/60, 2) as duracion_sugar, t.*  duracion_sugar, t.* 
from launches s, activities a, tilo t 
where s.bundle_id = a.bundle_id and s.serial_number = t.serial_number 
group by s.serial_number, DATE(FROM_UNIXTIME(s.timestamp)), s.bundle_id)
