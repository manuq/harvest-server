mysql -u root -p < misc/drop.sql
mysql -u root -p < sql/001-harvest.sql
mysql -u root -p harvest < sql/002-initial-data.sql
