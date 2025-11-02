/* ===== BLOCK: Block 1 ===== */

/* ===== CODE: Returned_Item_Summary ===== */

CREATE OR REPLACE TABLE "SF10_Returned_Item_Summary" AS
SELECT
	L_RETURNFLAG,
	L_LINESTATUS,
	SUM(L_QUANTITY) AS SUM_QTY,
	SUM(L_EXTENDEDPRICE) AS SUM_BASE_PRICE,
	SUM(L_EXTENDEDPRICE * (1 - L_DISCOUNT)) AS SUM_DISC_PRICE,
	SUM(L_EXTENDEDPRICE * (1 - L_DISCOUNT) * (1 + L_TAX)) AS SUM_CHARGE,
	AVG(L_QUANTITY) AS AVG_QTY,
	AVG(L_EXTENDEDPRICE) AS AVG_PRICE,
	AVG(L_DISCOUNT) AS AVG_DISC,
	COUNT(*) AS COUNT_ORDER
FROM
	lineitem
WHERE
	L_SHIPDATE <= DATEADD(day, 90, '1998-12-01')
GROUP BY
	L_RETURNFLAG,
	L_LINESTATUS
ORDER BY
	L_RETURNFLAG,
	L_LINESTATUS;

/* ===== BLOCK: Block 2 ===== */

/* ===== CODE: Top_Returned_Customers ===== */

CREATE OR REPLACE TABLE "SF10_Top_Returned_Customers" AS
select
	c_custkey,
	c_name,
	sum(l_extendedprice * (1 - l_discount)) as revenue,
	c_acctbal,
	n_name,
	c_address,
	c_phone,
	c_comment
from
	customer,
	orders,
	lineitem,
	nation
where
	c_custkey = o_custkey
	and l_orderkey = o_orderkey
	and o_orderdate >= date '1993-10-01'
	AND o_orderdate < DATEADD(month, 3, '1993-10-01')
	and l_returnflag = 'R'
	and c_nationkey = n_nationkey
group by
	c_custkey,
	c_name,
	c_acctbal,
	c_phone,
	n_name,
	c_address,
	c_comment
order by
	revenue desc limit 20;

/* ===== BLOCK: Block 3 ===== */

/* ===== CODE: Important_Stock ===== */

CREATE OR REPLACE TABLE "SF10_Important_Stock" AS
select
	ps_partkey,
	sum(ps_supplycost * ps_availqty) as value
from
	partsupp,
	supplier,
	nation
where
	ps_suppkey = s_suppkey
	and s_nationkey = n_nationkey
	and n_name = 'GERMANY'
group by
	ps_partkey having
		sum(ps_supplycost * ps_availqty) > (
			select
				sum(ps_supplycost * ps_availqty) * 0.0001000000
			from
				partsupp,
				supplier,
				nation
			where
				ps_suppkey = s_suppkey
				and s_nationkey = n_nationkey
				and n_name = 'GERMANY'
		)
order by
	value desc;

/* ===== BLOCK: Block 4 ===== */

/* ===== CODE: Shipping_Modes_Priority ===== */

CREATE OR REPLACE TABLE "SF10_Shipping_Modes_Priority" AS
select
	l_shipmode,
	sum(case
		when o_orderpriority = '1-URGENT'
			or o_orderpriority = '2-HIGH'
			then 1
		else 0
	end) as high_line_count,
	sum(case
		when o_orderpriority <> '1-URGENT'
			and o_orderpriority <> '2-HIGH'
			then 1
		else 0
	end) as low_line_count
from
	orders,
	lineitem
where
	o_orderkey = l_orderkey
	and l_shipmode in ('MAIL', 'SHIP')
	and l_commitdate < l_receiptdate
	and l_shipdate < l_commitdate
	and l_receiptdate >= date '1994-01-01'
	AND o_orderdate < DATEADD(year, 1, '1994-01-01')
group by
	l_shipmode
order by
	l_shipmode;

/* ===== BLOCK: Block 5 ===== */

/* ===== CODE: Customer_Distribution ===== */

CREATE OR REPLACE TABLE "SF10_Customer_Distribution" AS
select
	c_count,
	count(*) as custdist
