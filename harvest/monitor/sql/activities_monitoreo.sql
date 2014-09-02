SELECT 'actividad','fecha','duracion_sugar','uuid','fecha_act','serial_number',
'departamento','tipo_institucion', 'codigo_institucion', 'perfil','grado','fecha_nac','modelo_equipo'
UNION ALL
(select ifnull(activity_name,x.bundle_id), DATE(FROM_UNIXTIME(x.timestamp)),
truncate(x.duracion,2), t.* from
(select *, SUM(spent_time) as duracion 
from launches l
group by bundle_id, serial_number
order by bundle_id) x
join (
	select * from tilo
	group by serial_number) t
on t.serial_number = x.serial_number
left join (
select bundle_id, activity_name from activities
) y
on x.bundle_id = y.bundle_id);
