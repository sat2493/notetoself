CREATE TABLE IF NOT EXISTS note
(
    id serial PRIMARY KEY,
    title text,
    content text,
    last_updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    userid integer NOT NULL,
    CONSTRAINT note_userid FOREIGN KEY (userid) REFERENCES "user"(id)
);

CREATE TABLE IF NOT EXISTS "user"
(
    id serial PRIMARY KEY,
    first_name text,
    last_name text,
    email text,
    password text,
    username text,
    lastip text
);
