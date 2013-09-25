
-- Given a customer 'c1', list his/her indirect friends exactly 2 links away. 
-- For instance, if A is friends with B and B is friends with C, then A is a 2 
-- links away indirect friend with C.

select distinct c1.username
from customer c2
join customer c1 on (c1.username != 'c1')
join customer c3 on (c3.username = 'c1')
join friend f1 on (f1.user1 in (c1.username, c2.username) and f1.user2 in (c1.username, c2.username))
join friend f2 on (f2.user1 in (c2.username, 'c1') and f2.user2 in (c2.username, 'c1'))
where
  not exists(
    select c3.username
    from friend f3
    where
      c1.username in(f3.user1, f3.user2) and
      c3.username in(f3.user1, f3.user2))
;

