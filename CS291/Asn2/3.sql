
-- Find the users that have bought all media that customer 'c1' bought with a 
-- visibility set to friends only.

select distinct c2.username
from customer c2
where
  not exists(
    -- the set of all F purchases made by c1
    (select m1.id
    from media m1
    join buy b1 on (m1.id = b1.mediaid and b1.visibility = 'F' and b1.username = 'c1')
    )
    minus
    -- the set of all purchases made by c2
    (select m2.id
    from media m2
    join buy b2 on (m2.id = b2.mediaid)
    where
      b2.username = c2.username
    )
  )
;
