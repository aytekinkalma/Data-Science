--Introduction
--Set operations allow the results of multiple queries to be combined into a single result set. 
--Set operators include UNION, INTERSECT, and EXCEPT.
--The UNION set operator returns the combined results of the two SELECT statements. Essentially,
--It removes duplicates from the results i.e. only one row will be listed for each duplicated result. 
--To counter this behavior, use the UNION ALL set operator which retains the duplicates in the final result.
--INTERSECT lists only records that are common to both the SELECT queries;
--the EXCEPT set operator removes the second query's results from the output if they are also found in the first query's results. INTERSECT and EXCEPT set operations produce unduplicated results.

--☝ Important: 
--Both SELECT statements must contain the same number of columns.
--In the SELECT statements, the corresponding columns must have the same data type.
--Positional ordering must be used to sort the result set. The individual result set
--ordering is not allowed with Set operators. ORDER BY can appear once at the end of the query.
--UNION and INTERSECT operators are commutative, i.e. the order of queries is not important;
--it doesn't change the final result.
--Performance-wise, UNION ALL shows better performance as compared to UNION because resources
--are not wasted in filtering duplicates and sorting the result set.
--Set operators can be the part of subqueries.

--You can Create the "departments" table we'll work on the preclass in SQL Server, 
--using the script below

CREATE TABLE employees_A
(
emp_id BIGINT,
first_name VARCHAR(20),
last_name VARCHAR(20),
salary BIGINT,
job_title VARCHAR (30),
gender VARCHAR(10),
);



INSERT employees_A VALUES
 (17679,  'Robert'    , 'Gilmore'       ,   110000 ,  'Operations Director', 'Male')
,(26650,  'Elvis'    , 'Ritter'        ,   86000 ,  'Sales Manager', 'Male')
,(30840,  'David'   , 'Barrow'        ,   85000 ,  'Data Scientist', 'Male')
,(49714,  'Hugo'    , 'Forester'    ,   55000 ,  'IT Support Specialist', 'Male')
,(51821,  'Linda'    , 'Foster'     ,   95000 ,  'Data Scientist', 'Female')
,(67323,  'Lisa'    , 'Wiener'      ,   75000 ,  'Business Analyst', 'Female')





CREATE TABLE employees_B
(
emp_id BIGINT,
first_name VARCHAR(20),
last_name VARCHAR(20),
salary BIGINT,
job_title VARCHAR (30),
gender VARCHAR(10),
);


INSERT employees_B VALUES
 (49714,  'Hugo'    , 'Forester'       ,   55000 ,  'IT Support Specialist', 'Male')
,(67323,  'Lisa'    , 'Wiener'        ,   75000 ,  'Business Analyst', 'Female')
,(70950,  'Rodney'   , 'Weaver'        ,   87000 ,  'Project Manager', 'Male')
,(71329,  'Gayle'    , 'Meyer'    ,   77000 ,  'HR Manager', 'Female')
,(76589,  'Jason'    , 'Christian'     ,   99000 ,  'Project Manager', 'Male')
,(97927,  'Billie'    , 'Lanning'      ,   67000 ,  'Web Developer', 'Female')


--Union Operator
--In some cases, you may need to combine data from two or more tables into a result set.
--Union clause is used to perform this operation. The tables that you need to combine can
--be tables with similar data in the same database, or in different databases.

--You will use the UNION operator to combine rows from two or more queries into a single result
--set. The basic syntax for the UNION operator is:

--SELECT column1, column2, ...
--  FROM table_A
--UNION
--SELECT column1, column2, ...
--  FROM table_B

--Suppose we have two tables named "employees_A" and "employees_B". We will use UNION operator 
--to combine two employees table into a single table:

--Tables

--"employees_A" table:
--emp_id      first_name  last_name   salary      job_title            gender    
----------  ----------  ----------  ----------  -------------------  ----------
--17679       Robert      Gilmore     110000      Operations Director  Male      
--26650       Elvis       Ritter      86000       Sales Manager        Male      
--30840       David       Barrow      85000       Data Scientist       Male      
--49714       Hugo        Forester    55000       IT Support Speciali  Male      
--51821       Linda       Foster      95000       Data Scientist       Female    
--67323       Lisa        Wiener      75000       Business Analyst     Female

