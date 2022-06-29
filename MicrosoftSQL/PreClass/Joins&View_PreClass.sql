--INNER JOIN: Returns the common records in both tables.
--LEFT JOIN: Returns all records from the left table and matching records from the right table.
--RIGHT JOIN: Returns all records from the right table and matching records from the left table.
--FULL OUTER JOIN: Returns all records of both left and right tables.
--CROSS JOIN: Returns the Cartesian product of records in joined tables.
--SELF JOIN: A join of a table to itself.


--INNER JOIN is the most common type of JOINs. It creates a new result table based
--on the values in common columns from two or more tables. INNER JOIN returns a table
--that contains only joined rows that meet the specified join conditions.

--Here is the syntax of the INNER JOIN clause:
--SELECT columns
--  FROM table_A
--  INNER JOIN table_B ON join_conditions

--In this syntax,
--columns: Column names from table_A or table_B.
--table_A, table_B: The names of the joined tables.
--join_conditions: It specifies the conditions to evaluate for each pair of joined rows.
--A join condition generally takes the following form: table_A.column = table_B.column.
--The operator in this statement is usually an equal sign (=),
--but any comparison operator can also be used.
--💡Tips:
--Note the ON keyword for specifying the INNER JOIN condition.
--Multiple join conditions can be written using AND or OR statements.

--In addition, three or more tables can be combined using the INNER JOIN clause.
--The syntax used to join three or more tables is as follows:

--SELECT columns
--  FROM table_A
--  INNER JOIN table_B 
--    ON join_conditions1 AND join_conditions2
--  INNER JOIN table_C
--    ON join_conditions3 OR join_conditions4
--...


--In this JOIN statement, all the records of the left table and the common records
--of the right table are returned in the query. If no matching rows are found in 
--the right table during the JOIN operation, these values are assigned as NULL.
--Here is the syntax of the LEFT JOIN clause:

--SELECT columns
-- FROM table_A
-- LEFT JOIN table_B ON join_conditions

--In this syntax,
--columns: Column names from table_A or table_B.
--table_A, table_B: The names of the joined tables.
--join_conditions: It specifies the conditions to evaluate for each pair of joined rows.
--LEFT JOIN and LEFT OUTER JOIN keywords are exactly the same. OUTER keyword is optional.


--In simple terms, RIGHT JOIN is the opposite of LEFT JOIN.
--In this join statement, all the records of the right table and the common records of the 
--left table are returned in the query. If no matching rows are found in the left table
--during the JOIN operation, these values are assigned as NULL.
--Here is the syntax of the RIGHT JOIN clause:
--SELECT columns
--  FROM table_A
--  RIGHT JOIN table_B ON join_conditions
--In this syntax,
--columns: Column names from table_A or table_B.
--table_A, table_B: The names of the joined tables.
--join_conditions: It specifies the conditions to evaluate for each pair of joined rows.
--RIGHTJOIN and RIGHT OUTER JOIN keywords are exactly the same. OUTER keyword is optional.

--In SQL, the CROSS JOIN is used to combine each row of the first table with each row of the second table. 
--It is also known as the Cartesian join since it returns the Cartesian product of the sets of rows from the joined tables.

--Here is the syntax of the CROSS JOIN clause:
--SELECT columns
--  FROM table_A
--  CROSS JOIN table_B

--In this syntax,
--columns: Column names from table_A or table_B.
--table_A, table_B: The names of the joined tables.
--There is also another implementation of CROSS JOIN.
--Herein, you don't use CROSS JOIN clause. Here is the syntax:
--SELECT columns
--  FROM table_A, table_B

--Example
--Suppose we have two tables named "colors" and "brands".
--These two tables have been created to indicate the colors and brands of the cars to be sold.
--Tables
--"colors" table:
--id  color
--  ----- 
--1   white
--2   black
--3   red
--"brands" table:
--id  brand
---  --------
--1   Mercedes
--2   BMW
--3   Audi

--People wants to buy cars in all combinations of colors and brands. 
--Therefore, we will create a new table by joining these two tables.

--SELECT colors.color, brands.brand
--  FROM colors
--  CROSS JOIN brands;
--color   brand
-----   -----
--white   Mercedes
--white   BMW
--white   Audi
--black   Mercedes
--black   BMW
--black   Audi
--red     Mercedes
--red     BMW
--red     Audi
--There are nine possible cars based on two tables. 
--The three colors multiplied by three brands result in nine possible rows.


--SELF JOIN is a join of a table to itself. Joining a table to itself means
--that each row of the table is combined with itself and the other rows of the table. 
--A SELF JOIN can be defined as a combination of two copies of the same table. 
--This is accomplished with the SQL command, the table is not actually copied a second time.
--We use INNER JOIN or LEFT JOIN for creating a self join.

--You use self-join to create a result set that joins the rows with the other
--rows within the same table. Since you cannot refer to the same table more than one in a query,
--you need to use a table alias to assign the table a different name when you use self-join.

--The self-join compares values of the same or different columns in the same table.
--Only one table is involved in the self-join. You often use self-join to query parents/child
--relationship stored in a table or to obtain running totals.

--Here is the syntax of the SELF JOIN clause:
--SELECT columns
--  FROM table A 
--  JOIN table B 
--  WHERE join_conditions

--A FULL OUTER JOIN returns all rows from both tables. The output table will include rows with NULL data, 
--so nothing is left out. NULL values may be important to detect missing data in tables.
--A FULL OUTER JOIN is likely to generate large data sets based on the number of rows in the tables you want to join.

--Here is the syntax of the FULL OUTER JOIN clause:

--SELECT columns
--  FROM table_A
--  FULL OUTER JOIN table_B ON join_conditions

