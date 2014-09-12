SELECT ROUND(sum( data_length + index_length ) / 1024 / 1024) as size
FROM information_schema.TABLES 
where table_schema='harvest'
