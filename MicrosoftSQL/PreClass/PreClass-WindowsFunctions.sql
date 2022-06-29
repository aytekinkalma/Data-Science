--Introduction
--In this part, we'll learn a very important and very powerful concept
--in SQL data analysis, the window function.
--They are also known as analytic functions. Let's start with the definition
--of "window function" using some official documents. 

--A window function is an SQL function where the input values are taken from a "window" 
--of one or more rows in the results set of a SELECT statement.

--Window functions are distinguished from other SQL functions by the presence of an OVER clause.
--If a function has an OVER clause, then it is a window function. If it lacks an OVER clause, 
--then it is an ordinary aggregate or scalar function. Window functions might also have a FILTER clause in between the function and the OVER clause.

--A window function performs a calculation across a set of table rows that are somehow related to 
--the current row. This is comparable to the type of calculation that can be done with an aggregate function. 
--But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result.

--To sum up, window functions operate on a set of rows and return a single value for each row from
--the underlying query. This explains "...the rows retain their separate identities." phrase in the definition above. 
--The term "window" describes the set of rows on which the function operates.
--Here is the syntax of the window function:

--window_function (expression) OVER (
--[ PARTITION BY expr_list ]
--[ ORDER BY order_list ] [ frame_clause ])



--When we use a window function, we simply define the window using the OVER() clause. 
--The OVER() clause separates the window functions from other functions in SQL. 
--The OVER() clause can take the following clauses to extend its functionality:
--PARTITION BY clause: Defines window partitions to form groups of rows
--ORDER BY clause: Orders rows within a partition
--ROW or RANGE clause: Defines the scope of the function


--We can group window functions into three categories:
--Aggregate Window Functions
--Ranking Window Functions
--Value Window Functions


--Aggregate Window Functions
--An aggregate window function is similar to a normal aggregate function.
--But the main difference between them is the aggregate window function doesn't change the number of rows returned. 
--Let's rewrite the general syntax of the window function:

--window function (column_name)
--OVER ( [ PARTITION BY expr_list ] [ ORDER BY orders_list frame-clause ] )

--Now, we can breakdown the syntax arguments below:

--Window functions syntax breakdown
--window_function: This is an ordinary aggregate function which may be AVG(), COUNT(), MAX(), MIN(), SUM().
--column_name: The column that the function operates on
--OVER:  Specifies the window clauses for the aggregation functions. The OVER clause distinguishes window
--aggregation functions from ordinary aggregation functions.
--PARTITION BY expr_list : Optional. Defines the window for the window function.
--ORDER BY order_list : Optional. Sorts the rows within each partition.
--frame_clause: If ORDER BY clause is used, frame_clause is required. The frame clause refines the set of rows 
--in a function's window, including or excluding sets od rows within the ordered result.

--Now, let's see the aggregate window function in action.
 
--"departments" table:

--id     name     dept_name          seniority     graduation  salary   hire_date
------ -------- ----------------   --------      ----------  ------   ----------
--10238  Eric     Economics          Experienced   MSc         72000    01-12-2019
--13378  Karl     Music              Candidate     BSc         42000    01-01-2022
--23493  Jason    Philosophy         Candidate     MSc         45000    01-01-2022
--36299  Jane     Computer Science   Senior        PhD         91000    15-05-2018
--30766  Jack     Economics          Experienced   BSc         68000    06-04-2020
--40284  Mary     Psychology         Experienced   MSc         78000    22-10-2019
--43087  Brian    Physics            Senior        PhD         93000    18-08-2017
--53695  Richard  Philosophy         Candidate     PhD         54000    17-12-2021
--58248  Joseph   Political Science  Experienced   BSc         58000    25-09-2021
--63172  David    Art History        Experienced   BSc         65000    11-03-2021
--64378  Elvis    Physics            Senior        MSc         87000    23-11-2018
--96945  John     Computer Science   Experienced   MSc         80000    20-04-2019
--99231  Santosh  Computer Science   Experienced   BSc         74000    07-05-2020

--The following query shows us how to work window functions.   

SELECT graduation, COUNT (id) OVER() as cnt_employee
FROM departments 

--result:
--graduation cnt_employee      
---------- ----------
--MSc        13
--BSc        13
--MSc        13
--PhD        13
--BSc        13
--MSc        13
--PhD        13
--PhD        13
--BSc        13
--BSc        13
--MSc        13
--MSc        13
--BSc        13

--As you see, the whole table records were returned for the graduation column.
--Besides, the count of employees in the whole table was written for per row. 
--The new column created with a window function was added the result without 
--any changes in the main table. Also, there are many duplicate rows.

