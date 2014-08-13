SELECT 'aplicacion','fecha','serial_number','duracion_sugar','uuid','fecha_act','serial_number',
'departamento','tipo_institucion', 'codigo_institucion', 'perfil','grado','fecha_nac','modelo_equipo'
UNION ALL
(select ifnull(a.app_id, s.app_name), DATE(FROM_UNIXTIME(s.timestamp)) as fecha, s.serial_number, SUM(s.spent_time)/60 as duracion_gnome, t.*
from gnome_launches s, gnome_alias a, tilo t
where s.app_name = a.app_name and s.serial_number = t.serial_number
group by s.serial_number, DATE(FROM_UNIXTIME(s.timestamp)), s.app_name)

