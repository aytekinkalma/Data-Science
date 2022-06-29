select * from cust_dimen
select * from market_fact
select * from orders_dimen
select * from prod_dimen
select * from shipping_dimen

UPDATE market_fact
   SET Discount = round(Discount, 2 ),
       Product_Base_Margin = round(Product_Base_Margin, 2 )

UPDATE prod_dimen 
   SET Prod_id = SUBSTRING(Prod_id, PATINDEX('%[0-9]%', Prod_id), LEN(Prod_id)) 

ALTER TABLE prod_dimen
ALTER COLUMN Prod_id int;

UPDATE shipping_dimen 
   SET Ship_id = SUBSTRING(Ship_id, PATINDEX('%[0-9]%', Ship_id), LEN(Ship_id)) 

ALTER TABLE shipping_dimen
ALTER COLUMN Ship_id int;

UPDATE market_fact 
   SET  Ord_id= SUBSTRING(Ord_id, PATINDEX('%[0-9]%', Ord_id), LEN(Ord_id)) 

ALTER TABLE market_fact
ALTER COLUMN Ord_id int;

UPDATE market_fact 
   SET  Prod_id= SUBSTRING(Prod_id, PATINDEX('%[0-9]%', Prod_id), LEN(Prod_id))
   
ALTER TABLE market_fact
ALTER COLUMN Prod_id int;

UPDATE market_fact 
   SET  Ship_id= SUBSTRING(Ship_id, PATINDEX('%[0-9]%', Ship_id), LEN(Ship_id)) 

ALTER TABLE market_fact
ALTER COLUMN Ship_id int;

UPDATE market_fact 
   SET  Cust_id= SUBSTRING(Cust_id, PATINDEX('%[0-9]%', Cust_id), LEN(Cust_id)) 

ALTER TABLE market_fact
ALTER COLUMN Cust_id int;

UPDATE cust_dimen 
   SET  Cust_id= SUBSTRING(Cust_id, PATINDEX('%[0-9]%', Cust_id), LEN(Cust_id)) 

ALTER TABLE Cust_dimen
ALTER COLUMN Cust_id int;

UPDATE orders_dimen 
   SET  Ord_id= SUBSTRING(Ord_id, PATINDEX('%[0-9]%', Ord_id), LEN(Ord_id))

ALTER TABLE cust_dimen

ALTER TABLE market_factALTER COLUMN Ord_id int not null;ALTER TABLE market_factALTER COLUMN Prod_id int not null;ALTER TABLE market_factALTER COLUMN Ship_id int not null;ALTER TABLE market_factALTER COLUMN Cust_id int not null;
ALTER TABLE orders_dimenALTER COLUMN Ord_id int not null;
ALTER TABLE prod_dimenALTER COLUMN Prod_id int not null;
ALTER TABLE shipping_dimenALTER COLUMN Ship_id int not null;ALTER TABLE shipping_dimenALTER COLUMN Ship_Date date not null;


ALTER TABLE cust_dimen ADD CONSTRAINT PK_1 PRIMARY KEY (Cust_id)ALTER TABLE orders_dimen ADD CONSTRAINT PK_2 PRIMARY KEY (Ord_id)ALTER TABLE prod_dimen ADD CONSTRAINT PK_3 PRIMARY KEY (Prod_id)ALTER TABLE shipping_dimen ADD CONSTRAINT PK_4 PRIMARY KEY (Ship_id)

------------------------------------------------
Alter Table market_fact Add Id int Identity(1,1)
ALTER TABLE market_factALTER COLUMN Id int not null;

ALTER TABLE market_fact ADD CONSTRAINT PK_5 PRIMARY KEY (Id)


select * from market_fact


ALTER TABLE market_fact ADD CONSTRAINT FK_22 FOREIGN KEY (Cust_id) REFERENCES cust_dimen (Cust_id)ALTER TABLE market_fact ADD CONSTRAINT FK_11 FOREIGN KEY (Ord_id) REFERENCES orders_dimen (Ord_id)ALTER TABLE market_fact ADD CONSTRAINT FK_3 FOREIGN KEY (Prod_id) REFERENCES prod_dimen (Prod_id)ALTER TABLE market_fact ADD CONSTRAINT FK_4 FOREIGN KEY (Ship_id) REFERENCES shipping_dimen (Ship_id)

--select * from cust_dimen where Customer_Name='ERIC BARRETO'
--select * from cust_dimen where Customer_Name='KARL BROWN'