--In this syntax,
--columns: Column names from tables.
--table_A, table_B: The names of the joined tables.
--join_conditions: It specifies the conditions to evaluate for each pair of joined rows.

--💡Tips:
--All rows are returned from both tables regardless of matching data.
--Unmatched rows are filled with NULLs on either side.

--Full Outer JOIN
T--o do: Go through the activity to the end
--Example
--Suppose you want to join the "employees" table and the "departments" table. In this example, a full outer join has been created that is based on the columns in the two tables:

Tables

--"employees" table:
--emp_id  first_name  last_name  salary  job_title            gender    hire_date 
------  ----------  ---------  ------  -------------------  --------  ----------
--17679   Robert      Gilmore    110000  Operations Director  Male      2018-09-04
--26650   Elvis       Ritter     86000   Sales Manager        Male      2017-11-24
--30840   David       Barrow     85000   Data Scientist       Male      2019-12-02
--49714   Hugo        Forester   55000   IT Support Speciali  Male      2019-11-22
--51821   Linda       Foster     95000   Data Scientist       Female    2019-04-29
--67323   Lisa        Wiener     75000   Business Analyst     Female    2018-08-09
--70950   Rodney      Weaver     87000   Project Manager      Male      2018-12-20
--71329   Gayle       Meyer      77000   HR Manager           Female    2019-06-28
--76589   Jason       Christian  99000   Project Manager      Male      2019-01-21
--97927   Billie      Lanning    67000   Web Developer        Female    2018-06-25

--"departments" table:
--emp_id      dept_name   dept_id   
----------  ----------  ----------
--17679       Operations  13        
--26650       Marketing   14        
--30840       Operations  13        
--49823       Technology  12        
--51821       Operations  13        
--67323       Marketing   14        
--71119       Administra  11        
--76589       Operations  13        
--97927       Technology  12

--SELECT
--    employees.emp_id,
--    employees.first_name,
--    employees.last_name,
--    departments.dept_name
--    departments.dept_id
--  FROM employees
--  FULL OUTER JOIN departments
--    ON employees.emp_id = departments.emp_id;

--output:
--emp_id  first_name   last_name	 dept_name      dept_id
------  ----------   ---------   ---------      -------
--26650   Elvis        Ritter      Marketing      14
--70950   Rodney       Weaver      null           null
--97927   Billie       Lanning     Technology     12
--67323   Lisa         Wiener      Marketing      14
--17679   Robert       Gilmore     Operations     13
--76589   Jason        Christian   Operations     13
--51821   Linda        Foster      Operations     13
--71329   Gayle        Meyer       null           null
--49714   Hugo         Forester    null           null
--30840   David        Barrow      Operations     13
--null    null         null        Technology     12
--null    null         null        Administrative 11


--Views are useful tool for accessing multiple data types. Complex queries can be stored within views.
--In this way, we can invoke the view instead of recreating the queries every time we need them. 

--Sometimes we want some of the information in a table to be hidden to certain users.
--View is a convenient way to that. This important from the security perspective as well. Using view,
--complex structures can be synthesized and presented in an easy format for the end-user.

--Views ensure that only the data needed is used within the scope of a specific project or reporting.

--On the other hand, we can temporarily create views that you will not use later,
--making them visible only in the current database connection. This way, automatically
--removed the temporary view when the database connection is closed. Thus we avoid unnecessary storage costs.

--💡Tip:
--If you are not sure whether a view already exists and you want to run it in a stored procedure or function,
--the CREATE VIEW IF NOT EXISTS view_name syntax will prevent you from getting an error.

--Examples
--Views are read-only in SQL Server. So, you cannot use INSERT, DELETE, and  UPDATE statements to update data in
--the base tables through the view. You can only use CREATE , DROP and  ALTER statements for views.
--To update a view, we should drop the view first, and then create it again.

--You can create a view using the following syntax:
--CREATE VIEW view_name AS
--  SELECT columns
--  FROM tables
--  [WHERE conditions];

--You can drop a view using the following syntax:
--DROP VIEW view_name; 

--Note that; when we execute the drop view command it removes the views. 
--The underlying data stored in the base tables from which this view is derived 
--remains unchanged. A view once dropped can be recreated with the same name.

--Let's create a simple example view with the employee table and then drop it.
--"departments" table:

--id      name       dept_name          seniority     graduation    salary 
------  --------   ----------------   --------      ----------    ------  
--10238   Eric       Economics          Experienced   MSc           72000  
--13378   Karl       Music              Candidate     BSc           42000   
--23493   Jason      Philosophy         Candidate     MSc           45000   
--36299   Jane       Computer Science   Senior        PhD           91000   
--30766   Jack       Economics          Experienced   BSc           68000   
--40284   Mary       Psychology         Experienced   MSc           78000   
--43087   Brian      Physics            Senior        PhD           93000   
--53695   Richard    Philosophy         Candidate     PhD           54000   
--58248   Joseph     Political Science  Experienced   BSc           58000   
--63172   David      Art History        Experienced   BSc           65000   
--64378   Elvis      Physics            Senior        MSc           87000
--96945   John       Computer Science   Experienced   MSc           80000
--99231   Santosh	 Computer Science   Experienced   BSc           74000

--CREATE VIEW sample_dept_view AS
--  SELECT *
--  FROM departments
--  WHERE dept_name LIKE 'P_y%';

--  SELECT *
--  FROM sample_dept_view;

--:output
--id      name       dept_name          seniority     graduation    salary 
------  --------   ----------------   --------      ----------    ------   
--40284   Mary       Psychology         Experienced   MSc           78000   
--43087   Brian      Physics            Senior        PhD           93000    
--64378   Elvis      Physics            Senior        MSc           87000

--DROP VIEW v_managers; 

