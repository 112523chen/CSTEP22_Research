# Import your libraries
import pandas as pd

# Start writing code
sf_exchange_rate_s = sf_exchange_rate[sf_exchange_rate.date == '2020-01-01']
sf_exchange_rate_f = sf_exchange_rate[sf_exchange_rate.date == '2020-07-01']

sf_exchange_rate = sf_exchange_rate_s.merge(sf_exchange_rate_f, on=["source_currency","target_currency"])

sf_exchange_rate["difference"] = sf_exchange_rate["exchange_rate_y"] - sf_exchange_rate["exchange_rate_x"]

sf_exchange_rate[["source_currency","target_currency","difference"]]