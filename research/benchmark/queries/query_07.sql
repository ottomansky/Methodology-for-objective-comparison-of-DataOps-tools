-- Query 7: Top Supplier
-- Volume Shipping Query

CREATE OR REPLACE TABLE "Top_Supplier" AS
SELECT 
    supp_nation, 
    cust_nation, 
    l_year, 
    SUM(volume) AS revenue 
FROM 
    (
        SELECT 
            n1.n_name AS supp_nation, 
            n2.n_name AS cust_nation, 
            EXTRACT(YEAR FROM CAST(l.l_shipdate AS DATE)) AS l_year, 
            l.l_extendedprice * (1 - l.l_discount) AS volume 
        FROM 
            SUPPLIER s
            JOIN LINEITEM l ON s.s_suppkey = l.l_suppkey
            JOIN ORDERS o ON l.l_orderkey = o.o_orderkey
            JOIN CUSTOMER c ON o.o_custkey = c.c_custkey
            JOIN NATION n1 ON s.s_nationkey = n1.n_nationkey
            JOIN NATION n2 ON c.c_nationkey = n2.n_nationkey
        WHERE 
            (
                (n1.n_name = 'FRANCE' AND n2.n_name = 'GERMANY') 
                OR (n1.n_name = 'GERMANY' AND n2.n_name = 'FRANCE')
            )
            AND CAST(l.l_shipdate AS DATE) BETWEEN DATE '1995-01-01' AND DATE '1996-12-31'
    ) AS shipping 
GROUP BY 
    supp_nation, 
    cust_nation, 
    l_year 
ORDER BY 
    supp_nation, 
    cust_nation, 
    l_year;
