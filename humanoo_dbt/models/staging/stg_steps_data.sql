SELECT
    activity_date,
    user_id,
    steps
FROM {{ source('raw_data', 'steps_data') }}
