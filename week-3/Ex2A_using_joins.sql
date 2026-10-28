USE northwind;

/*
Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name.
*/
SELECT p.ProductID, p.ProductName,p.UnitPrice, c.CategoryName
FROM Products AS p
LEFT JOIN Categories AS c
ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;

/*
Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name.
*/
SELECT p.ProductID, p.ProductName,p.UnitPrice, s.CompanyName
FROM Products AS p
LEFT JOIN Suppliers AS s
ON p.SupplierID = s.SupplierID
WHERE UnitPrice > 75
ORDER BY p.ProductName;

/*
Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name.
*/
SELECT p.ProductID, p.ProductName,p.UnitPrice, c.CategoryName, s.CompanyName
FROM Products AS p
LEFT Join Categories AS c
ON p.CategoryID = c.CategoryID
LEFT JOIN Suppliers AS s
ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName;

/*
Create a single query to list the order id, ship name, ship address, and shipping
company name of every order that shipped to Germany. Assign the shipping company
name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
shipped to.
*/
SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName AS "Shipper"
FROM Orders AS o
LEFT JOIN Shippers AS s
ON o.ShipVia = s.ShipperID
LEFT JOIN Customers AS c
ON o.CustomerID = c.CustomerID
WHERE o.ShipCountry = "Germany"
ORDER BY s.CompanyName, c.CompanyName;

/*
Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name.
*/
SELECT o.ShipName, COUNT(o.OrderID)
FROM Orders AS o
LEFT JOIN Shippers AS s
ON o.ShipVia = s.ShipperID
LEFT JOIN Customers AS c
ON o.CustomerID = c.CustomerID
WHERE o.ShipCountry = "Germany"
GROUP BY o.ShipName;

/*
Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale.
*/
SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM Orders AS o
LEFT JOIN `Order Details` AS od
ON o.OrderID = od.OrderID
LEFT JOIN Products AS p
ON od.ProductID = p.ProductID
WHERE p.ProductName = "Sasquatch Ale";

