--You can use the GETDATE() function to determine the current date and time of the 
--computer running the current SQL instance. This function doesn't include the time 
--zone difference, just returns datetime format.
--Let's see a GETDATE() function example.

SELECT GETDATE() AS now;
--output :
--now
-----------------------
--2021-11-13 10:38:23.363

--The DATENAME() function returns the name or value of a specific 
--part of the date in nvarchar format.

--Let's see a DATENAME() function example
SELECT DATENAME(WEEKDAY, '2021-11-11') AS sample;
--sample
--------
--Thursday


--💡Tips: There ara fourty datepart tips in SQL Server you can use.
--Such as: DAY, HOUR, MINUTE, WEEKDAY, YEAR, DAYOFYEAR, MONTH, 
--etc.

SELECT DATEPART(MINUTE, GETDATE()) AS sample;

--The DAY() function returns the day of the date in integer format.
--Let's see a DAY() function example.

SELECT DAY('2021-11-19') AS sample;

--sample
------
--19

--The MONTH() function returns the month of the date in integer format.
--Let's see a MONTH() function example.

SELECT MONTH('2021-11-19') AS sample;
--sample
------
--11
--The YEAR() function returns the year of the date in integer format.
--Let's see a YEAR() function example.
SELECT YEAR('2021-11-19') AS sample;
--sample
------
--2021


--DATEDIFF(datepart, startdate, enddate)
--The DATEDIFF() function returns the difference between two dates in integer format.
--In the syntax, datepart is the parameter that specifies which part of the date you want to use to calculate difference. The datepart can be year, month, week, day, hour, minute, second, or milisecond. You then specify the start date in the startdate parameter and the end date in the enddate parameter for which you want to find the difference.
--Let's see a DATEDIFF() function example.

SELECT DATEDIFF(week, '2021-01-01', '2021-02-12') AS DateDifference

--DateDifference
--------------
--6

--DATEADD(datepart, number, date)
--The DATEADD() function enables you to add an interval to part of a specific date.
--Let's see a DATEADD() function example.

SELECT DATEADD (SECOND, 1, '2021-12-31 23:59:59') AS NewDate

--NewDate   
-----------------------
--2022-01-01 00:00:00.000


--EOMONTH(startdate [, month to add])
--The EOMONTH() function returns the last day of the month containing a specified date, with an optional offset.
--Let's see a EOMONTH() function example.

SELECT EOMONTH('2021-02-10') AS EndofFeb

--EndofFeb   
----------
--2021-02-28


--ISDATE(expression)
--The ISDATE() returns 1 if the expression is a valid datetime value; otherwise, 0.
--If your system language is us_english, the date format is "mdy" (month, day, year) by default. The ISDATE() function checks the expression according to this format.
--If you need, you can change the date format as below:
SET DATEFORMAT DMY
--Let's see a ISDATE() function example. (dateformat = mdy)

SELECT ISDATE('2021-02-10') AS isdate_
--isdate_   
-------
--1

--Let's see another ISDATE() function example.
SELECT ISDATE('15/2008/04') AS isdate_

--isdate_   
-------
--0


--Introduction
--In this part, we'll learn other types of SQL Server built-in functions called
--string functions. These functions are listed as below:

--LEN(input string)
--CHARINDEX(substring, string [, start location])
--PATINDEX('%PATTERN%', input string)
--LEFT(input string, number of characters)
--RIGHT(input string, number of characters)
--SUBSTRING(input string, start, length)
--LOWER(input string)
--UPPER(input string)
--STRING_SPLIT(input string, seperator)
--TRIM([removed characters, from] input string)
--LTRIM(input string, seperator)
--RTRIM(input string, seperator)
--REPLACE(input string, seperator)
--STR(input string, seperator)
--String functions are used to manipulate string values.
--They are useful for data cleaning operations in data analysis.


--LEN()
--The LEN() function returns the number of characters of a string 
--(excluding spaces end of the text). The return type of the result is an integer.
--Here is an example of the LEN() function:

