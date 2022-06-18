select bike_number,
max(end_time) as latest_use_time
from dc_bikeshare_q1_2012
GROUP BY bike_number
ORDER BY max(end_time);