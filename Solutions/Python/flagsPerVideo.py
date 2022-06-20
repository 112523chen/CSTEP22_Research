import numpy
import pandas
user_flags.dropna(subset=['flag_id'], inplace=True)
user_flags.fillna("", inplace=True)
user_flags['user_id'] = user_flags.user_firstname+user_flags.user_lastname
user_flags = user_flags.groupby(["video_id"])[["user_id"]].count()
user_flags.reset_index()