--💡Tips:
--If you use DISTINCT keyword like the query below, you would be get rid of duplicate rows.

SELECT DISTINCT graduation, COUNT (id) OVER() as cnt_employee
FROM departments 

--graduation cnt_employee      
---------- ----------
--MSc        13
--BSc        13
--PhD        13

--As you noticed, we didn't use any partitioning, ordering, or frame condition for the result.
--The parentheses near the OVER keyword were empty and we got the results above.

--If we use PARTITION BY with DISTINCT keyword like below:

SELECT DISTINCT graduation, COUNT (id) OVER(PARTITION BY graduation) as cnt_employee
FROM departments 

--graduation cnt_employee      
---------- ----------
--BSc        5
--MSc        5
--PhD        3

--As you see above, the query returned the count of employees according to graduation.
--And the result got rid of the duplicate rows with using DISTINCT keyword.

--💡That's the point:
--PARTITION BY specifies partitions on which a window function operates.
--The window function is applied to each partition separately and computation
--restarts for each partition. If we don't include PARTITION BY,
--the window function operates on the whole column.

--What if we use only ORDER BY in the parentheses? Let's try and see it.
SELECT hire_date, COUNT (id) OVER(ORDER BY hire_date) cnt_employee
FROM departments

--hire_date    cnt_employee     
----------   ------------
--2017-08-18   1
--2018-05-15   2
--2018-11-23   3
--2019-04-20   4
--2019-10-22   5
--2019-12-01   6
--2020-05-07   7
--2020-06-04   8
--2021-03-11   9
--2021-09-25   10
--2021-12-17   11
--2022-01-01   13
--2022-01-01   13        

--About the result above, If you don't specify the ordering rule as ASC or DESC,
--ORDER BY accept ASC by default. So, in this example, hire_date column was ordered by ascending.

--☝ Note: You see that when we don't include the ORDER BY we get total when we include ORDER BY we
--get running total/cumulative total. You don't have to use ORDER BY with aggregate window functions.
--But that's important to know what happened when you use ORDER BY with aggregate functions.

--Ranking Window Functions
--In this part, we'll learn ranking window functions. Ranking window functions return a ranking value
--for each row in a partition. Here are the window functions and their description used for ranking purposes.

--Ranking Window Functions
--CUME_DIST	Compute the cumulative distribution of a value in an ordered set of values.
--DENSE_RANK	Compute the rank for a row in an ordered set of rows with no gaps in rank values.
--NTILE	Divide a result set into a number of buckets as evenly as possible and assign a bucket number to each row.
--PERCENT_RANK	Calculate the percent rank of each row in an ordered set of rows.
--RANK	Assign a rank to each row within the partition of the result set.
--ROW_NUMBER	Assign a sequential integer starting from one to each row within the current partition
--.We'll not cover all of them in our course. However, you can easily try them on your own.
--Let me remind you of the general window function syntax.

--window function (column_name)
--OVER ( [ PARTITION BY expr_list ] [ ORDER BY orders_list frame-clause ] )
--Let's rank the employees based on their hire date.

--"departments" table:

--id     name     dept_name          seniority     graduation  salary   hire_date
------ -------- ----------------   --------      ----------  ------   ----------
--10238  Eric     Economics          Experienced   MSc         72000    01-12-2019
--13378  Karl     Music              Candidate     BSc         42000    01-01-2022
--23493  Jason    Philosophy         Candidate     MSc         45000    01-01-2022
--36299  Jane     Computer Science   Senior        PhD         91000    15-05-2018
--30766  Jack     Economics          Experienced   BSc         68000    06-04-2020
--40284  Mary     Psychology         Experienced   MSc         78000    22-10-2019
--43087  Brian    Physics            Senior        PhD         93000    18-08-2017
--53695  Richard  Philosophy         Candidate     PhD         54000    17-12-2021
--58248  Joseph   Political Science  Experienced   BSc         58000    25-09-2021
--63172  David    Art History        Experienced   BSc         65000    11-03-2021
--64378  Elvis    Physics            Senior        MSc         87000    23-11-2018
--96945  John     Computer Science   Experienced   MSc         80000    20-04-2019
--99231  Santosh  Computer Science   Experienced   BSc         74000    07-05-2020


SELECT name,
	   RANK() OVER(ORDER BY hire_date DESC) AS rank_duration
FROM departments;

--name      rank_duration
--------  -------------
--Karl      1
--Jason     1
--Richard   3
--Joseph    4 
--David     5
--Jack      6
--Santos    7
--Eric      8
--Mary      9
--John      10
--Elvis     11
--Jane      12
--Brian     13 

