USE northwind;

-- What is the product name(s) of the most expensive products?
SELECT ProductName
FROM Products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

-- What is the product name(s) and categories of the least expensive products?
SELECT p.ProductName, c.CategoryName
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM Products);

-- What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName
FROM Orders o
JOIN Shippers s
ON o.ShipVia = s.ShipperID
WHERE o.ShipVia = (SELECT ShipperID FROM Shippers WHERE CompanyName = "Federal Shipping");

-- What are the order ids of the orders that included "Sasquatch Ale"?
SELECT od.OrderID, p.ProductName
FROM `Order Details` od
JOIN Products p
ON od.ProductID = p.ProductID
WHERE od.ProductID = (SELECT ProductID FROM Products WHERE ProductName = "Sasquatch Ale");

-- What is the name of the employee that sold order 10266?
SELECT e.LastName, e.FirstName
FROM Orders o
JOIN Employees e
ON o.EmployeeID = e.EmployeeID
WHERE o.OrderID = (SELECT OrderID FROM Orders WHERE OrderID = 10266);

-- What is the name of the customer that bought order 10266?
SELECT CompanyName
FROM Orders o
JOIN Customers c
ON o.CustomerID = c.CustomerID
WHERE o.OrderID = (SELECT OrderID FROM Orders WHERE OrderID = 10266);
