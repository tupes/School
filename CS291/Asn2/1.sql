
-- For the movie 'M3', give the username and email of the user who is next on the 
-- waiting list for that movie.

select OrderedList.username, OrderedList.email
from (
  select c1.username, c1.email
  from customer c1
  join waitingList wl on (c1.username = wl.username)
  join media m on (wl.movieid = m.id and m.title = 'M3')
  order by wl.since
  ) OrderedList
where
  rownum = 1
;
