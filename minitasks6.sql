-- 1.
select * from products
where category_id > 3
order by product_name;

-- 2.
select * from customers
where country = 'Brazil'
	and company_name like '__n%'

-- 3.
select * from customers
where country = 'Germany'and company_name like '%a__' -- UK da chiqmadi, Germaniyaga o'zgartirdim.

-- 4.
select avg(unit_price) from products

-- 5.
select * from orders
where extract (year from order_date) = 1997
	and extract (month from order_date) = 7
	and required_date < shipped_date

-- 6.
select * from products
where category_id = 1
	and unit_price = (
		select max(unit_price) from products
	)

