select x.fecha, x.serial_number, duracion_sugar, duracion_gnome, t.* from (
  select DATE(FROM_UNIXTIME(s.timestamp)) as fecha, s.serial_number, SUM(s.spent_time)/60 as duracion_sugar
  from sessions s
  where s.is_sugar = 1
  group by s.serial_number, DATE(FROM_UNIXTIME(s.timestamp))
) as x, (
  select DATE(FROM_UNIXTIME(s.timestamp)) as fecha, s.serial_number, SUM(s.spent_time)/60 as duracion_gnome
  from sessions s
  where s.is_sugar = 0
  group by s.serial_number, DATE(FROM_UNIXTIME(s.timestamp))
) as y,
tilo t
where x.fecha = y.fecha and x.serial_number = y.serial_number and t.serial_number = x.serial_number;
