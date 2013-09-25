
-- Find the ID of the artist that has gained the most fans since September 1, 2012.

select CountTable.artist
from (
  select f2.artistid as artist, count(*) as fancount
  from fan f2
  where
    f2.since >= TO_DATE('01-09-2012', 'DD-MM-YYYY')
  group by f2.artistid
  order by fancount desc
  ) CountTable
where 
  rownum = 1
;
