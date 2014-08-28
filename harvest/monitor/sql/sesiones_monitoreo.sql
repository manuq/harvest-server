SELECT 'fecha','duracion','uuid','fecha_act','serial_number',
'departamento','tipo_institucion', 'codigo_institucion', 'perfil','grado','fecha_nac','modelo_equipo'
UNION ALL
(select DATE(FROM_UNIXTIME(s.timestamp)), truncate(s.spent_time/60, 2), t.* 
from sessions s, tilo t 
where t.serial_number = s.serial_number)
