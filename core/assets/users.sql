create table if not exists users(
  id varchar(12) not null,
  full_name varchar(255),
  username varchar(255) not null unique,
  email varchar(255) not null unique,
  password varchar(255) not null,
  date_joined date,
  constraint users_pk primary key(id)
);

-- alter table users alter column password drop not null;

create table if not exists salts(
  id serial not null,
  user_id varchar(12) references users(id),
  pass_salt varchar(10) not null,
  constraint salts_pk primary key(id)
);