--RANK() function assigns the same rank number if the hire_date value is same. 

--☝ Note: RANK() function assigns the row numbers of the values in the list 
--created by the ordering rule. For the same values assigns their smallest row number.

--Now, let's apply the same scenario by using the DENSE_RANK function.

--query:
SELECT name,DENSE_RANK() OVER(ORDER BY hire_date desc) as rank_duration
from departments;

--Note: DENSE_RANK() returns the sequence numbers of the values in the list
--created by the ordering rule. For the same values assigns their smallest sequential integer.

--Let's continue with another ranking function, ROW_NUMBER().

--ROW_NUMBER() assigns a sequential integer to each row.  The row number starts with 1 for the first row.

--If used with PARTITION BY, ROW_NUMBER() assigns a sequential integer to each row within the partition. 
--The row number starts with 1 for the first row in each partition. 

--Let's give a sequence number to the employees in each seniority category according to their hire dates.

Select name,seniority,hire_date, ROW_NUMBER() OVER(PARTITION BY seniority order by hire_date DESC) AS  row_number
from departments

--name     seniority    hire_date    row_number  
-------- -----------  ----------   ----------
--Karl     Candidate    2022-01-01   1
--Jason    Candidate    2022-01-01   2
--Richard  Candidate    2021-12-17   3
--Joseph   Experienced  2021-09-25   1
--David    Experienced  2021-03-11   2
--Jack     Experienced  2020-06-04   3
--Santosh  Experienced  2020-05-07   4
--Eric     Experienced  2019-12-01   5
--Mary     Experienced  2019-10-22   6
--John     Experienced  2019-04-20   7
--Elvis    Senior       2018-11-23   1
--Jane     Senior       2018-05-15   2
--Brian    Senior       2017-08-18   3


--☝ Note: We must use ORDER BY with ranking window functions.
--Alright, you've got the logic of how a ranking window function works. 
--You can easily apply other ranking window functions on your own.
--Let's continue with the last category of window function: Value Window Functions.

--Value Window Functions
--In this part, we'll learn value window functions as the last category of window functions. 
--They allow you to include values from other rows. Value Window Functions access a previous
--row without having to do a self-join. Some also call these functions 'offset functions'. 
--The following table illustrates value window functions and their descriptions. 

--Function	Description
--FIRST_VALUE	Get the value of the first row in a specified window frame.
--LAG	Provide access to a row at a given physical offset that comes before the current row.
--LAST_VALUE	Get the value of the last row in a specified window frame.
--LEAD	Provide access to a row at a given physical offset that follows the current row.
--We'll not cover all of them in our course. However, you can easily try them on your own.
--Let me remind you of the general window function syntax.

--window function (column_name)
--OVER ( [ PARTITION BY expr_list ] [ ORDER BY orders_list frame-clause ] )
--Let's start with LAG() and LEAD() functions. These functions are useful to compare 
--rows to preceding or following rows. LAG returns data from previous rows and LEAD
--returns data from the following rows.

--The following displays syntax of the LAG and LEAD function in particular.
--LAG(column_name [,offset] [,default])

--offset: Optional. It specifies the number of rows back from the current row
--from which to obtain a value. If not given, the default is 1. In that case,
--it returns the value of the previous value. If there is no previous row
--(the current row is the first), then returns NULL.
--Offset value must be a non-negative integer.

--default: The value to return when the offset is beyond the scope of the partition.
--If a default value is not specified, NULL is returned.

--Let's do an example.

--query:

SELECT id,name,LAG(name) over(order by id ) as previous_name
from departments
--result:
--id      name     previous_name
-----   -------  -------------
--10238   Eric     NULL
--13378   Karl     Eric
--23493   Jason    Karl
--30766   Jack     Jason
--36299   Jane     Jack
--40284   Mary     Jane
--43087   Brian    Mary
--53695   Richard  Brian
--58248   Joseph   Richard
--63172   David    Joseph
--64378   Elvis    David
--96945   John     Elvis
--99231   Santosh  John

--Let's do the same example by using LEAD() function.

SELECT id, name,
		LEAD(name) OVER(ORDER BY id) AS next_name
FROM departments;

--id      name     next_name
-----   -------  ---------
--10238   Eric     Karl
--13378   Karl     Jason
--23493   Jason    Jack
--30766   Jack     Jane
--36299   Jane     Mary
--40284   Mary     Brian
--43087   Brian    Richard
--53695   Richard  Joseph
--58248   Joseph   David
--63172   David    Elvis
--64378   Elvis    John
--96945   John     Santosh
--99231   Santosh  NULL

