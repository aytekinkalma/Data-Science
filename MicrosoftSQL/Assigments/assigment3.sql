CREATE TABLE Actions
(
Visitor_ID int,
Adv_Type VARCHAR(20),
Action VARCHAR(20),

);



INSERT Actions VALUES
 (1,  'A'    , 'Left')
,(2,  'A'    , 'Order')
,(3,  'B'    , 'Left')
,(4,  'A'    , 'Order')
,(5,  'A'    , 'Review')
,(6,  'A'    , 'Left')
,(7,  'B'    , 'Left')
,(8,  'B'    , 'Order')
,(9,  'B'    , 'Review')
,(10, 'A'    , 'Review')
;

CREATE VIEW T1 AS 
SELECT Visitor_ID,Adv_Type,
   SUM(CASE WHEN Adv_Type = 'A' THEN 1 ELSE 0 END) AS A, 
   SUM(CASE WHEN Adv_Type = 'B' THEN 1 ELSE 0 END) AS B,
   SUM(CASE WHEN Action = 'Left' THEN 1 ELSE 0 END) AS Left_, 
   SUM(CASE WHEN Action = 'Order' THEN 1 ELSE 0 END) AS Order_,
   SUM(CASE WHEN Action = 'Review' THEN 1 ELSE 0 END) AS Review_
from Actions 
GROUP BY  Visitor_ID,Adv_Type

SELECT DISTINCT Adv_Type,Round(cast(SUM(Order_) as float)/cast(COUNT(Adv_Type) as float),2) AS Conversion_Rate
FROM 
T1
group by Adv_Type


SELECT * FROM T1
SELECT * FROM Actions
DROP VIEW T1 

