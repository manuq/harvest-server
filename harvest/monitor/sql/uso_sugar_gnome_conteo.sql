SELECT COUNT(*) AS cantidad_sesiones, is_sugar, sum(100) / total AS porcentaje
FROM sessions
CROSS JOIN
(SELECT COUNT(*) AS total FROM sessions) x
GROUP BY is_sugar;
