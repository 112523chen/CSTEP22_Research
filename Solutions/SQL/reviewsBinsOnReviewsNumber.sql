select price,
(
    CASE
        WHEN number_of_reviews = 0 THEN "No"
        WHEN number_of_reviews between 1 and 6 THEN "Few"
        WHEN number_of_reviews between 6 and 16 THEN "Some"
        WHEN number_of_reviews between 16 and 40 THEN "Many"
        ELSE "A Lot"
    END
) AS reviews_qualification
from airbnb_search_details;