--HAVING Clause
--Introduction
--HAVING clause is used to filter on the new column that will create as a result of the aggregate 
--operation.
--Its intended use is very similar to WHERE. Both are used for filtering results.
--However, HAVING and WHERE differ from each other in terms of usage and reasons for use.
--WHERE is taken into account at an earlier stage of a query execution, filtering the rows read
--from the tables. Using WHERE, the fields to be grouped over the filtered rows are determined 
--and a new field is created with the aggregate operation. And then HAVING is used if you want 
--to filter the newly created field within the same query. You can create the "departments" table 
--we'll work on the preclass in SQL Server, using the script below.

CREATE TABLE departments
(
id BIGINT,
name VARCHAR(20),
dept_name VARCHAR(20),
seniority VARCHAR(20),
graduation CHAR (3),
salary BIGINT,
hire_date DATE
);



INSERT departments VALUES
 (10238,  'Eric'    , 'Economics'        , 'Experienced'  , 'MSc'      ,   72000 ,  '2019-12-01')
,(13378,  'Karl'    , 'Music'            , 'Candidate'    , 'BSc'      ,   42000 ,  '2022-01-01')
,(23493,  'Jason'   , 'Philosophy'       , 'Candidate'    , 'MSc'      ,   45000 ,  '2022-01-01')
,(36299,  'Jane'    , 'Computer Science' , 'Senior'       , 'PhD'      ,   91000 ,  '2018-05-15')
,(30766,  'Jack'    , 'Economics'        , 'Experienced'  , 'BSc'      ,   68000 ,  '2020-04-06')
,(40284,  'Mary'    , 'Psychology'       , 'Experienced'  , 'MSc'      ,   78000 ,  '2019-10-22')
,(43087,  'Brian'   , 'Physics'          , 'Senior'       , 'PhD'      ,   93000 ,  '2017-08-18')
,(53695,  'Richard' , 'Philosophy'       , 'Candidate'    , 'PhD'      ,   54000 ,  '2021-12-17')
,(58248,  'Joseph'  , 'Political Science', 'Experienced'  , 'BSc'      ,   58000 ,  '2021-09-25')
,(63172,  'David'   , 'Art History'      , 'Experienced'  , 'BSc'      ,   65000 ,  '2021-03-11')
,(64378,  'Elvis'   , 'Physics'          , 'Senior'       , 'MSc'      ,   87000 ,  '2018-11-23')
,(96945,  'John'    , 'Computer Science' , 'Experienced'  , 'MSc'      ,   80000 ,  '2019-04-20')
,(99231,  'Santosh'	,'Computer Science'  ,'Experienced'   ,'BSc'       ,  74000  , '2020-05-07' )
;

--GROUP BY with HAVING
--The GROUP BY clause groups rows into summary rows or groups. The HAVING clause filters groups 
--on a specified condition. You have to use the HAVING clause with the GROUP BY. Otherwise,
--you will get an error. The HAVING clause is applied after the GROUP BY. Also, if you want 
--to sort the output, you should use the ORDER BY clause after the HAVING clause. 

--The syntax is:
--SELECT column_1, aggregate_function(column_2)
--FROM table_name
--GROUP BY column_1
--HAVING search_condition;

--Here is our new database instructors. The database has a table named department.
--Every row contains a single instructor's id, name, department name, and salary info. 
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
--99231  Santosh	Computer Science   Experienced   BSc         74000    07-05-2020

SELECT dept_name, AVG(salary) AS avg_salary
FROM departments
GROUP BY dept_name;

--output:
--dept_name    avg_salary
-----------  ----------
--Art History  65000.0   
--Computer Sc  81666.6
--Economics    70000.0   
--Music        42000.0   
--Philosophy   49500.0   
--Physics      90000.0   
--Political S  58000.0   
--Psychology   78000.0

--We may be interested in only departments where the average salary of the instructors 
--is more than $50,000. We cannot use the WHERE clause here. Because the WHERE clause
--is for non-aggregate data. Since there is aggregated data (average salary of the instructors)
--in the query above, we have to include the HAVING clause.

SELECT dept_name, AVG(salary) AS avg_salary
FROM departments
GROUP BY dept_name
HAVING avg_salary > 50000;

--dept_name    avg_salary
-----------  ----------
--Art History  65000.0   
--Computer Sc  81666.6
--Economics    70000.0   
--Physics      90000.0   
--Political S  58000.0   
--Psychology   78000.0

