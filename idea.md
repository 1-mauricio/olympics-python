CRUD

Create - insert - create
database
table


Read - select
tables

Update - update


Delete - delete
database
table






COMANDS

USE olympics;
CREATE TABLE medals (
	rank INT(10),
    team VARCHAR(100),
    gold INT(4),
    silver INT(4),
    bronze INT(4),
    total INT(4),
    rank_total INT(10)
); 

insert_ = ("INSERT INTO medals "
        "(rank, team, gold, silver, bronze, total, rank_total) "
        f" VALUES ('{rank}, {team}, {gold}, {silver}, {bronze}, {total}, {rank_total}')")