CREATE TABLE Country (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    code VARCHAR(3) UNIQUE NOT NULL,  -- ISO country code
    continent VARCHAR(50)
);

