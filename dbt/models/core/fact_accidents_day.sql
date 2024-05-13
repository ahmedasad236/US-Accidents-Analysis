with dim_date as (
    select * from {{ref('dim_date')}}
),

accidents as (
    select * from {{ref('stg_accidents')}}
)

select 
    accidents.accident_id,
    accidents.severity,
    dim_date.date_id,
    dim_date.day_of_week_name
    from accidents
    inner join dim_date on accidents.day_of_acc = dim_date.day_of_week_name



