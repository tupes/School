
-- Write and update statement that changes all rent modes from short term to 
-- long term if more than 7 days have passed since the movie was rented.

update rent
set rent.rentmode = 'L'
where 
  rent.rentmode = 'S' and
  sysdate - rent.since > 7
;
