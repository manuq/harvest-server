select DATE(FROM_UNIXTIME(s.timestamp)) as fecha, truncate(s.spent_time/60, 2) as duracion, t.serial_number as serial_number, t.departamento as departamento, t.tipo_institucion as tipo_institucion, t.codigo_institucion as codigo_institucion, t.perfil as perfil, t.grado as grado, t.fecha_nac as fecha_nac, t.modelo_equipo as modelo_equipo
from sessions s, tilo t 
where t.serial_number = s.serial_number
and codigo_institucion in (select codigo_institucion from muestras where id_muestra = 2)
