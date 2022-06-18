select weather, hour, 
(count(*)/(select count(*) from lyft_rides)) as 'percentage'
from lyft_rides 
group by weather,hour 
order by weather,hour;