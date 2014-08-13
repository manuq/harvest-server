select ifnull(a.activity_name, s.bundle_id), DATE(FROM_UNIXTIME(s.timestamp)) as fecha, s.serial_number, SUM(s.spent_time)/60 as duracion_sugar, t.* 
from launches s, activities a, tilo t 
where s.bundle_id = a.bundle_id and s.serial_number = t.serial_number 
group by s.serial_number, DATE(FROM_UNIXTIME(s.timestamp)), s.bundle_id;
