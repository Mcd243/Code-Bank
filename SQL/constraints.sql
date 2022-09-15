CREATE TABLE module (
    module_code    VARCHAR(8) PRIMARY KEY,
    module_title   VARCHAR(40) NOT NULL,
    level          INT NOT NULL,
    credits        INT NOT NULL
);

-- CHECK

CREATE TABLE student (
    matric_no     VARCHAR(8) PRIMARY KEY,
    first_name    VARCHAR(20),
    last_name     VARCHAR(20),
    age 		 INT CHECK (age >=16)
);

-- Add a check
ALTER TABLE student
ADD CHECK (age >=16);