from
	(
		select
			c_custkey,
			count(o_orderkey)
		from
			customer left outer join orders on
				c_custkey = o_custkey
				and o_comment not like '%special%requests%'
		group by
			c_custkey
	) as c_orders (c_custkey, c_count)
group by
	c_count
order by
	custdist desc,
	c_count desc;

/* ===== BLOCK: Block 6 ===== */

/* ===== CODE: Promotion_Effect ===== */

CREATE OR REPLACE TABLE "SF10_Promotion_Effect" AS
select
	100.00 * sum(case
		when p_type like 'PROMO%'
			then l_extendedprice * (1 - l_discount)
		else 0
	end) / sum(l_extendedprice * (1 - l_discount)) as promo_revenue
from
	lineitem,
	part
where
	l_partkey = p_partkey
	and l_shipdate >= date '1995-09-01'
	AND l_shipdate < DATEADD(month, 1, '1995-09-01');

/* ===== BLOCK: Block 7 ===== */

/* ===== CODE: Top_Supplier ===== */

CREATE OR REPLACE TABLE "SF10_Top_Supplier" AS
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

/* ===== BLOCK: Block 8 ===== */

/* ===== CODE: Supplier_Relationship ===== */

CREATE OR REPLACE TABLE "SF10_Supplier_Relationship" AS
select
	p_brand,
	p_type,
	p_size,
	count(distinct ps_suppkey) as supplier_cnt
from
	partsupp,
	part
where
	p_partkey = ps_partkey
	and p_brand <> 'Brand#45'
	and p_type not like 'MEDIUM POLISHED%'
	and p_size in (49, 14, 23, 45, 19, 3, 36, 9)
	and ps_suppkey not in (
		select
			s_suppkey
		from
			supplier
		where
			s_comment like '%Customer%Complaints%'
	)
group by
	p_brand,
	p_type,
	p_size
order by
	supplier_cnt desc,
	p_brand,
	p_type,
	p_size;

/* ===== BLOCK: Block 9 ===== */

/* ===== CODE: Small_Quantity_Order_Revenue ===== */

CREATE OR REPLACE TABLE "SF10_Small_Quantity_Order_Revenue" AS
select
	sum(l_extendedprice) / 7.0 as avg_yearly
from
	lineitem,
	part
where
	p_partkey = l_partkey
	and p_brand = 'Brand#23'
	and p_container = 'MED BOX'
	and l_quantity < (
		select
			0.2 * avg(l_quantity)
		from
			lineitem
		where
			l_partkey = p_partkey
	);

/* ===== BLOCK: Block 10 ===== */

/* ===== CODE: Large_Volume_Customers ===== */

CREATE OR REPLACE TABLE "SF10_Large_Volume_Customers" AS
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

/* ===== BLOCK: Block 11 ===== */

/* ===== CODE: Discounted_Revenue ===== */

CREATE OR REPLACE TABLE "SF10_Discounted_Revenue" AS
select
	sum(l_extendedprice* (1 - l_discount)) as revenue
from
	lineitem,
	part
where
	(
		p_partkey = l_partkey
		and p_brand = 'Brand#12'
		and p_container in ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG')
		and l_quantity >= 1 and l_quantity <= 1 + 10
		and p_size between 1 and 5
		and l_shipmode in ('AIR', 'AIR REG')
		and l_shipinstruct = 'DELIVER IN PERSON'
	)
	or
	(
		p_partkey = l_partkey
		and p_brand = 'Brand#23'
		and p_container in ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK')
		and l_quantity >= 10 and l_quantity <= 10 + 10
		and p_size between 1 and 10
		and l_shipmode in ('AIR', 'AIR REG')
		and l_shipinstruct = 'DELIVER IN PERSON'
	)
	or
	(
		p_partkey = l_partkey
		and p_brand = 'Brand#34'
		and p_container in ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG')
		and l_quantity >= 20 and l_quantity <= 20 + 10
		and p_size between 1 and 15
		and l_shipmode in ('AIR', 'AIR REG')
		and l_shipinstruct = 'DELIVER IN PERSON'
	);

