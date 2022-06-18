select cust_id 
from orders
group by cust_id
having count(*) > 3;