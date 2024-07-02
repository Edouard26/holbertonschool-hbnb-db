CREATE TABLE City (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    state VARCHAR(100),
    population INT,
    country_id VARCHAR(36),
    FOREIGN KEY (country_id) REFERENCES Country(id)
);

