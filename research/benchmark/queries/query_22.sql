-- Query 22: Product Type Profit Measure
-- Global Sales Opportunity Query

CREATE OR REPLACE TABLE "Product_Type_Profit_Measure" AS
SELECT 
    cntrycode, 
    COUNT(*) AS numcust, 
    SUM(c_acctbal) AS totacctbal 
FROM (
    SELECT 
        SUBSTRING(c.c_phone, 1, 2) AS cntrycode, 
        c.c_acctbal 
    FROM 
        CUSTOMER c 
    WHERE 
        SUBSTRING(c.c_phone, 1, 2) IN ('13', '31', '23', '29', '30', '18', '17') 
        AND c.c_acctbal > (
            SELECT AVG(c2.c_acctbal) 
            FROM CUSTOMER c2 
            WHERE c2.c_acctbal > 0.00 
            AND SUBSTRING(c2.c_phone, 1, 2) IN ('13', '31', '23', '29', '30', '18', '17')
        ) 
        AND NOT EXISTS (
            SELECT 1 
            FROM ORDERS o 
            WHERE o.o_custkey = c.c_custkey
        )
) AS custsale 
GROUP BY cntrycode 
ORDER BY cntrycode;
