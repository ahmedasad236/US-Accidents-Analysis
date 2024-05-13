with 

source as (

    select * from {{ source('staging', 'accidents') }}

),

accidents_info as (
    select 
    -- identifier
    cast(ID as STRING) as accident_id,
    
    -- timestamp
    cast(Start_Time as DATE) as start_time,
    
    -- accident info
    cast(Severity as INTEGER) as severity,
    cast(Start_Lat as FLOAT64) as start_lat,
    cast(Start_Lng as FLOAT64) as start_lng,
    cast(Temperature as FLOAT64) as temperature,
    cast(Wind_Chill as FLOAT64) as wind_chill,
    cast(Humidity as FLOAT64) as humidity,
    cast(Pressure as FLOAT64) as pressure,
    cast(Wind_Speed as FLOAT64) as wind_speed,
    cast(City as STRING) as city,
    cast(Day_Of_Acc as STRING) as day_of_acc,
    cast(Month_Of_Acc as STRING) as month_of_acc,
    cast(State as STRING) as state,
    cast(Street as STRING) as street,
    cast(Wind_Direction as STRING) as wind_direction,
    cast(Weather_Condition as STRING) as weather_condition,
    cast(Sunrise_Sunset as STRING) as sunrise_sunset,
    cast(Crossing as BOOLEAN) as is_crossing,
    cast(Railway as BOOLEAN) as is_railway,
    cast(Traffic_Calming as BOOLEAN) as is_traffic_calming,
    from source
)

select * from accidents_info