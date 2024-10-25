-- Task1
--(1)
SELECT COUNT(*)
FROM employees;

--(2)
SELECT COUNT(*)
FROM employees
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON dept_emp.dept_no = departments.dept_no
WHERE departments.dept_name = 'Marketing';


-- Task2
-- (1)
CREATE TABLE IF NOT EXISTS salaries_for_seperate (
  emp_no int NOT NULL,
  salary int NOT NULL,
  from_date date NOT NULL,
  to_date date NOT NULL,
  PRIMARY KEY (emp_no, from_date),
  CONSTRAINT salaries_emp_no_fk FOREIGN KEY (emp_no) REFERENCES employees (emp_no)
)PARTITION BY RANGE (from_date);
-- SELECT MIN(from_date)
-- FROM salaries;
CREATE TABLE IF NOT EXISTS fragmentation1_of_salaries PARTITION OF salaries_for_seperate
FOR VALUES FROM ('1985-01-01') TO ('1990-01-01');

CREATE TABLE IF NOT EXISTS fragmentation2_of_salaries PARTITION OF salaries_for_seperate
FOR VALUES FROM ('1990-01-01') TO ('1992-01-01');

CREATE TABLE IF NOT EXISTS fragmentation3_of_salaries PARTITION OF salaries_for_seperate
FOR VALUES FROM ('1992-01-01') TO ('1994-01-01');

CREATE TABLE IF NOT EXISTS fragmentation4_of_salaries PARTITION OF salaries_for_seperate
FOR VALUES FROM ('1994-01-01') TO ('1996-01-01');

CREATE TABLE IF NOT EXISTS fragmentation5_of_salaries PARTITION OF salaries_for_seperate
FOR VALUES FROM ('1996-01-01') TO ('1998-01-01');

CREATE TABLE IF NOT EXISTS fragmentation6_of_salaries PARTITION OF salaries_for_seperate
FOR VALUES FROM ('1998-01-01') TO ('2000-01-01');

-- SELECT MAX(from_date)
-- FROM salaries;
CREATE TABLE IF NOT EXISTS fragmentation7_of_salaries PARTITION OF salaries_for_seperate
FOR VALUES FROM ('2000-01-01') TO ('2002-08-02');

TRUNCATE TABLE salaries_for_seperate;
INSERT INTO salaries_for_seperate
SELECT *
FROM salaries;

-- (2)
EXPLAIN SELECT AVG(salary)
FROM fragmentation5_of_salaries
WHERE from_date >= '1996-06-30' AND to_date <= '1996-12-31';

-- (3)
CREATE TABLE employees_public (
  emp_no int NOT NULL,
  first_name varchar(14) NOT NULL,
  last_name varchar(16) NOT NULL,
  hire_date date NOT NULL,
  PRIMARY KEY (emp_no));

INSERT INTO employees_public (
  emp_no, first_name, last_name, hire_date)
  SELECT emp_no, first_name, last_name, hire_date
  FROM employees;

CREATE DATABASE EMP_Confidential;

CREATE TABLE employees_confidential (
  emp_no int NOT NULL,
  birth_date date NOT NULL,
  gender varchar(1) NOT NULL CHECK (gender IN ('M', 'F')),
  PRIMARY KEY (emp_no)
);

-- Task 4.
-- (1)
\c EMP_s4752348;
CREATE USER sharedb WITH PASSWORD 'Y3Y7FdqDSM9.3d47XUWg';
-- Create user to deliver the data from foreign DB.
GRANT CONNECT ON DATABASE "EMP_s4752348" TO sharedb;
-- Allow user to connecet to local DB.
GRANT USAGE ON SCHEMA public TO sharedb;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO sharedb;
CREATE extension postgres_fdw;
CREATE SERVER foreign_server Foreign DATA wrapper postgres_fdw OPTIONS (
  host 'infs3200-sharedb.zones.eait.uq.edu.au',
  port '5432', 
  dbname 'sharedb');
