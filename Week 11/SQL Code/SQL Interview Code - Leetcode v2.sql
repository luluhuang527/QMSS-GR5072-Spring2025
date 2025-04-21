-- POSTRE


-- Basic SQL commands
SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table

#### Create & modify tables ----------------------------
CREATE TABLE Persons (
   PersonID int,
   LastName varchar(255),
   FirstName varchar(255),
   Address varchar(255),
   City varchar(255)
)

CREATE TABLE Persons (
  ID int NOT NULL,
  LastName varchar(255) NOT NULL,
  FirstName varchar(255),
  PRIMARY KEY (ID)                -- PRIMARY KEY tells SQL that ID is the unique identifier 
)

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
  VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway')

UPDATE Customers
  SET ContactName = 'Alfred Schmidt', City='Frankfurt'
  WHERE CustomerID = 1

DELETE FROM table_name
  WHERE condition
  
  
#### Basic SQL Syntax ----------------------------

SELECT * 
  FROM Customers

SELECT CustomerName, City 
  FROM Customers

SELECT DISTINCT column1, column2 -- Unique values
  FROM table_name

SELECT column1, column2 
  FROM table_name 
  WHERE city='Mexico'  -- WHERE city!='Mexico'  OR WHERE NOT city='Mexico'

SELECT * FROM Products
  WHERE Price BETWEEN 10 AND 20

SELECT column_names
  FROM table_name
  WHERE column_name IS NULL

SELECT * FROM Customers
  ORDER BY Country ASC, CustomerName DESC

SELECT AVG(column_name)  --SUM() COUNT() MIN() MAX() are useful functions !
  FROM table_name     

SELECT col, AVG(column_name)  --Shows avg by col
  FROM table_name
  GROUP BY col1        

SELECT Country, COUNT(CustomerID), -- Frequnecy table
  FROM Customers
  GROUP BY Country
  HAVING COUNT(CustomerID) > 5 -- HAVING bc WHERE doesn't work with GROUP BY

#### Joins ----------------------------

SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
  FROM Orders 
  INNER JOIN Customers ON
  Orders.CustomerID=Customers.CustomerID

-- Union adds rows rather than cols when merging
SELECT prime_minister AS leader, country
  FROM prime_ministers
  UNION ALL                    
  SELECT monarch, country
  FROM monarchs
  ORDER BY country

-- This is like an inner join, but drops any rows with missing data if there is any
SELECT id        
  FROM left_one
  INTERSECT
  SELECT id
  FROM right_one
  
-- Joins by all non-matches in the 2nd table  
SELECT monarch, country
  FROM monarchs
  EXCEPT    
  SELECT prime_minister, country
  FROM prime_ministers
  
-- Semi-Join table onto itself, using a condition 
SELECT name FROM Employee
WHERE id in (select managerId 
                from employee 
                group by managerId 
                having count(managerId) >= 5)

SELECT name, fert_rate
  FROM states
  WHERE continent = 'Asia'
  AND fert_rate <
       (SELECT AVG(fert_rate) FROM states)

-- Perform operations as we join data
SELECT * FROM Customers
  WHERE Country IN (SELECT Country FROM Suppliers)

-- Useful SQL functions
COALESCE(col1, 0)                                -- When NULL, returns 0 instead, IFNULL in MYSQL
LENGTH(col)                                      -- Check length of string char
to_char(trans_date, 'YYYY-MM')                   -- Extracts year-month from date field
SELECT COUNT(DISTINCT player_id) FROM Activity   -- Count unique values for a var
WHERE id % 2 != 0                                -- grab odds, by using the divider remainder options
WHERE activity_date BETWEEN '2019-07-27'::DATE - INTERVAL '29 DAYS' AND '2019-07-27'::DATE -- Date subtraction
SELECT MAX(id) AS id FROM Seat                   -- Max of a variable

SELECT name, continent, indep_year,
  CASE WHEN indep_year <  1900 THEN 'before 1900'
       WHEN indep_year <= 1930 THEN '1900-1929'
       ELSE '1930+' END AS indep_year_group
  FROM states
  ORDER BY indep_year_group



SELECT DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rank -- Ranks by salary within each dept

SELECT DENSE_RANK() OVER(ORDER BY salary) AS rank --Ranks salary

(UPPER(SUBSTRING(name, 1, 1)) || LOWER(SUBSTRING(name, 2, LENGTH(name)))) --Concatenates upercase first char, all lower

INITCAP(col) -- Proper case

conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%' -- check for that string at start of any word

-- Use "," to separate multiple with statements
WITH q_sort AS (
    SELECT person_id, person_name, weight, turn, 
        SUM(weight) OVER (ORDER BY turn) AS cum_weight  -- Cumulative sum 
        FROM Queue
        ORDER BY turn )
SELECT person_name
    FROM (SELECT person_name FROM q_sort WHERE cum_weight >= 1000)
    LIMIT 1  -- Take only top 1 row
    OFFSET 1 -- ADD to skip 1st position

-- Groups by sell_date, and collapses all diff prods into a single string
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, STRING_AGG(DISTINCT product, ',' ORDER BY product) AS products
    FROM Activities GROUP BY sell_date
    
-- Join table to itslef to compare dates
SELECT w1.id 
  FROM Weather w1
  LEFT JOIN Weather w2
  ON w1.recordDate = w2.recordDate + 1
  WHERE w1.temperature > w2.temperature 

SELECT today.id
  FROM Weather yesterday 
  CROSS JOIN Weather today
  WHERE DATEDIFF(today.recordDate, yesterday.recordDate) = 1
    AND today.temperature > yesterday.temperature


-- Join table to itself, keeping only start and end times and calculating diff
SELECT a1.machine_id, 
  ROUND(AVG(a2.timestamp - a1.timestamp)::numeric,3) AS processing_time
  FROM Activity AS a1
  LEFT JOIN Activity AS a2 ON
  a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id
  AND a1.activity_type='start' AND a2.activity_type='end'
  GROUP BY a1.machine_id

-- Cross join
SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
  FROM Students AS s
  CROSS JOIN Subjects AS sub
  LEFT JOIN Examinations AS e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
  GROUP BY s.student_id, s.student_name, sub.subject_name
  ORDER BY s.student_id, sub.subject_name
                
select s.user_id, round(avg(
  case when action = 'confirmed' then 1 else 0 end),2) as confirmation_rate
  from signups s left join confirmations c
  on s.user_id = c.user_id
  group by s.user_id

-- Subquery where we select a number when it only appears once
SELECT MAX(num) AS num
    FROM MyNumbers
    WHERE ((num) IN (SELECT num FROM MyNumbers GROUP BY num  HAVING COUNT(num) = 1 ))








