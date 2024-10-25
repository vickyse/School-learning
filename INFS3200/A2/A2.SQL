CREATE DATABASE A2
\c a2 -- 創建資料庫

CREATE TABLE originaldata(
    TID INT,
    SID INT,
    FNAME VARCHAR(20),
    LNAME VARCHAR(20),
    STATE VARCHAR(10),
    STORE VARCHAR(10),
    DATE DATE,
    PID INT,
    BRAND VARCHAR(20),
    PRODUCT VARCHAR(40),
    UNIT_COST DECIMAL(10, 2),
    QUANTITY INT,
    PRICE DECIMAL(10, 2)
);
\COPY originaldata FROM '/home/s4752348/P4-materials/Sales.csv' WITH CSV HEADER;
-- 創建原始資料庫的表格，把CSV丟入其中。

-- 2.1
CREATE TABLE staff(
    SID INT NOT NULL,
    FNAME VARCHAR(20) NOT NULL,
    LNAME VARCHAR(20) NOT NULL, 
    STATE VARCHAR(10) NOT NULL,
    STORE VARCHAR(10) NOT NULL,
    PRIMARY KEY (SID)
);

CREATE TABLE product(
    PID INT NOT NULL,
    BRAND VARCHAR(20),
    PRODUCT VARCHAR(40),
    UNIT_COST DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY(PID)
);

CREATE TABLE time_period(
    DATE DATE,
    year INT,
    month INT,
    quarter INT
);
-- 創造3個維度表。

-- 2.2
INSERT INTO staff(SID, FNAME, LNAME, STATE, STORE)
SELECT SID, FNAME, LNAME, STATE, STORE
FROM originaldata
ON CONFLICT DO NOTHING;

INSERT INTO product(PID, product, UNIT_COST)
SELECT DISTINCT(PID), product, UNIT_COST
FROM originaldata;

INSERT INTO time_period(DATE, year, month, quarter)
SELECT DATE,
    EXTRACT(YEAR FROM DATE) AS year,
    EXTRACT(MONTH FROM DATE) AS month,
    EXTRACT(QUARTER FROM DATE) AS quarter
FROM originaldata;

SELECT COUNT(*)
FROM time_period
WHERE year = 2022
AND quarter = 3;

-- 2.3

CREATE MATERIALIZED VIEW Sales_Time_Staff AS
SELECT originaldata.STATE, unique_time_period.quarter, unique_time_period.year,
    SUM(QUANTITY * (PRICE - UNIT_COST)) AS profits
FROM originaldata
LEFT JOIN (
    SELECT DISTINCT DATE, quarter, year
    FROM time_period
) AS unique_time_period ON unique_time_period.DATE = originaldata.DATE
GROUP BY CUBE(originaldata.STATE, unique_time_period.quarter, unique_time_period.year);


-- 2.4

CREATE VIEW Q2_4 AS
SELECT STATE, year, quarter, profits 
FROM Sales_Time_Staff
WHERE STATE IS NOT NULL
  AND year = 2021
  AND quarter IS NOT NULL
ORDER BY STATE, year, quarter;

-- 2.5

CREATE MATERIALIZED VIEW Sales_Product_Staff AS
SELECT originaldata.STATE, originaldata.STORE, originaldata.PRODUCT, originaldata.PRICE,
    SUM(QUANTITY * (PRICE - UNIT_COST)) AS profits
FROM originaldata
GROUP BY CUBE(originaldata.STATE, originaldata.STORE, originaldata.PRODUCT, originaldata.PRICE);


CREATE VIEW Q5_1 AS
SELECT STORE, SUM(profits) AS total_profits
FROM Sales_Product_Staff
WHERE STORE IS NOT NULL
GROUP BY STORE
ORDER BY total_profits DESC
LIMIT 3;

