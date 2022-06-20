import numpy
import pandas
fraud_score['state_percentile'] = fraud_score.groupby('state')['fraud_score'].apply(lambda ser: ser.rank(pct=True, ascending=False))
fraud_score[fraud_score.state_percentile <= 0.05]