WITH daily_averages AS (
  SELECT
    activity_date,
    AVG(steps) AS avg_steps_per_day
  FROM {{ ref('stg_steps_data') }}
  GROUP BY activity_date
)
SELECT AVG(avg_steps_per_day) AS overall_daily_average_steps
FROM daily_averages
