SELECT policy_num, state, claim_cost, fraud_score
FROM
(
    SELECT *, NTILE(100) OVER(PARTITION BY state ORDER BY fraud_score DESC) AS percentile
    FROM fraud_score
) AS fraud
WHERE percentile <= 5;