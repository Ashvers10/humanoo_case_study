-- Top 10 users
WITH ranked_users AS (
  SELECT
    u.user_name,
    s.steps,
    ROW_NUMBER() OVER (PARTITION BY s.user_id ORDER BY s.steps DESC) AS rank
  FROM {{ ref('stg_users') }} u
  JOIN {{ ref('stg_steps_data') }} s ON u.user_id = s.user_id
)

(SELECT
  'Top 10' AS category,
  user_name,
  steps
FROM ranked_users
WHERE rank = 1
ORDER BY steps DESC
LIMIT 10)

UNION ALL

-- Bottom 10 users
(SELECT
  'Bottom 10' AS category,
  user_name,
  steps
FROM ranked_users
WHERE rank = 1 AND steps > 0  -- Assuming to consider only active days
ORDER BY steps ASC
LIMIT 10)
