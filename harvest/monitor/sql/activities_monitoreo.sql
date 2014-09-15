SELECT 'actividad','fecha','duracion_sugar','uuid','fecha_act','serial_number',
'departamento','tipo_institucion', 'codigo_institucion', 'perfil','grado','fecha_nac','modelo_equipo'
UNION ALL
(select ifnull(activity_name,x.bundle_id), DATE(FROM_UNIXTIME(x.timestamp)),
truncate(x.duracion,2), t.* from
(select *, SUM(spent_time) as duracion 
from launches l
where l.bundle_id <> ''
and l.spent_time > 0
and l.bundle_id not in ( select bundle_id from activities where enabled=0)
group by bundle_id, serial_number, DATE(FROM_UNIXTIME(timestamp))
order by bundle_id) x
join (
	select * from tilo t 
	where codigo_institucion in (select codigo_institucion from muestras where id_muestra = 1)
	group by serial_number) t
on t.serial_number = x.serial_number
left join (
select bundle_id, activity_name from activities
) y
on x.bundle_id = y.bundle_id);