SELECT LEN('this is an example') AS sample

--sample
------
--18

--If string is NULL value, the length function returns NULL. 
--If the value specified inside the function is numeric, the LEN() 
--function returns the length of a string representation of the value.
--That means the numeric value is converted into a string and then the number of 
--characters of it is calculated. Such as:

SELECT LEN(NULL) AS col1, LEN(10) AS col2, LEN(10.5) AS col3

--col1   col2  col3
----   ----  ----
--NULL   2     4

--CHARINDEX(substring, string [, start location])
--CHARINDEX() function takes a string and a substring of it as arguments 
--and returns an integer that indicates the position of the substring,
--which is the first character of the substring. CHARINDEX() function finds 
--the first occurrence of substring and returns a value of integer type.

SELECT CHARINDEX('yourself', 'Reinvent yourself') AS start_position;
--start_position
--------------
--10

--CHARINDEX() function works case-sensitively. The following query 
--returns the index number of the first occurrence of 
--the substring 'r' not 'R'.

SELECT CHARINDEX('r', 'Reinvent yourself') AS motto;
--motto
-----
--1

--The following query finds the first occurrence of the substring 'self' 
--and returns its first character's index number. As your see that there are two 'self's.
--CHARINDEX() function only finds the first occurrence which is the 'self' inside the 
--'yourself'.

SELECT CHARINDEX('self', 'Reinvent yourself and ourself') AS motto;

--motto     
----------
--14

--But the following query find second 'self' 
--by using the optional parameter [start location]

SELECT CHARINDEX('self', 'Reinvent yourself and ourself', 15) AS motto;
--motto     
----------
--26

--PATINDEX(%pattern%, input string)

--The PATINDEX() function returns the starting position of the first occurrence
--of a pattern in a specified expression, or zeros if the pattern
--is not found, on all valid text and character data types.

--PATINDEX() function takes two arguments:
--pattern:  Is a character expression that contains the sequence to be found.
--The % character must come before and follow pattern
--(except when you search for first or last characters).
--input string:  Is a character string data that is searched for the specified pattern

--Tips:
--If either pattern or expression is NULL, PATINDEX() returns NULL.
--The starting position for PATINDEX() is 1.
--PATINDEX works just like LIKE, so you can use any of the wildcards. 
--You do not have to enclose the pattern between percents. Unlike LIKE,
--PATINDEX() returns a position, similar to what CHARINDEX() does..

SELECT PATINDEX('%ern%', 'this is not a pattern') AS sample
--sample
------
--19

--If we don't use the % character end of the pattern:

SELECT PATINDEX('%ern', 'this is not a pattern') AS sample
--sample
------
--19

SELECT SUBSTRING('clarusway.com', LEN('clarusway.com')-1, LEN('clarusway.com'));
--output:om
--UPPER(), LOWER(), STRING_SPLIT() Functions
--UPPER() function returns a copy of a string in which all 
--lower-case ASCII characters converted to upper-case equivalent. 
--LOWER() function returns a copy of a string in which all
--upper-case ASCII characters converted to lower-case equivalent. 
--UPPER() and LOWER() functions return null values if you pass a null value. 
--If you pass numeric values to UPPER() or LOWER(), both of them will return
--the exact numeric value.
--Now, it's time to do some examples.
SELECT UPPER('clarusway') AS col;
--col
---------
--CLARUSWAY
SELECT LOWER('CLARUSWAY') AS col;
--col
---------
--clarusway

--STRING_SPLIT(string, seperator)
--The STRING_SPLIT() function is a table-valued function that splits a string 
--into rows of substrings, based on a specified separator character.

--STRING_SPLIT() function takes three arguments:
--string: Is an expression of any character type 
--(for example, nvarchar, varchar, nchar, or char).
--seperator:  Is a single character expression of any character type 
--(for example, nvarchar(1), varchar(1), nchar(1), or char(1)) that is used as
--separator for concatenated substrings.
SELECT value from string_split('John,is,a,very,tall,boy.', ',')
--value
---------
--John
--is
--a
--very
--tall
--boy.


