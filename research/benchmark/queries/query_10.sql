-- Query 10: Large Volume Customers
-- Returned Item Reporting Query

CREATE OR REPLACE TABLE "Large_Volume_Customers" AS
SELECT
    c.c_custkey,
    c.c_name,
    SUM(l.l_extendedprice * (1 - l.l_discount)) AS revenue,
    c.c_acctbal,
    n.n_name,
    c.c_address,
    c.c_phone,
    c.c_comment
FROM
    CUSTOMER c
    JOIN ORDERS o ON c.c_custkey = o.o_custkey
    JOIN LINEITEM l ON o.o_orderkey = l.l_orderkey
    JOIN NATION n ON c.c_nationkey = n.n_nationkey
WHERE
    o.o_orderdate >= DATE '1993-10-01' 
    AND o.o_orderdate < DATEADD('MONTH', 3, DATE '1993-10-01')
    AND l.l_returnflag = 'R'
GROUP BY
    c.c_custkey,
    c.c_name,
    c.c_acctbal,
    c.c_phone,
    n.n_name,
    c.c_address,
    c.c_comment
ORDER BY
    revenue DESC
LIMIT 20;