--Only the average salaries that meet the HAVING criteria (average salary > $50,000)
--are returned. HAVING and WHERE clauses can be in the same query.

--☝ Important: HAVING is for aggregate data and WHERE is for non-aggregate data.
--The WHERE clause operates on the data before the aggregation and the HAVING 
--clause operates on the data after the aggregation.


--GROUPING SETS & PIVOT & ROLLUP & CUBE

--Introduction
--These methods are mostly used in periodical reporting. They ensure that different breakdowns
--of the data are obtained as a result of a single query. Different grouping options are returned 
--in a single query, saving time and resources.
--In addition, it enables decision-makers to evaluate the reported analysis from different directions
--at a single glance.
--Only a piece of brief information has been given here. Details and examples will be covered 
--in in-class lessons.
--GROUPING SETS operator refers to groups of columns grouped in aggregation operations.
--Here is the syntax of the GROUPING SETS clause:

--SELECT
--    column1,
--    column2,
--    aggregate_function (column3)
--FROM
--    table_name
--GROUP BY
--    GROUPING SETS (
--        (column1, column2),
--        (column1),
--        (column2),
--        ()
--);

--PIVOT operator allows the rows in the pivot table to be converted into fields in 
--reporting operations. The aggregation process is repeated for each column included in
--the grouping and a separate field is created.

--Here is the syntax of the PIVOT clause:

--SELECT [column_name], [pivot_value1], [pivot_value2], ...[pivot_value_n]
--FROM 
--table_name
--PIVOT 
--(
-- aggregate_function(aggregate_column)
-- FOR pivot_column
-- IN ([pivot_value1], [pivot_value2], ... [pivot_value_n])
--) AS pivot_table_name;

--ROLLUP operator creates a group for each combination of column expressions. 
--It makes grouping combinations by subtracting one at a time from the column names written 
--in parentheses, in the order from right to left. Therefore, the order in which the columns
--are written is important.

--Here is the syntax of the ROLLUP clause:

--SELECT
--    d1,
--    d2,
--    d3,
--   aggregate_function(c4)
--FROM
--    table_name
--GROUP BY
--    ROLLUP (d1, d2, d3);

--Groups for ROLLUP:

--d1, d2, d3
--d1, d2, NULL
--d1, NULL, NULL
--NULL, NULL, NULL
--CUBE operator makes all possible grouping combinations for all fields specified in
--the select operator. The order in which the columns are written is not important.

--Here is the syntax of the CUBE clause:

--SELECT
--   d1,
--    d2,
--    d3,
--    aggregate_function (c4)
--FROM
--    table_name
--GROUP BY
--    CUBE (d1, d2, d3);


--Groups for CUBE:

--d1, d2, d3
--d1, d2, NULL
--d1, d3, NULL
--d2, d3, NULL
--d1, NULL, NULL
--d2, NULL, NULL
--d3, NULL, NULL
--NULL, NULL, NULL

--Grouping Sets Example
--Here is the syntax of the GROUPING SETS clause:

--SELECT
--   column1,
--    column2,
--    aggregate_function (column3)
--FROM
--    table_name
--GROUP BY
--    GROUPING SETS (
--       (column1, column2),
--        (column1),
--       (column2),
--        ()
--);

--"departments" table:

--id     name     dept_name          seniority     graduation  salary   hire_date
-------- -------- ----------------   --------      ----------  ------   ----------
--10238  Eric     Economics          Experienced   MSc         72000    01-12-2019
--13378  Karl     Music              Candidate     BSc         42000    01-01-2022
--36299  Jane     Computer Science   Senior        PhD         91000    15-05-2018
--30766  Jack     Economics          Experienced   BSc         68000    06-04-2020
--40284  Mary     Psychology         Experienced   MSc         78000    22-10-2019
--43087  Brian    Physics            Senior        PhD         93000    18-08-2017
--53695  Richard  Philosophy         Candidate     PhD         54000    17-12-2021
--58248  Joseph   Political Science  Experienced   BSc         58000    25-09-2021
--63172  David    Art History        Experienced   BSc         65000    11-03-2021
--64378  Elvis    Physics            Senior        MSc         87000    23-11-2018
--96945  John     Computer Science   Experienced   MSc         80000    20-04-2019
--99231  Santosh	Computer Science   Experienced   BSc         74000    07-05-2020

SELECT
    seniority,
    graduation,
    AVG(Salary) AS Salary
FROM
    departments
