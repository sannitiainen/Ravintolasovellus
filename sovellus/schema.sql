CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE, 
    password TEXT, 
    admin INTEGER
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name TEXT,
    openinghours TEXT,
    address TEXT,
    info TEXT,
    visible INTEGER,
    avg_rating FLOAT,
    type TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    restaurant_id INTEGER REFERENCES restaurants,
    rating INTEGER,
    comment TEXT,
    visible INTEGER
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name TEXT,
    creator_id INTEGER REFERENCES users
    visible INTEGER
);

CREATE TABLE map_group (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants,
    group_id INTEGER REFERENCES groups
);
