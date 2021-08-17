CREATE TABLE IF NOT EXISTS note
(
    id integer NOT NULL,
    title text,
    content text,
    last_modified date,
    CONSTRAINT note_pkey PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS user
(
    id integer NOT NULL,
    first_name text,
    last_name text,
    email text,
    password text,
    username text,
    lastip text,
    CONSTRAINT user_pkey PRIMARY KEY (id)
)
