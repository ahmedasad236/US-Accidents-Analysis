select
    accident_id,
    wind_chill,
    wind_speed,
    wind_direction,
    pressure,
    humidity,
    weather_condition,
    temperature
from {{ref('stg_accidents')}}