select IFNULL(app_id, x.app_name), fecha, duracion, uuid, serial_number, departamento, tipo_institucion, codigo_institucion, perfil, grado, fecha_nac, modelo_equipo from (
select l.app_name, DATE(FROM_UNIXTIME(timestamp)) as fecha, truncate(SUM(spent_time)/60,2) as duracion, t.uuid, t.serial_number, t.departamento, t.tipo_institucion, t.codigo_institucion, t.perfil, t.grado, t.fecha_nac, t.modelo_equipo
from gnome_launches l, tilo t
where l.app_name != ''
and t.serial_number=l.serial_number
and l.app_name not in ( select g.app_name from gnome_alias g where enabled=0)
and t.codigo_institucion in (select codigo_institucion from muestras where id_muestra = 2)
group by l.serial_number, l.app_name, DATE(FROM_UNIXTIME(l.timestamp))
) x
left join (
select app_id, app_name from gnome_alias
) y
on x.app_name = y.app_name;