--"employees_B" table:
--emp_id      first_name  last_name   salary      job_title              gender    
----------  ----------  ----------  ----------  ---------------------  ----------
--49714       Hugo        Forester    55000       IT Support Specialist  Male      
--67323       Lisa        Wiener      75000       Business Analyst       Female    
--70950       Rodney      Weaver      87000       Project Manager        Male      
--71329       Gayle       Meyer       77000       HR Manager             Female    
--76589       Jason       Christian   99000       Project Manager        Male      
--97927       Billie      Lanning     67000       Web Developer          Female

SELECT emp_id, first_name, last_name, job_title
  FROM employees_A
UNION
SELECT emp_id, first_name, last_name, job_title
  FROM employees_B;


--output:
--  emp_id      first_name  last_name   job_title          
----------  ----------  ----------  -------------------
--17679       Robert      Gilmore     Operations Director
--26650       Elvis       Ritter      Sales Manager
--30840       David       Barrow      Data Scientist
--49714       Hugo        Forester    IT Support Speciali 
--51821       Linda       Foster      Data Scientist 
--67323       Lisa        Wiener      Business Analyst
--70950       Rodney      Weaver      Project Manager
--71329       Gayle       Meyer       HR Manager             
--76589       Jason       Christian   Project Manager
--97927       Billie      Lanning     Web Developer

--The six rows in the employees_A table and the six rows in the employees_B 
--table are combined using the UNION operator and a ten rows table is obtained.
--However, some records are not repeated in the output table because they are duplicate records.

--Union All Operator
--The UNION ALL clause is used to print all the records including duplicate records when 
--combining the two tables.

--The basic syntax for the UNION ALL operator is:

--SELECT column1, column2, ...
--  FROM table_A
--UNION ALL
--SELECT column1, column2, ...
--  FROM table_B

--After reviewing the following picture, it will be easier to understand UNION ALL operation.

--Suppose we have two tables named "employees_A" and "employees_B". We will use 
--Tables

--"employees_A" table:

--emp_id      first_name  last_name   salary      job_title            gender    
----------  ----------  ----------  ----------  -------------------  ----------
--17679       Robert      Gilmore     110000      Operations Director  Male      
--26650       Elvis       Ritter      86000       Sales Manager        Male      
--30840       David       Barrow      85000       Data Scientist       Male      
--49714       Hugo        Forester    55000       IT Support Speciali  Male      
--51821       Linda       Foster      95000       Data Scientist       Female    
--67323       Lisa        Wiener      75000       Business Analyst     Female

--"employees_B" table:
--emp_id      first_name  last_name   salary      job_title              gender    
----------  ----------  ----------  ----------  ---------------------  ----------
--49714       Hugo        Forester    55000       IT Support Specialist  Male      
--67323       Lisa        Wiener      75000       Business Analyst       Female    
--70950       Rodney      Weaver      87000       Project Manager        Male      
--71329       Gayle       Meyer       77000       HR Manager             Female    
--76589       Jason       Christian   99000       Project Manager        Male      
--97927       Billie      Lanning     67000       Web Developer          Female


--Syntax

--query :

--Here, the Type column is created to indicate which table the employees belong to.

--output:

--Type         emp_id      first_name  last_name   job_title          
-----------  ----------  ----------  ----------  -------------------
--Employees A  17679       Robert      Gilmore     Operations Director
--Employees A  26650       Elvis       Ritter      Sales Manager      
--Employees A  30840       David       Barrow      Data Scientist     
--Employees A  49714       Hugo        Forester    IT Support Speciali
--Employees A  51821       Linda       Foster      Data Scientist     
--Employees A  67323       Lisa        Wiener      Business Analyst   
--Employees B  49714       Hugo        Forester    IT Support Speciali
--Employees B  67323       Lisa        Wiener      Business Analyst   
--Employees B  70950       Rodney      Weaver      Project Manager    
--Employees B  71329       Gayle       Meyer       HR Manager         
--Employees B  76589       Jason       Christian   Project Manager    
--Employees B  97927       Billie      Lanning     Web Developer