GROUP BY
    GROUPING SETS (
        (seniority, graduation),
        (graduation)
);

 --seniority     graduation    salary 
 --------      ----------    ------   
 --Candidate     BSc           42000.0   
 --Candidate     MSc           45000.0   
 --Candidate     PhD           54000.0   
 -- Experienced   BSc           66250.0   
 --Experienced   MSc           76666.0
 --Senior        MSc           87000.0
 --Senior        PhD           92000.0
 --Null          BSc           61400.0
 --Null          MSc           72400.0
 --Null          PhD           79333.0

 --In the query above, two fields were used for aggregation. The average salary was 
 --calculated according to both seniority and graduation, at the same time only graduation.
 --As you see, two different grouping models were applied using GROUPING SETS.

 
--Pivot Example
--Here is the syntax of the PIVOT clause:
--SELECT [column_name], [pivot_value1], [pivot_value2], ...[pivot_value_n]
--FROM 
--table_name
--PIVOT 
--(
--aggregate_function(aggregate_column)
-- FOR pivot_column
-- IN ([pivot_value1], [pivot_value2], ... [pivot_value_n])
--) AS pivot_table_name;

--"departments" table:

--id     name     dept_name          seniority     graduation  salary   hire_date
-------- -------- ----------------   --------      ----------  ------   ----------
--10238  Eric     Economics          Experienced   MSc         72000    01-12-2019
--13378  Karl     Music              Candidate     BSc         42000    01-01-2022
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

SELECT [seniority], [BSc], [MSc], [PhD]
FROM 
(
SELECT seniority, graduation, salary
FROM   departments
) AS SourceTable
PIVOT 
(
 avg(salary)
 FOR graduation
 IN ([BSc], [MSc], [PhD])
) AS pivot_table;
--output:
 --seniority     BSc       MSc       PhD
 --------      --------  ------    ------
 --Candidate     42000.0   45000.0   54000.0
 --Experienced   66250.0   76666.0   Null
 --Senior        Null      87000.0   92000.0

--Rollup Example
--Here is the syntax of the ROLLUP clause:

--SELECT
--    d1,
--    d2,
--    d3,
--    aggregate_function(c4)
--FROM
--    table_name
--GROUP BY
--    ROLLUP (d1, d2, d3);

--"departments" table:
--id     name     dept_name          seniority     graduation  salary   hire_date
-------- -------- ----------------   --------      ----------  ------   ----------
--10238  Eric     Economics          Experienced   MSc         72000    01-12-2019
--13378  Karl     Music              Candidate     BSc         42000    01-01-2022
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
SELECT
    seniority,
    graduation,
    AVG(Salary) As Salary 
FROM
    departments
GROUP BY
    ROLLUP (seniority, graduation);

--As you see above, there was applied three different grouping models using ROLLUP.
--One of them was applied according to both seniority and graduation. 
--The second one was applied according to only seniority. The last one was applied with no group.

--Cube Example
--Here is the syntax of the CUBE clause:

--SELECT
--    d1,
--    d2,
--    d3,
--    aggregate_function(c4)
--FROM
--    table_name
--GROUP BY
--   CUBE (d1, d2, d3);

--"departments" table:

--"departments" table:
--id     name     dept_name          seniority     graduation  salary   hire_date
-------- -------- ----------------   --------      ----------  ------   ----------
--10238  Eric     Economics          Experienced   MSc         72000    01-12-2019
--13378  Karl     Music              Candidate     BSc         42000    01-01-2022
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

SELECT
    seniority,
    graduation,
    AVG(Salary) As salary
FROM
    departments
GROUP BY
    CUBE (seniority, graduation);

 --seniority     graduation    salary 
 --------      ----------    ------   
 --Candidate     BSc           42000.0   
 --Candidate     MSc           45000.0   
 --Candidate     PhD           54000.0
 --Experienced   BSc           66250.0   
 --Experienced   MSc           76666.0
 --Senior        MSc           87000.0
 --Senior        PhD           92000.0
 --Candidate     Null          47000.0
 --Experienced   Null          70714.0
 --Senior        Null          90333.0
 --Null          BSc           61400.0
 --Null          MSc           72400.0
 --Null          PhD           79333.3
 --Null          Null          74230.0

 --As you see above, there was applied four different grouping models using CUBE.
 --One of them was applied according to both seniority and graduation. 
 --The second one was applied according to only seniority. The third one was applied according 
 --to only graduation.The last one was applied with no group.

--For better understanding, you should compare the results that you got using CUBE and ROLLUP.