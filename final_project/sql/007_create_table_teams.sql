CREATE TABLE
    IS601_Teams(
        id INT PRIMARY KEY,
        name VARCHAR(40) unique,
        country VARCHAR(20),
        code VARCHAR(3),
        logo VARCHAR(200),
        league_id INT
    )