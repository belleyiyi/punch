drop table if exists members;
create table members(
  id integer primary key autoincrement,
  first_name text,
  last_name text,
  qq text,
  phone_number text,
  email text,
  password text,
  gender boolean);
drop table if exists kids;
create table kids(
	id integer primary key autoincrement,
	first_name text,
	last_name text,
	gender boolean,
	birthday text);
drop table if exists parents_kids;
create table parents_kids(
 foreign key(members_id) 
    references members(id)
 foreign key(kids_id)
    references kids(id)
);
drop table if exists districts;
create table districts(
	id integer primary key autoincrement,
	name text);

drop table if exists venues;
create table venues(
	id integer primary key autoincrement,
	comment text,
	contract_phone_num text,
	address text,
 	foreign key(district_id) 
    		references districts(id)
);

drop table if exists site;
create table sites(
	id integer primary key autoincrement,
	theme text,
	
	foreign key(members_id) 
    		references members(id),
	
);

drop table if exists punch;
create table punch(
	id integer primary key autoincrement,
	 foreign key(members_id) 
	    references members(id)
	 foreign key(site_id)
	    references site(id)
);