--The six rows in the employees_A table and the six rows in the employees_B table are combined
--using the UNION ALL operator and a twelve-rows table is obtained. However, the employee
--records of emp_id 49714 and emp_id 67323 are duplicate records.
--Syntax

--query :
SELECT emp_id, first_name, last_name, job_title
  FROM employees_A
INTERSECT
SELECT emp_id, first_name, last_name, job_title
  FROM employees_B
  ORDER BY emp_id;

--  emp_id      first_name  last_name   job_title            
----------  ----------  ----------  ---------------------
--49714       Hugo        Forester    IT Support Specialist
--67323       Lisa        Wiener      Business Analyst

--As you can see, in the result set, only the information of two employees
--that were common to both tables was returned.

--Except Operator
--EXCEPT operator compares the result sets of the two queries and returns the rows of 
--the previous query that differ from the next query.

--The basic syntax for the EXCEPT operator is:.

--SELECT column1, column2, ...
--  FROM table_A
--EXCEPT
--SELECT column1, column2, ...
--  FROM table_B

--Syntax

--query :
SELECT emp_id, first_name, last_name, job_title
  FROM employees_A
EXCEPT
SELECT emp_id, first_name, last_name, job_title
  FROM employees_B;

--  emp_id      first_name  last_name   job_title          
----------  ----------  ----------  -------------------
--17679       Robert      Gilmore     Operations Director
--26650       Elvis       Ritter      Sales Manager      
--30840       David       Barrow      Data Scientist     
--51821       Linda       Foster      Data Scientist

--As you can see, in the result set, only employees who were in the employees_A 
--table but not the employees_B table were returned



--CASE Expression
--Introduction
--The CASE expression evaluates a list of conditions and returns a value when the first condition
--is met. The CASE expression is similar to the IF-THEN-ELSE statement
--in other programming languages. The  CASE expression is
--SQL's way of handling if/then logic. Every CASE expression must end with the END keyword.

--ELSE part is optional. In case there is no ELSE part and no conditions are true, it returns NULL.
--There are two kinds of CASE expression: 
--Simple CASE expression:
--The simple CASE expression compares an expression to a set of simple expressions to determine
--the result.
--Searched CASE expression:
--The searched CASE expression evaluates a set of Boolean expressions to determine the result.
--CASE can be used in any statement or clause. For example, you can use CASE in statements such
--as SELECT, UPDATE, DELETE and SET, and in clauses such as IN, WHERE, ORDER BY and HAVING.

--Simple CASE Expression
--The simple CASE expression compares an expression to a set of expressions to return the result.
--Here is the simple CASE expression syntax:

--CASE case_expression
--  WHEN when_expression_1 THEN result_expression_1
--  WHEN when_expression_1 THEN result_expression_1
--  ...
--  [ ELSE else_result_expression ]
--END

--The simple CASE expression compares the case_expression to the expressions in the WHEN clauses.
--Then it returns one of the multiple possible result expressions. If no case expression matches
--the when expression, the CASE expression returns the else_result_expression. If no ELSE part
--is included, the CASE expression returns NULL.

--ELSE is optional. This is why it's displayed between the square brackets. 
--The square bracket means "optional". That's to say we don't have to include the ELSE 
--part in our CASE expressions. 

--Let's look at an example. We will classify the departments whether or not they are
--related to the Information Technologies (IT) field. If any department falls into this category,
--label it 'IT', otherwise 'others'.
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

--Now, it's time to write the query:

--query:

SELECT dept_name,
   CASE dept_name
        WHEN 'Computer Science' THEN 'IT'
        ELSE 'others'
    END AS category
FROM departments;

