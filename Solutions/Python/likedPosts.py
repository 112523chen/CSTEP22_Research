import numpy
import pandas
df = facebook_posts.merge(facebook_reactions, on=["post_id", "poster"])
total = len(df[df.reaction == 'like'])
total