INSERT INTO student (matric_no, 
                    first_name, 
                    last_name,
                    date_of_birth)
VALUES ('4000123’, 
        'John'
        'Smith', 
        '2000-10-29');



INSERT INTO copy (copy_id,
                isbn,
                copy_status)
SELECT 1200,
        isbn,
        'On shelf'
FROM book
WHERE title = 'Database Systems: A
                Practical Approach to
                Design, Implementation and management';

                