-- "foreign_server" is server name, options should be fill with source db's host, port, and name.
CREATE USER MAPPING FOR "s4752348" SERVER foreign_server options (
  user 'sharedb', 
  PASSWORD 'Y3Y7FdqDSM9.3d47XUWg'
  );
-- Create user mapping from source DB to local DB. User after "FOR" means the actual operator, 
-- user inside options means the deliver media.
CREATE FOREIGN TABLE title_from_sharedb (
	emp_no INTEGER NOT NULL,
  title CHARACTER(40) NOT NULL,
  from_date DATE NOT NULL,
  to_date DATE) 
	SERVER foreign_server options (schema_name 'public', table_name 'titles');
-- Create a foreign table to store the arrival data(schema should be identical to the source 
-- foreign table), table_name means the exact resource table should be delivered.
-- (2)
SELECT title, AVG(salary)
FROM title_from_sharedb
JOIN salaries ON title_from_sharedb.emp_no = salaries.emp_no
WHERE title_from_sharedb.to_date = '9999-01-01'
GROUP BY title;

-- (3)
CREATE USER sharedb WITH PASSWORD 'Y3Y7FdqDSM9.3d47XUWg';
GRANT CONNECT ON DATABASE "emp_confidential" TO sharedb;
GRANT USAGE ON SCHEMA public TO sharedb;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO sharedb;
CREATE extension postgres_fdw;
CREATE SERVER foreign_server_2 Foreign DATA wrapper postgres_fdw OPTIONS (
  host 'localhost',
  port '5432', 
  dbname 'emp_confidential');
CREATE USER MAPPING FOR "s4752348" SERVER foreign_server_2 options (
  user 'sharedb', 
  PASSWORD 'Y3Y7FdqDSM9.3d47XUWg'
  );
CREATE FOREIGN TABLE confidential_table_from_EMP_Confidential(
  emp_no int NOT NULL,
  birth_date date NOT NULL,
  gender varchar(1) NOT NULL CHECK (gender IN ('M', 'F')))
  SERVER foreign_server_2 options (schema_name 'public', table_name 'employees_confidential');

SELECT emp_no
FROM employees_public

SELECT confidential_table_from_EMP_Confidential.emp_no
FROM confidential_table_from_EMP_Confidential, (
  SELECT emp_no
  FROM employees_public
) a
WHERE confidential_table_from_EMP_Confidential.emp_no = a.emp_no
AND confidential_table_from_EMP_Confidential.birth_date >= '1970-01-01'
AND confidential_table_from_EMP_Confidential.birth_date < '1975-01-01';

SELECT employees_public.first_name, employees_public.last_name
FROM employees_public, (
  SELECT confidential_table_from_EMP_Confidential.emp_no
  FROM confidential_table_from_EMP_Confidential, (
  SELECT emp_no
  FROM employees_public
  ) a
  WHERE confidential_table_from_EMP_Confidential.emp_no = a.emp_no
  AND confidential_table_from_EMP_Confidential.birth_date >= '1970-01-01'
  AND confidential_table_from_EMP_Confidential.birth_date < '1975-01-01'
) b
WHERE employees_public.emp_no = b.emp_no;

-- (4)

EXPLAIN SELECT employees_public.first_name, employees_public.last_name
FROM employees_public
INNER JOIN confidential_table_from_EMP_Confidential ON 
  employees_public.emp_no = confidential_table_from_EMP_Confidential.emp_no
WHERE confidential_table_from_EMP_Confidential.birth_date >= '1970-01-01'
AND confidential_table_from_EMP_Confidential.birth_date < '1975-01-01';

SELECT COUNT(emp_no)
FROM employees_public;

SELECT emp_no
FROM confidential_table_from_EMP_Confidential
WHERE birth_date >= '1970-01-01'
AND birth_date < '1975-01-01';