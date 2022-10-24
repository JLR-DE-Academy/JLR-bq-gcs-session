CREATE VIEW `jlr-dl-cat-training.2022_DE_Training_dm_bikesharing.top_2_region_by_capacity`
AS
SELECT region_id, SUM(capacity) as total_capacity
FROM `jlr-dl-cat-training.2022_DE_Training_raw_bikesharing.stations`
WHERE region_id != ''
GROUP BY region_id
ORDER BY total_capacity desc
LIMIT 2;
