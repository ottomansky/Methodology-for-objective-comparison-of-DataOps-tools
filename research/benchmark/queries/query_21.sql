-- Query 21: National Market Share
-- Suppliers Who Kept Orders Waiting Query

CREATE OR REPLACE TABLE "National_Market_Share" AS
SELECT 
    s.s_name, 
    COUNT(*) AS numwait 
FROM 
    SUPPLIER s
JOIN 
    LINEITEM l1 ON s.s_suppkey = l1.l_suppkey
JOIN 
    ORDERS o ON o.o_orderkey = l1.l_orderkey
JOIN 
    NATION n ON s.s_nationkey = n.n_nationkey
WHERE 
    o.o_orderstatus = 'F' 
    AND l1.l_receiptdate > l1.l_commitdate
    AND EXISTS (
        SELECT 1 
        FROM LINEITEM l2 
        WHERE l2.l_orderkey = l1.l_orderkey 
        AND l2.l_suppkey <> l1.l_suppkey
    )
    AND NOT EXISTS (
        SELECT 1 
        FROM LINEITEM l3 
        WHERE l3.l_orderkey = l1.l_orderkey 
        AND l3.l_suppkey <> l1.l_suppkey 
        AND l3.l_receiptdate > l3.l_commitdate
    )
    AND n.n_name = 'SAUDI ARABIA' 
GROUP BY 
    s.s_name 
ORDER BY 
    numwait DESC, 
    s.s_name 
LIMIT 100;