----------------------------------------------------------------------
--1. Using the columns of “market_fact”, “cust_dimen”, “orders_dimen”, 
--“prod_dimen”, “shipping_dimen”, Create a new table, named as
--“combined_table”.SELECT  A.Id, A.Discount, A.Order_Quantity, A.Product_Base_Margin, A.Sales, B.*, C.*,D.*,E.* INTO combined_df      FROM market_fact A, cust_dimen B, orders_dimen C, prod_dimen D,  shipping_dimen E      WHERE A.Cust_id = B.Cust_id  and A.Ord_id = C.Ord_id 	  and A.Prod_id = D.Prod_id and A.Ship_id = E.Ship_id

select * from combined_df

-----------------------------------------------------------------
--2. Find the top 3 customers who have the maximum count of orders.


select Top 3 Cust_id, COUNT(distinct Ord_id) count_of_orders from combined_dfgroup by Cust_idorder by 2 desc

--3.Create a new column at combined_table as DaysTakenForDelivery that contains the date difference of Order_Date and Ship_Date.
--Use "ALTER TABLE", "UPDATE" etc.

ALTER TABLE combined_df ADD DaysTakenForDelivery INT

UPDATE combined_df 
SET DaysTakenForDelivery = DATEDIFF(DAY, Order_date, Ship_date

select * from combined_df

--ALTER TABLE combined_df 
--ADD 
--  DaysTakenForDelivery AS DATEDIFF (DAY,Order_date,Ship_date) PERSISTED

--4. Find the customer whose order took the maximum time to get delivered

select TOP 1 Cust_id,Customer_Name, Max(DaysTakenForDelivery) Max_delivery_day from combined_dfgroup by Cust_id,Customer_Nameorder by 3 desc


--5. Count the total number of unique customers in January and how many of them came back every month over the entire year in 2011
--You can use such date functions and subqueries
--Ocak ayındaki toplam benzersiz müşteri sayısını ve 2011'de tüm yıl boyunca her ay kaç tanesinin geri geldiğini sayın.
--Ocak ayinda unique olan musterilerin 2011 yilinin her ayinda kacinin alisveris yaptigini bulunuzdrop view v1create view v1 as(select distinct Cust_id,order_datefrom combined_dfWHERE  Cust_id in
(select distinct Cust_idfrom combined_df where MONTH(Order_Date) = 1 group by Cust_id
)
) 
select MONTH(order_date) month_2011, COUNT(DISTINCT cust_id) total_cust
from v1
where Year(Order_Date)='2011'
group by MONTH(order_date) 

select * from v1 

--select distinct Cust_id,count(MONTH(order_date)) a from v1
--where Year(Order_Date)='2011'
--group by Cust_id
--order by a desc 

-----------------------------------------------------------------------
--6--- Write a query to return for each user the time elapsed between the first 
--purchasing and the third purchasing, in ascending order by Customer ID.

CREATE VIEW T1 as (select Cust_id from (select cust_id, count(distinct Order_Date) order_count from combined_dfgroup by cust_idhaving count(distinct Order_Date) >=3) A)CREATE VIEW T3 as (select B.* from T1 A, combined_df Bwhere A.cust_id = B.Cust_id)CREATE VIEW T4 as (select distinct cust_id, order_date, dense_rank() over(partition by cust_id order by order_date) dense_ from T3)CREATE VIEW T5 as (select Cust_id, Order_Date, dense_ from T4where dense_ = 3 or dense_ = 1)select cust_id, DATEDIFF(day, MIN(order_date), MAX(order_date)) diffrence from T5 group by cust_id

------------------------------------
--7. Write a query that returns customers who purchased both product 11 and 
--product 14, as well as the ratio of these products to the total number of 
--products purchased by the customer.


create view p1 as (
select distinct b.Prod_id,A.Cust_id, count(Prod_id) num_of_prod ,b.Order_Quantity num_of_quantity from (select cust_id from combined_dfwhere Prod_id=11INTERSECT select cust_id from combined_dfwhere Prod_id=14) A, combined_df B WHERE A.Cust_id=B.Cust_idgroup by A.Cust_id,b.Prod_id,b.Order_Quantity)


select a.prod_id,a.sum_quantity_prod ,round(cast((1.0*a.sum_quantity_prod) as float) /cast(sum(1.0*p1.num_of_quantity) as float),2)
from (
select Prod_id,sum(num_of_quantity) sum_quantity_prod from p1
where prod_id=11 or prod_id=14
group by Prod_id
) A,p1 where A.prod_id=p1.prod_id
group by a.prod_id,a.sum_quantity_prod

-----------------------------
create view p1 as (select distinct b.Prod_id,A.Cust_id, count(Prod_id) num_of_prod ,b.Order_Quantity num_of_quantity from (select cust_id from combined_dfwhere Prod_id=11INTERSECT select cust_id from combined_dfwhere Prod_id=14) A, combined_df B WHERE A.Cust_id=B.Cust_idgroup by A.Cust_id,b.Prod_id,b.Order_Quantity)CREATE VIEW H1 as(select Prod_id, sum(num_of_quantity) num_of_quantity_11_14 from p1where Prod_id=11 or Prod_id=14group by Prod_id)CREATE VIEW H2 as(select sum(num_of_quantity) num_of_quantity from p1)select h1.Prod_id,cast(1.0*H1.num_of_quantity_11_14/H2.num_of_quantity  as decimal(5,3)) ratio
from H1,H2


---------------------------------------------------------
--Customer Segmentation
--Categorize customers based on their frequency of visits. The following steps 
--will guide you. If you want, you can track your own way.
--1. Create a “view” that keeps visit logs of customers on a monthly basis. (For 
--each log, three field is kept: Cust_id, Year, Month
CREATE VIEW L1 AS(select  MONTH(order_date) [MONTH],YEAR(order_date) [YEAR], cust_id  from combined_df)select * from L1 order by 1-- 2.Create a “view” that keeps the number of monthly visits by users. (Show separately all months from the beginning business)
SELECT Month , COUNT(*) FROM (select Cust_id, L1.MONTH,L1.YEAR from L1) Agroup by MONTHorder by 1

-- 3.For each visit of customers, create the next month of the visit as a separate column-- Müşterilerin her ziyareti için, ziyaretin bir sonraki ayını ayrı bir sütun olarak oluşturunCREATE VIEW L3 as(select distinct Cust_id, Order_Date from combined_df)select cust_id, order_date, LEAD(order_date) over(partition by cust_id order by order_date) next_visit from L3CREATE VIEW L4 as(select * from (select cust_id, order_date, LEAD(order_date) over(partition by cust_id order by order_date) next_visitfrom L3) Awhere A.next_visit is not null)select distinct cust_id , order_date from combined_df order by 1--4.Calculate the monthly time gap between two consecutive visits by each customer.select cust_id, DATEDIFF(MONTH, Order_Date,next_visit) a from L4


--5. Categorise customers using average time gaps. Choose the most fitted
--labeling model for you.
--For example: 
--o Labeled as churn if the customer hasn't made another purchase in the 
--months since they made their first purchase.
--o Labeled as regular if the customer has made a purchase every month.
--Etc.
-- CHURNCREATE VIEW CHURN_ as(select cust_id, COUNT(distinct Order_Date) count_order from combined_dfgroup by cust_idhaving COUNT(distinct Order_Date)=1)select cust_id, order_date from combined_df order by 1-- REGULARCREATE VIEW REGULAR as(select cust_id , avg(DATEDIFF(MONTH, Order_Date,next_visit)) a from L4group by Cust_id)


--labelıng
CREATE VIEW LABELLING as (select Cust_id, case when cust_id=cust_id then 'Churn' end churn_from CHURN_unionselect Cust_id, case when cust_id=cust_id then 'Regular' end churn_from REGULAR
)

select * from LABELLING
/* Month-Wise Retention Rate
Find month-by-month customer retention ratei since the start of the business.
There are many different variations in the calculation of Retention Rate. 
But we will try to calculate the month-wise retention rate in this project.
So, we will be interested in how many of the customers in the previous month could be retained in the next month.
Proceed step by step by creating views. 
You can use the view you got at the end of the Customer Segmentation section as a source. */

-- 1. Find the number of customers retained month-wise. (You can use time gaps)


select count(*) from REGULAR

--2. Calculate the month-wise retention rate.
--Month-Wise Retention Rate = 1.0 * Total Number of Customers in The Previous Month /
--Number of Customers Retained in The Next Month

-- Month-Wise Retention Rate-- 1.Find the number of customers retained month-wise. (You can use time gaps)select COUNT(*) from REGULAR--2.Calculate the month-wise retention rate.-- Month-Wise Retention Rate = 1.0 * Number of Customers Retained in The Current Month / Total Number of Customers in the Current MonthCREATE VIEW COUNT_RETAINED AS(select month_ , count(*) count_retained from(select A.Cust_id, Month(B.Order_Date) month_ from REGULAR A, combined_df B where a.Cust_id = B.Cust_id) Cgroup by month_)CREATE VIEW COUNT_TOTAL AS(select month(order_date) month_, count(*) total_retained from combined_dfgroup by month(order_date))select cast(1.0*A.count_retained/B.total_retained as decimal(5,3)) from COUNT_RETAINED A, COUNT_TOTAL B where A.month_=B.month_















