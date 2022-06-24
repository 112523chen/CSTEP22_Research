import numpy
import pandas

df = playbook_events.merge(playbook_users, on=["user_id"])
d = ["ipad air", "iphone 5s", "macbook pro"]
df = df[df.device.isin(d)]
df = df.groupby(["device", "language"])["user_id"].count()
df.sort_values(ascending=False, inplace=True)
df.reset_index()
