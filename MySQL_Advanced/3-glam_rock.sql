-- Write a SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT DISTINCT -- Select all the different values from metal bands
  band_name,
  (IFNULL(split, 2020)-formed) AS lifespan
FROM
  metal_bands
WHERE
  style LIKE '%Glam rock%'
ORDER BY
  lifespan DESC;