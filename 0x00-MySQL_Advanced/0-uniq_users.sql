/*SQL script that creates a table users with the following 
 id, integer, never null, auto increment and primary key
 emai, string (255 characters), never null and unique
 name, string (255 characters)
 */

CREATE TABLE IF NOT EXISTS users(id INT NOT NULL AUTO_INCREMENT PRIMARY kEY,
	email VARCHAR(255) NOT NULL UNIQUE,
 	name VARCHAR(255)
	)
