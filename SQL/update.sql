UPDATE copy
SET    status = 'On loan'
WHERE  copy_id = 1200;

UPDATE book
SET    main_author = 'Connolly, Thomas',
        other_authors = 'Begg, Caroline'
WHERE isbn = '978-0321210258';
