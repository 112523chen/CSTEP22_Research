select count(*) as 'total'
from facebook_posts
join facebook_reactions 
on facebook_posts.post_id = facebook_reactions.post_id
and facebook_posts.poster = facebook_reactions.poster
where reaction = "like";