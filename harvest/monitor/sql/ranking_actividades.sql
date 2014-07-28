SELECT SUM(spent_time), bundle_id
FROM launches
WHERE spent_time IS NOT NULL
GROUP BY bundle_id
ORDER BY SUM(spent_time) DESC
LIMIT 10;