/* ===== BLOCK: Block 12 ===== */

/* ===== CODE: Minimum_Cost_Supplier ===== */

CREATE OR REPLACE TABLE "SF10_Minimum_Cost_Supplier" AS
select
	s_acctbal,
	s_name,
	n_name,
	p_partkey,
	p_mfgr,
	s_address,
	s_phone,
	s_comment
from
	part,
	supplier,
	partsupp,
	nation,
	region
where
	p_partkey = ps_partkey
	and s_suppkey = ps_suppkey
	and p_size = 15
	and p_type like '%BRASS'
	and s_nationkey = n_nationkey
	and n_regionkey = r_regionkey
	and r_name = 'EUROPE'
	and ps_supplycost = (
		select
			min(ps_supplycost)
		from
			partsupp,
			supplier,
			nation,
			region
		where
			p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'EUROPE'
	)
order by
	s_acctbal desc,
	n_name,
	s_name,
	p_partkey LIMIT 100;

/* ===== BLOCK: Block 13 ===== */

/* ===== CODE: Potential_Part_Promotion ===== */

CREATE OR REPLACE TABLE "SF10_Potential_Part_Promotion" AS
select
	s_name,
	s_address
from
	supplier,
	nation
where
	s_suppkey in (
		select
			ps_suppkey
		from
			partsupp
		where
			ps_partkey in (
				select
					p_partkey
				from
					part
				where
					p_name like 'forest%'
			)
			and ps_availqty > (
				select
					0.5 * sum(l_quantity)
				from
					lineitem
				where
					l_partkey = ps_partkey
					and l_suppkey = ps_suppkey
					and l_shipdate >= date '1994-01-01'
                	AND l_shipdate < DATEADD(year, 1, '1994-01-01')
			)
	)
	and s_nationkey = n_nationkey
	and n_name = 'CANADA'
order by
	s_name;

/* ===== BLOCK: Block 14 ===== */

/* ===== CODE: Suppliers_Order_Waiting ===== */

CREATE OR REPLACE TABLE "SF10_Suppliers_Order_Waiting" AS
select
	s_name,
	count(*) as numwait
from
	supplier,
	lineitem l1,
	orders,
	nation
where
	s_suppkey = l1.l_suppkey
	and o_orderkey = l1.l_orderkey
	and o_orderstatus = 'F'
	and l1.l_receiptdate > l1.l_commitdate
	and exists (
		select
			*
		from
			lineitem l2
		where
			l2.l_orderkey = l1.l_orderkey
			and l2.l_suppkey <> l1.l_suppkey
	)
	and not exists (
		select
			*
		from
			lineitem l3
		where
			l3.l_orderkey = l1.l_orderkey
			and l3.l_suppkey <> l1.l_suppkey
			and l3.l_receiptdate > l3.l_commitdate
	)
	and s_nationkey = n_nationkey
	and n_name = 'SAUDI ARABIA'
group by
	s_name
order by
	numwait desc,
	s_name limit 100;

/* ===== BLOCK: Block 15 ===== */

/* ===== CODE: Global_Sales_Opportunity ===== */

CREATE OR REPLACE TABLE "SF10_Global_Sales_Opportunity" AS
select
	cntrycode,
	count(*) as numcust,
	sum(c_acctbal) as totacctbal
from
	(
		select
      SUBSTRING(c_phone, 1, 2) AS cntrycode,
			c_acctbal
		from
			customer
		where
          SUBSTRING(c_phone, 1, 2) IN
				('13', '31', '23', '29', '30', '18', '17')
			and c_acctbal > (
				select
					avg(c_acctbal)
				from
					customer
				where
					c_acctbal > 0.00
                    AND SUBSTRING(c_phone, 1, 2) IN
						('13', '31', '23', '29', '30', '18', '17')
			)
			and not exists (
				select
					*
				from
					orders
				where
					o_custkey = c_custkey
			)
	) as custsale
group by
	cntrycode
order by
	cntrycode;

/* ===== BLOCK: Block 16 ===== */

/* ===== CODE: Shipping_Priority ===== */

