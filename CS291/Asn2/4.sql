
-- For the movie 'M2', list the username of all users who have rented that movie 
-- with a public visibility and if they have rated the movie include the rating 
-- as well.  If they didn't rate the movie a NULL (empty string) should be displayed for rating.

select customer.username, rating
from customer
join rent on (customer.username = rent.username and rent.visibility = 'A')
join media on (rent.movieid = media.id and media.title = 'M2')
left outer join rate on (customer.username = rate.username and rent.movieid = rate.movieid)
;
