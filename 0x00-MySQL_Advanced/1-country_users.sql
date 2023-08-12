-- SQL script that creates a tablecalled users
-- the attributes are id, email, name and country
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country enum('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
	);
