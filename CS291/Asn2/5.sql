
-- For the album titled 'A1', find the title of all other albums that share at 
-- least one artist.

select distinct m1.title
from media m1
join song s1 on (m1.id = s1.albumid)
join artist a1 on (s1.artistid = a1.aid)
join media m2 on (m1.id != m2.id and m2.title = 'A1')
join song s2 on (m2.id = s2.albumid and s2.artistid = a1.aid)
;
