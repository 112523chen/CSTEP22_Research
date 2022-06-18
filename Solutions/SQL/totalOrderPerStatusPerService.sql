select service_name, status_of_order, sum(number_of_orders) as 'number of orders' 
from uber_orders
group by service_name, status_of_order;
