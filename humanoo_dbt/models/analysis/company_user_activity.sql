WITH user_activity AS (
  SELECT
    u.company_name,
    u.user_id,
    CASE WHEN s.user_id IS NOT NULL THEN 1 ELSE 0 END AS has_steps
  FROM {{ ref('stg_users') }} u
  LEFT JOIN (SELECT DISTINCT user_id FROM {{ ref('stg_steps_data') }}) s ON u.user_id = s.user_id
)

SELECT
  company_name,
  COUNT(user_id) AS total_users,
  SUM(has_steps) AS users_with_steps,
  ROUND((SUM(has_steps) * 100.0 / COUNT(user_id)), 2) AS percent_users_with_steps
FROM user_activity
GROUP BY company_name
ORDER BY company_name
