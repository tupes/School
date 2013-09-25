
-- Given a customer 'c1', list all of his/her friends.

select distinct username
from friend
join customer on (
  username != 'c1' and
  user1 in ('c1', username) and 
  user2 in ('c1', username))
;
