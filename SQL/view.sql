--A view is a named SELECT statement
--It can be a useful short cut

CREATE VIEW europe AS
SELECT name, capital, population
FROM world
WHERE continent='Europe';
