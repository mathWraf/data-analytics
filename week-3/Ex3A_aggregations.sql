USE northwind;

/*
Write a query to find the price of the cheapest item that Northwind sells. Then write a
second query to find the name of the product that has that price.
*/
SELECT MIN(UnitPrice)
FROM Products;

SELECT ProductName
FROM Products
WHERE UnitPrice = 2.50;

-- Write a query to find the average price of all items that Northwind sells.
SELECT AVG(UnitPrice)
FROM Products;

/*
Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product.
*/
SELECT MAX(UnitPrice)
FROM Products;

SELECT p.ProductName, s.CompanyName
FROM Products p
JOIN Suppliers s
ON p.SupplierID = s.SupplierID
WHERE UnitPrice = 263.50;

-- Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).
SELECT SUM(Salary) 
FROM Employees;

/*
Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!)
*/
SELECT MAX(Salary), MIN(Salary)
FROM Employees;

/*
Write a query to find the name and supplier ID of each supplier and the number of
items they supply. 
*/
SELECT s.CompanyName, s.SupplierID, COUNT(p.ProductName)
FROM Suppliers s
LEFT JOIN Products p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID;

/*
Write a query to find the list of all category names and the average price for items in
each category.
*/
SELECT c.CategoryName, AVG(p.UnitPrice)
FROM Categories c
LEFT JOIN Products p
ON c.CategoryID = p.CategoryID
GROUP BY C.CategoryName;

/*
Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
is the name of each supplier and the number of items they supply.
*/
SELECT s.CompanyName, s.SupplierID, COUNT(p.ProductName) AS total_amount
FROM Suppliers s
LEFT JOIN Products p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID
HAVING total_amount >= 5;

/*
Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list.
*/
SELECT ProductID, ProductName, UnitsInStock * UnitPrice AS inventory_value
FROM Products
WHERE UnitsInStock >= 1
ORDER BY inventory_value DESC, ProductName;