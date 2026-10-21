/*
a) The information in the actor table are actor names, their IDs, and their last update.
b) The information in the film table are film titles, their IDs, titles, descriptions, release years, language, original language, rental duration, rental rate, time length, replacement cost, ratings, special features, and their last update.
c) the film actor table contains both actor_id and film_id as columns.
d) The rental table includes a rental ID, rental date, inventory and customer IDs, return date, staff ID, and last update. The information is easy to read because everything is formatted properly.
e) The inventory table includes an inventory ID, film and store IDs, and last update.
f) The tables I need to learn the names of all films rented on a specific date are the film, inventory, and rental tables. The film and inventory tables have film_id as a common field, and the inventory and rental tables have inventory_id as a common field.
*/

USE sakila;
SELECT film_id, title FROM film;
SELECT inventory_id, film_id FROM inventory;
SELECT inventory_id, rental_date FROM rental;