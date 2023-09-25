CREATE TABLE users (
	id INTEGER NOT NULL,
	name VARCHAR(30) NOT NULL,
	username VARCHAR,
	PRIMARY KEY (id),
	UNIQUE (name)
);



CREATE TABLE addresses (
	id INTEGER NOT NULL,
	email VARCHAR NOT NULL,
	user_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES users (id)
);

INSERT INTO users (name, username) VALUES (?, ?)
('Bob White', 'bob');




INSERT INTO users (name, username) VALUES ('John Smith', 'john');

INSERT INTO addresses (email, user_id) VALUES ('jone@gmail.com', 2),('jone.smith@gmail.gov', 2);


INSERT INTO addresses (email, user_id) VALUES ('bob@example.com', 1);

SELECT users.id, users.name, users.username
FROM users;

SELECT addresses.user_id AS addresses_user_id,
       addresses.id AS addresses_id,
       addresses.email AS addresses_email

FROM addresses
WHERE addresses.user_id IN (1, 2);



SELECT addresses.id,addresses.email,
       addresses.user_id, users_1.id AS id_1,
       users_1.name, users_1.username
FROM addresses LEFT OUTER JOIN users AS users_1 ON
     users_1.id = addresses.user_id