CREATE OR REPLACE TABLE "SF10_Shipping_Priority" AS
select
	l_orderkey,
	sum(l_extendedprice * (1 - l_discount)) as revenue,
	o_orderdate,
	o_shippriority
from
	customer,
	orders,
	lineitem
where
	c_mktsegment = 'BUILDING'
	and c_custkey = o_custkey
	and l_orderkey = o_orderkey
	and o_orderdate < date '1995-03-15'
	and l_shipdate > date '1995-03-15'
group by
	l_orderkey,
	o_orderdate,
	o_shippriority
order by
	revenue desc,
	o_orderdate limit 10;

/* ===== BLOCK: Block 17 ===== */

/* ===== CODE: Order_Priority_Checking ===== */

CREATE OR REPLACE TABLE "SF10_Order_Priority_Checking" AS
select
	o_orderpriority,
	count(*) as order_count
from
	orders
where
	o_orderdate >= date '1993-07-01'
	AND o_orderdate < DATEADD(month, 3, '1993-07-01')
	and exists (
		select
			*
		from
			lineitem
		where
			l_orderkey = o_orderkey
			and l_commitdate < l_receiptdate
	)
group by
	o_orderpriority
order by
	o_orderpriority;

/* ===== BLOCK: Block 18 ===== */

/* ===== CODE: Local_Supplier_Volume ===== */

CREATE OR REPLACE TABLE "SF10_Local_Supplier_Volume" AS
select
	n_name,
	sum(l_extendedprice * (1 - l_discount)) as revenue
from
	customer,
	orders,
	lineitem,
	supplier,
	nation,
	region
where
	c_custkey = o_custkey
	and l_orderkey = o_orderkey
	and l_suppkey = s_suppkey
	and c_nationkey = s_nationkey
	and s_nationkey = n_nationkey
	and n_regionkey = r_regionkey
	and r_name = 'ASIA'
	and o_orderdate >= date '1994-01-01'
	AND o_orderdate < DATEADD(year, 1, '1994-01-01')
group by
	n_name
order by
	revenue desc;

/* ===== BLOCK: Block 19 ===== */

/* ===== CODE: Forecasting_Revenue_Change ===== */

CREATE OR REPLACE TABLE "SF10_Forecasting_Revenue_Change" AS
select
	sum(l_extendedprice * l_discount) as revenue
from
	lineitem
where
	l_shipdate >= date '1994-01-01'
	AND l_shipdate < DATEADD(year, 1, '1994-01-01')
	and l_discount between .06 - 0.01 and .06 + 0.01
	and l_quantity < 24;

/* ===== BLOCK: Block 20 ===== */

/* ===== CODE: Volume_Shipping ===== */

CREATE OR REPLACE TABLE "SF10_Volume_Shipping" AS
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
            EXTRACT(YEAR FROM CAST(l_shipdate AS DATE)) AS l_year,
            l_extendedprice * (1 - l_discount) AS volume
        FROM
            supplier,
            lineitem,
            orders,
            customer,
            nation n1,
            nation n2
        WHERE
            s_suppkey = l_suppkey
            AND o_orderkey = l_orderkey
            AND c_custkey = o_custkey
            AND s_nationkey = n1.n_nationkey
            AND c_nationkey = n2.n_nationkey
            AND (
                (n1.n_name = 'FRANCE' AND n2.n_name = 'GERMANY')
                OR (n1.n_name = 'GERMANY' AND n2.n_name = 'FRANCE')
            )
            AND l_shipdate BETWEEN DATE '1995-01-01' AND DATE '1996-12-31'
    ) AS shipping
GROUP BY
    supp_nation,
    cust_nation,
    l_year
ORDER BY
    supp_nation,
    cust_nation,
    l_year;

/* ===== BLOCK: Block 21 ===== */

/* ===== CODE: National_Market_Share ===== */

CREATE OR REPLACE TABLE "SF10_National_Market_Share" AS
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

/* ===== BLOCK: Block 22 ===== */

/* ===== CODE: Product_Type_Profit_Measure ===== */

CREATE OR REPLACE TABLE "SF10_Product_Type_Profit_Measure" AS
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

