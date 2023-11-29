-- posts_table create query
CREATE TABLE posts_table (
    id INT NOT NULL AUTO_INCREMENT,
    author VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    content VARCHAR(45) NOT NULL,
    title VARCHAR(45) NOT NULL,
    comment INT DEFAULT 0,
    uploadAt VARCHAR(45) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY id_UNIQUE (id)
);
-- comments_table create query
CREATE TABLE comments_table (
    id INT NOT NULL AUTO_INCREMENT,
    author VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    content VARCHAR(45) NOT NULL,
    post_id INT,
    uploadAt VARCHAR(45) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY id_UNIQUE (id)
);

-- trigger + 
DELIMITER //

CREATE TRIGGER update_comments_count
AFTER INSERT ON comments_table
FOR EACH ROW
BEGIN
    UPDATE posts_table
    SET comment = comment + 1
    WHERE id = NEW.post_id;
END;
//

DELIMITER ;

-- trigger -
DELIMITER //

CREATE TRIGGER decrease_comments_count
AFTER DELETE ON comments_table
FOR EACH ROW
BEGIN
    UPDATE posts_table
    SET comment = comment - 1
    WHERE id = OLD.post_id;
END;
//

DELIMITER ;
