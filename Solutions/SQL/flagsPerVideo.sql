select video_id, count(user_id)
from (
    select *, concat(user_firstname,user_lastname)
    as user_id
    from user_flags
    where flag_id is not null
) as test
group by video_id;