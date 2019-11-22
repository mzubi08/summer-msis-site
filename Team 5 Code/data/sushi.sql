-- We're cheating a little by requiring everything to be NOT NULL,
-- but it will make things a bit easier on the Python side.

CREATE TABLE sushi (
  id INTEGER PRIMARY KEY, -- sqLite will automatically auto-increment *if* (and only if) using the integer type for the primary key
  name VARCHAR(24) NOT NULL,
  price DECIMAL (5,2) NOT NULL
);


INSERT INTO sushi (id, name, price)
  VALUES (1, 'California Roll', 5.99);
INSERT INTO sushi (id, name, price)
  VALUES (2, 'Spicy Tuna Roll', 6.99);
INSERT INTO sushi (id, name, price)
  VALUES (3, 'Ahi Nigiri', 4.50);
