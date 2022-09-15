-- COLUMN DEFINITION
ALTER TABLE student 
MODIFY last_name VARCHAR(25);

-- Add a column
ALTER TABLE student
ADD middle_name VARCHAR(20);

-- Drop a table
DROP TABLE student;