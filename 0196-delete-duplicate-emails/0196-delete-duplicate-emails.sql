with sametable as ( select p1.id from person p1 
                join  person p2
                on p1.email = p2.email
                where p1.id > p2.id
                )
delete from person where id  in (select id from sametable)