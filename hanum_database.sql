-- posts_table create query
CREATE TABLE posts_table (
    id INT NOT NULL AUTO_INCREMENT,
    author VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    content VARCHAR(45) NOT NULL,
    title VARCHAR(45) NOT NULL,
    datetime VARCHAR(45) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY id_UNIQUE (id)
);
-- comments_table create query
CREATE TABLE comments_table (
    comment_id INT NOT NULL AUTO_INCREMENT,
    author VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    content VARCHAR(45) NOT NULL,
    post_id INT,
    PRIMARY KEY (comment_id),
    UNIQUE KEY id_UNIQUE (comment_id)
);