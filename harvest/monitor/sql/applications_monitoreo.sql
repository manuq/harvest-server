SELECT 'aplicacion','fecha','duracion_gnome','uuid','fecha_act','serial_number',
'departamento','tipo_institucion', 'codigo_institucion', 'perfil','grado','fecha_nac','modelo_equipo'
UNION ALL
(select ifnull(app_id,x.app_name), DATE(FROM_UNIXTIME(x.timestamp)),
truncate(x.duracion,2), t.* from
(select timestamp, app_name, serial_number, SUM(spent_time)/60 as duracion 
from gnome_launches l
where l.app_name != ''
and l.spent_time > 0
and l.app_name not in ( select app_name from gnome_alias where enabled=0)
group by serial_number, app_name, DATE(FROM_UNIXTIME(timestamp))
order by app_name) x
join (
	select * from tilo
	where codigo_institucion in (select codigo_institucion from muestras where id_muestra = 2)
	group by serial_number) t
on t.serial_number = x.serial_number
left join (
select app_name, app_id from gnome_alias    
) y
on x.app_name = y.app_name);
