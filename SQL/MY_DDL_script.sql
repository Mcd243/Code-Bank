CREATE TABLE reviews(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  food_quality_review VARCHAR(200),
  delivery_review VARCHAR(200),
  satisfaction_review VARCHAR(200)
);

INSERT INTO reviews VALUES (1,'Average food  but I like food.'
,'It was delivered on time.'
,'Overall I was satified with my order.'
);
INSERT INTO reviews VALUES (2,null,'I want to marry the rider.'
,null);
INSERT INTO reviews VALUES (3,'Food was rubbish.'
,null,null);


CREATE TABLE ratings(
  id INT AUTO_INCREMENT PRIMARY KEY,
  review_id INT 
  food_quality INT CHECK (food_quality <=5),
  delivery INT CHECK (delivery <=5),
  satisfaction INT CHECK (satisfaction <=5),
  FOREIGN KEY (review_id) REFERENCES reviews(id)
);

INSERT INTO ratings VALUES (1,1,3,5,4);
INSERT INTO ratings VALUES (2,null,null,1,null);
INSERT INTO ratings VALUES (3,null,4,null,null);
INSERT INTO ratings VALUES (4,2,null,5,null);
INSERT INTO ratings VALUES (5,null,4,2,3);
INSERT INTO ratings VALUES (6,3,1,4,2);
INSERT INTO ratings VALUES (7,null,3,1,2);
INSERT INTO ratings VALUES (8,null,4,null,null);
INSERT INTO ratings VALUES (9,null,1,2,null);
INSERT INTO ratings VALUES (10,null,3,3,3);

ALTER TABLE orders ADD rating_id INT;
ALTER TABLE orders ADD FOREIGN KEY (rating_id) REFERENCES ratings(id) ;

UPDATE orders SET rating_id = 1 WHERE id = 292 ;
UPDATE orders SET rating_id = 2 WHERE id = 1701 ;
UPDATE orders SET rating_id = 3 WHERE id = 1724 ;
UPDATE orders SET rating_id = 4 WHERE id = 1732 ;
UPDATE orders SET rating_id = 5 WHERE id = 2306 ;
UPDATE orders SET rating_id = 6 WHERE id = 3664 ;
UPDATE orders SET rating_id = 7 WHERE id = 5506 ;
UPDATE orders SET rating_id = 8 WHERE id = 7644 ;
UPDATE orders SET rating_id = 9 WHERE id = 8934 ;
UPDATE orders SET rating_id = 10 WHERE id = 9886 ;

