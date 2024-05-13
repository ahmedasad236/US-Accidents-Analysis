select
    {{ dbt_utils.generate_surrogate_key(['start_lat','start_lng']) }} as location_id,
    city,
    state,
    street,
    start_lat,
    start_lng,
    is_crossing,
    is_railway,
    is_traffic_calming
from {{ref('stg_accidents')}}