--If you want to access two rows back from the current row,
--you need to specify the offset argument 2. 
--The following query displays the values two rows back from the current row.
--query:
SELECT id, name,
		LAG(name, 2) OVER(ORDER BY id) AS previous_name
FROM departments;

--id      name     previous_name
-----   -------  -------------
--10238   Eric     NULL
--13378   Karl     NULL
--23493   Jason    Eric
--30766   Jack     Karl
--36299   Jane     Jason
--40284   Mary     Jack
--43087   Brian    Jane
--53695   Richard  Mary
--58248   Joseph   Brian
--63172   David    Richard
--64378   Elvis    Joseph
--96945   John     David
--99231   Santosh  Elvis

--Let's do the examples with FIRST_VALUE() AND LAST_VALUE()
--query:

SELECT id,name,FIRST_VALUE(name) over(order by id) as first_name
from departments

--id      name      the_first_name
-----   -------   -------------- 
--10238   Eric      Eric   
--13378   Karl      Eric
--23493   Jason     Eric
--30766   Jack      Eric
--36299   Jane      Eric
--40284   Mary      Eric
--43087   Brian     Eric
--53695   Richard   Eric
--58248   Joseph    Eric
--63172   David     Eric
--64378   Elvis     Eric
--96945   John      Eric
--99231   Santosh   Eric     

--As you see, for each row, FIRST_VALUE() function returns
--the first value from the whole name column sorted by id.
--✍ Because the default window frame covered all of the rows for each row.

SELECT id, name,
		LAST_VALUE(name) OVER(ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING ) AS last_name
FROM departments;
--id      name      the_last_name
-----   --------  ------------- 
--10238   Eric      Santosh   
--13378   Karl      Santosh
--23493   Jason     Santosh
--30766   Jack      Santosh
--36299   Jane      Santosh
--40284   Mary      Santosh
--43087   Brian     Santosh
--53695   Richard   Santosh
--58248   Joseph    Santosh
--63172   David     Santosh
--64378   Elvis     Santosh
--96945   John      Santosh
--99231   Santosh   Santosh    

--In the example above, for each row, LAST_VALUE() function returns the last value from the whole name column sorted by id.
--✍ We change the window frame. Because the default window frame didn't cover all of the rows for each row.

SELECT id, name,
		LAST_VALUE(name) OVER(ORDER BY id) AS last_name
FROM departments;
--id      name      the_last_name
--10238	Eric	Eric
--13378	Karl	Karl
--23493	Jason	Jason
--30766	Jack	Jack
--36299	Jane	Jane
--40284	Mary	Mary
--43087	Brian	Brian
--53695	Richard	Richard
--58248	Joseph	Joseph
--63172	David	David
--64378	Elvis	Elvis
--96945	John	John
--99231	Santosh	Santosh

--Window Frames
--In this part, we'll learn window frames that is a very important part of window functions.
--By default, a window is set for each row to encompass all the rows from the first to the current row in the partition.
--However, this is the default and can be adjusted using the window frame clause.
--A window function query using the window frame clause would look as follows:


--SELECT {columns},
--{window_func} OVER (PARTITION BY {partition_key} ORDER BY {order_key} {rangeorrows} 
--BETWEEN {frame_start} AND {frame_end})
--FROM {table1};

--Here,
--{columns} are the columns to retrieve from tables for the query, 
--{window_func} is the window function you want to use, 
--{partition_key} is the column or columns you want to partition on (more on this later), 
--{order_key} is the column or columns you want to order by, 
--{rangeorrows} is either the RANGE keyword or the  ROWS keyword, 
--{frame_start} is a keyword indicating where to start the window frame, 
--{frame_end} is a keyword indicating where to end the window frame, and 


--Commonly Used Framing Syntax
--Frame	Meaning
--ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW :
--Start at row 1 of the partition and include rows up to the current row.

--ROWS UNBOUNDED PRECEDING :
--Start at row 1 of the partition and include rows up to the current row.

--ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING:
--Start at the current row and include rows up to the end of the partition.

--ROWS BETWEEN N PRECEDING AND CURRENT ROW:
--Start at a specified number of rows before the current row and include rows up to the current row.

--ROWS BETWEEN CURRENT ROW AND N FOLLOWING:
--Start at the current row and include rows up to a specified number of rows following the current row.

--ROWS BETWEEN N PRECEDING AND N FOLLOWING:
--Start at a specified number of rows before the current row and include a specified number
--of rows following the current row. Yes, the current row is also included!