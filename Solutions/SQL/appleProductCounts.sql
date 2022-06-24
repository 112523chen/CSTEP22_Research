select device,language, count(*) as 'total'
from playbook_events
join playbook_users
on playbook_events.user_id = playbook_users.user_id
where device = 'ipad air'
or device = 'iphone 5s'
or device = 'macbook pro'
group by 1,2
order by 3 desc;