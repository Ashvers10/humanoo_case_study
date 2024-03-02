SELECT
    user_id,
    user_name,
    company_id,
    company_name,
    CASE
        WHEN company_size = 'unknown' THEN NULL
        ELSE CAST(company_size AS INTEGER)
    END AS company_size
FROM {{ source('raw_data', 'users') }}
