
-- Create a view called MoviePopularity that has two columns: 'mid'(the movie id) 
-- and 'popularity'. The value of attribute 'popularity' is obtained by taking the 
-- total number of (distinct) users who have bought or rented the movie.

drop view MoviePopularity;

create view MoviePopularity(mid, popularity) as
  select movie.mid, count(distinct customer.username)
  from movie, customer, buy, rent
  where
    (customer.username = buy.username and
    buy.mediaid = movie.mid)
    or
    (customer.username = rent.username and
    rent.movieid = movie.mid)
  group by movie.mid
;
