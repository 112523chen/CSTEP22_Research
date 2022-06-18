SELECT DISTINCT loans.user_id
FROM loans
JOIN (
    SELECT user_id
    FROM loans
    WHERE type = 'Refinance'
) refinance
    ON loans.user_id = refinance.user_id
JOIN (
    SELECT user_id
    FROM loans
    WHERE type = 'InSchool'
) inschool
     ON loans.user_id = inschool.user_id