select duracion, IFNULL(activity_name, x.bundle_id) from (
SELECT SUM(spent_time) as duracion, bundle_id
FROM launches
WHERE spent_time IS NOT NULL
AND spent_time > 0 
AND bundle_id not in ( select bundle_id from activities where enabled=0)
GROUP BY bundle_id
ORDER BY SUM(spent_time) DESC
LIMIT 10
) x
left join (
select bundle_id, activity_name from activities
) y
on x.bundle_id = y.bundle_id;