--SUBSTRING(), LEFT(), RIGHT() Functions
--SUBSTRING() function enables you to extract a substring from a string.
--The return value is text.
--Here is the syntax of the SUBSTRING() function:
--SUBSTRING(string, start_postion, [length])

--SUBSTRING() function takes three arguments
--string: The source string
--start_position: The position for extraction. If the start_position is a positive integer,
--the  SUBSTRING() function returns a substring starting from the beginning of the string.
--The first character has an index of 1.  If the start_position is a negative integer, 
--the returned substring consists of the length number of character starting from the 
--end of the string. The last character has an index of -1.
--length:  Optional. It's the number of characters to extract. 
--If it is omitted then SUBSTRING() returns all remaining characters from 
--the starting_postion. 

--If any argument is NULL, the SUBSTRING() function will return NULL.

--Let's see SUBSTRING() function in an example.

--The following query takes the string "Clarusway" starting at position 1,
--which is character "C" and extracts 3 characters that are 'Cla'.
SELECT SUBSTRING('Clarusway', 1, 3) AS substr
--substr
------
--Cla

--The following query starts from position -5 to extract the first character.
SELECT SUBSTRING('Clarusway', -5,7) AS substr
--substr
------
--C

--The following query starts from position -6  and extracts 2 characters.
 --query :
SELECT SUBSTRING('Clarusway', -6, 2) AS substr
--substr
------

--LEFT(string, number of characters)

--Returns the left part of a character string with the specified 
--number of characters.

--LEFT() function takes three arguments
--string: The source string. Can be a constant, variable, or column.
--number of characters:  Is a positive integer that specifies how many
--characters will be returned.
SELECT LEFT('Clarusway', 2) AS leftchars

--leftchars
---------
--Cl

--RIGHT(string, number of characters)

--Returns the right part of a character string with the 
--specified number of characters.

--RIGHT() function takes three arguments
--string: The source string. Can be a constant, variable, or column.
--number of characters:  Is a positive integer that specifies how many 
--characters will be returned.
SELECT RIGHT('Clarusway', 2) AS rightchars
--rightchars
----------
--ay

SELECT UPPER (SUBSTRING('clarusway.com', 0 , CHARINDEX('.','clarusway.com')));

--TRIM(), LTRIM(), RTRIM() Functions
--TRIM() function removes specified characters from both ends of the string. 
--Here is the syntax of the TRIM() function:
--TRIM([characters FROM] string)

--TRIM() function takes two arguments:
--string: The source string
--[characters FROM]:  Optional. Any and all characters that appear 
--in this argument will be removed from the both ends of the string.
--If this argument is omitted, TRIM() function removes spaces from both ends
--of the string.

--TRIM() function returns a new string with the specified leading and 
--trailing characters removed. It does not change the original string.
--Let's do some examples.
SELECT TRIM('  Reinvent Yourself  ') AS new_string;
--new_string
-----------------
--Reinvent Yourself
SELECT TRIM('@' FROM '@@@clarusway@@@@') AS new_string;
--new_string
----------
--clarusway
SELECT TRIM('ca' FROM 'cadillac') AS new_string;
--new_string
----------
--dill

--LTRIM(string)
--Returns a character expression after it removes leading blanks.
--LTRIM() function takes an arguments:
--string: The source string.
SELECT LTRIM('   cadillac') AS new_string;
--new_string
----------
--cadillac

--RTRIM(string)

--Returns a character string after truncating all trailing spaces.

--RTRIM() function takes an arguments:
--string: The source string.
SELECT RTRIM('   cadillac   ') AS new_string;
--new_string
-----------
--   cadillac


--REPLACE() and STR() Functions
--The REPLACE() function allows you to replace all occurrences of
--a specified string with another string. Here is the syntax:

--REPLACE(string expression, string pattern, string replacement)

