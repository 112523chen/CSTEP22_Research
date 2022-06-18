SELECT s.source_currency, 
f.exchange_rate - s.exchange_rate AS difference
FROM sf_exchange_rate s
JOIN sf_exchange_rate f
    ON s.source_currency = f.source_currency
    AND f.target_currency = f.target_currency
WHERE s.date = '2020-01-01'
AND f.date = '2020-07-01'
AND s.target_currency = 'USD'