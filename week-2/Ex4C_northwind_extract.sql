/*
4a) The Products table holds the items Northwind sells. 
4b) The Categories table holds the types of the items Northwind sells.
5a) The employee with the bird name is Margaret Peacock.
6a) The query returned 77 records. You can make the query retrieve only 10 rows by using the "Limit to..." drop down menu.
7a) The category id of seafood is 8.
*/
USE northwind;
SELECT * FROM Employees;
SELECT * FROM products;
SELECT * FROM  categories;
SELECT OrderID, OrderDate, ShipName, ShipCountry FROM Orders;