--REPLACE() function takes three arguments:
--string expression:  The string that you want to perform the replacement.
--string pattern:  The substring to be found in the original string
--string replacement:  The replacement string

SELECT REPLACE('REIMVEMT','M','N');
--REINVENT
SELECT REPLACE('I do it my way.','do','did') AS song_name;
--song_name       
----------------
--I did it my way.

--STR(float expression [, length [, decimal]])
--Returns character data converted from numeric data. The character data is right-justified, with a specified length and decimal precision.
--STR() function takes three argument

--float expression:  Is an expression of approximate numeric (float) 
--data type with a decimal point.
--length:  (Optional) Is the total length. This includes decimal point,
--sign, digits, and spaces. The default is 10.
--decimal:  (Optional) Is the number of places to the right of the decimal point.
--decimal must be less than or equal to 16.

SELECT STR(123.45, 6, 1) AS num_to_str;
--num_to_str
----------------
-- 123.5

--When the expression exceeds the specified length, the string returns ** 
--for the specified length.
SELECT STR(123.45, 2, 2) AS num_to_str;
--num_to_str
----------
--**

SELECT STR(FLOOR (123.45), 20, 3) AS num_to_str;
--num_to_str
----------
--       123.000

--"+" Operator or CONCAT() Function for Concatenating
--The SQL standard provides the CONCAT() function to concatenate two strings 
--into a single string. Besides, the concatenate operator (+) is used to join
--two strings into one as well. It's also possible to join more than two strings 
--using  (+) operator multiple times.

--Here is the syntax of the concatenation operator:
--string1 + string2

SELECT 'Reinvent' + ' yourself' AS concat_string;

--concat_string
-----------------
--Reinvent yourself

SELECT CONCAT('Reinvent' , ' yourself') AS concat_string;

--concat_string
-----------------
--Reinvent yourself

SELECT 'Way' + ' to ' + 'Reinvent ' + 'Yourself' AS motto;

--motto                   
-------------------------
--Way to Reinvent Yourself
SELECT CONCAT ('Robert' , ' ', 'Gilmore') AS full_name 

--full_name     
--------------
--Robert Gilmore


SELECT REPLACE (TRIM(' Reinvent $Yourself! '), '$', '')

--Introduction
--In this part, we'll learn some useful built-in functions and expressions 
--related to our curriculum. These functions are listed as below:

--Functions:
--CAST(expression AS target_type [length])
--CONVERT(target_type [(length)], expression [, style])
--ROUND(numeric expression, length [, function])
--ISNUMERIC(expression)
--Expressions:
--COALESCE(expression [, ...n])
--NULLIF(expression, expression)

--CAST() and CONVERT() Functions
--These functions convert an expression of one data type to another.

-- CAST Syntax:  
--CAST ( expression AS data_type [ ( length ) ] )  
  
-- CONVERT Syntax:  
--CONVERT ( data_type [ ( length ) ] , expression [ , style ] )

--expression:  Any valid expression
--data_type:  The target data type.
--length: An optional integer that specifies the length of the target data type,
--for data types that allow a user specified length. The default value is 30.
--style: An optional integer expression that specifies how the 
--CONVERT function will translate expression. For a style value of NULL,
--NULL is returned..

SELECT 'customer' + '_' + CAST(1 AS VARCHAR(1)) AS col
--col
----------
--customer_1
SELECT CAST(4599.999999 AS numeric(5,1)) AS col
--col
------
--4600.0
SELECT GETDATE() AS current_time1, CONVERT(DATE, GETDATE()) AS current_date1
--current_time              current_date
-----------------------   ------------
--2021-11-22 22:14:27.650   2021-11-22
SELECT GETDATE() AS current_time1, CONVERT(NVARCHAR, GETDATE(), 11)AS current_date1
--current_time              current_date
-----------------------   ------------
--2021-11-22 22:14:27.650   21/11/22


--ROUND() and ISNULL() Function
--ROUND(numeric_expression , length [ ,function ])

--Returns a numeric value, rounded to the specified length or precision.