--output:
--dept_name          category  
----------         ----------
--Economics          others    
--Music              others    
--Philosophy         others    
--Computer Science   IT        
--Economics          others    
--Psychology         others    
--Physics            others    
--Philosophy         others    
--Political          others    
--Art Histor         others    
--Physics            others    
--Computer Science   IT        
--Computer Science   IT

--We used the CASE expression in the SELECT statement. As you see that a new column named
--'category' is created. We named it after the END keyword using the AS keyword.

--In the above query, values under the dept_name column are compared with the expression
--('Computer Science') in the WHEN clause. If any matches, then 'IT' result returns.
--Non-matched values return as 'others'. All returned values 'IT' or 'others' are put in 
--a different column specified after END AS. In our case, the newly created column name is 
--'category'. You can give any name you want to the new column created.

--The CASE expression can be used in WHERE, HAVING, ORDER BY, SELECT clauses.

--Searched CASE Expression
--The searched CASE expression evaluates a set of expressions to determine the result. 
--In the simple CASE expression, it's only compared for equivalence whereas the searched 
--CASE expression can include any type of comparison. In this type of CASE statement, 
--we don't specify any expression right after the CASE keyword.

--The searched CASE expression:

--CASE
--  WHEN condition_1 THEN result_1
--  WHEN condition_2 THEN result_2
--  WHEN condition_N THEN result_N
--  [ ELSE result ]
--END

--Let's look at an example. We will classify the salaries of the employees into three 
--categories: High, Middle, Low.
--Here are our criteria:

--When salary < $55,000 THEN 'Low'
--When salary is between $55,000 and $80,000 THEN 'Middle'
--When salary > $80,000 THEN 'High'

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


SELECT name as fist_name, salary,
    CASE
        WHEN salary <= 55000 THEN 'Low'
        WHEN salary > 55000 AND salary < 80000 THEN 'Middle'
        WHEN salary >= 80000 THEN 'High'
    END AS category
FROM departments;

--first_name   Salary    category  
----------   -------   ----------
--Eric         72000     Middle
--Karl         42000     Low
--Jason        45000     Low
--Jane         91000     High
--Jack         68000     Middle
--Mary         78000     Middle
--Brian        93000     High
--Richard      54000     Low
--Joseph       58000     Middle
--David        65000     Middle
--Elvis        87000     High
--John         80000     Middle
--Santosh	   74000     Middle

--An example of the CASE expression in WHERE statement:

SELECT name as fist_name, salary
FROM departments
WHERE 
    CASE
        WHEN salary <= 55000 THEN 'Low'
        WHEN salary > 55000 AND salary < 80000 THEN 'Middle'
        WHEN salary >= 80000 THEN 'High'
    END = 'High'
;

output:
--first_name   Salary    
----------   -------     
--Jane         91000       
--Brian        93000       
--Elvis        87000  

--Using CASE expression with aggregation functions most of the time saves you from long queries.
--Here is another example with CASE Expression:

--query:

SELECT name as fist_name,
       SUM (CASE WHEN seniority = 'Experienced' THEN 1 ELSE 0 END) AS Seniority,
       SUM (CASE WHEN graduation = 'BSc' THEN 1 ELSE 0 END) AS Graduation
FROM departments
GROUP BY name
HAVING SUM (CASE WHEN seniority = 'Experienced' THEN 1 ELSE 0 END) > 0
	     AND
       SUM (CASE WHEN graduation = 'BSc' THEN 1 ELSE 0 END) > 0
  
;

--output:
--first_name   Seniority Graduation  
----------   -------   ----------
--Jack         1         1
--Joseph       1         1
--David        1         1
--Santosh	   1         1

--In the above query, we have listed the experienced employees whose graduation is 
--Bachelor's Degree.

--In this query, the columns that result from filtering using the SUM() function and 
--CASE Expression may not be written in the SELECT statement. We wrote it here because
--we want you to see the result.

--We wanted to filter on the result of an aggregating operation. So, we did this in the
--HAVING statement.