--ROUND() function takes three arguments:
--numeric_expression: Is an expression of the exact numeric or approximate
--numeric data type category, except for the bit data type.
--length: Is the precision to which numeric_expression is to be rounded. 
--length must be an expression of type tinyint, smallint, or int. 
--When length is a positive number, numeric_expression is rounded to the number 
--of decimal positions specified by length. When length is a negative number, 
--numeric_expression is rounded on the left side of the decimal point, as specified
--by length.
--function: Is the type of operation to perform. function must be tinyint, smallint,
--or int. When function is omitted or has a value of 0 (default), 
--numeric_expression is rounded. When a value other than 0 is specified,
--numeric_expression is truncated.

SELECT ROUND(565.49, -1) AS col;
--col
------
--570.00
SELECT ROUND(565.49, -2) AS col;
--col
------
--600.00
SELECT ROUND(123.9994, 3) AS col1, ROUND(123.9995, 3) AS col2;
--col1      col2
--------  --------
--123.9990  124.0000

SELECT ROUND(123.4545, 2) col1, ROUND(123.45, -2) AS col2;
--col1      col2
--------  ------
--123.4500  100.00
SELECT ROUND(150.75, 0) AS col1, ROUND(150.75, 0, 1) AS col2;
--col1      col2
------  ------
--151.00  150.00

--ISNULL(check expression, replacement value)
--Replaces NULL with the specified replacement value.

--check expression: Is the expression to be checked for NULL.
--check expression can be of any type.
--replacement value: Is the expression to be returned if check expression is NULL.
--replacement value must be of a type that is implicitly convertible to the 
--type of check expression.
SELECT ISNULL(NULL, 'Not null yet.') AS col;
--col
-------------
--Not null yet.
SELECT ISNULL(1, 2) AS col;
--col
---
--1

--COALESCE, NULLIF and ISNUMERIC Expressions
--COALESCE(expression [, ...n])
--Evaluates the arguments in order and returns the current value of the 
--first expression that initially doesn't evaluate to NULL. For example,

SELECT COALESCE(NULL, NULL, 'third_value', 'fourth_value');
--returns the third value because the third value is the first value 
--that isn't null.
--💡Tips:
--If all arguments are NULL, COALESCE returns NULL. 
--At least one of the null values must be a typed NULL.

SELECT COALESCE(Null, Null, 1, 3) AS col
--col
------
--1
SELECT COALESCE(Null, Null, 'William', Null) AS col
--col
-------
--William

--NULLIF(expression, expression)
--Returns a null value if the two specified expressions are equal. For example,
SELECT NULLIF(4,4) AS Same, NULLIF(5,7) AS Different;
--returns NULL for the first column (4 and 4) because the two input 
--values are the same. The second column returns the first value (5)
--because the two input values are different.

SELECT NULLIF(1, 3) AS col
--col
------
--1

SELECT NULLIF('2021-01-01', '2021-01-01') AS col
--col
------
--NULL

--💡Tips:
--You can use the NULLIF() function to find the product whose price does not change.
--If all arguments are NULL, COALESCE returns NULL.
--At least one of the null values must be a typed NULL.

--ISNUMERIC(expression)
--Determines whether an expression is a valid numeric type.
--Returns 1 when the input expression evaluates to a valid numeric data type;
--otherwise it returns 0. Valid numeric data types are: bigint, int, smallint,
--tinyint, bit, decimal, numeric, float, real, money, smallmoney.
SELECT ISNUMERIC ('William') AS col
--col
---
--0
SELECT ISNUMERIC (123.455) AS col
--col
---
--1

--What is the outputvalues of 
SELECT UPPER (SUBSTRING('clarusway.com', 0 , CHARINDEX('.','clarusway.com')))
--CLARUSWAY

--What is the output value of 
SELECT TRIM(' 789Sun is shining789')
--789Sun is shining789

--What is the output of 
SELECT COALESCE(NULLIF(ISNUMERIC(STR(12255.212, 7)), 1), 9999);
--9999