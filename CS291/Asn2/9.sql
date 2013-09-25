
-- Use the view MoviePopularity defined above to find the most popular movie in 
-- each genre

select m1.genre, media.title
from movie m1
join moviepopularity mp using (mid)
join media on (mid = media.id)
where
  mp.popularity = (
    select max(mp2.popularity)
    from movie m2
    join moviepopularity mp2 using (mid)
    where
      m1.genre = m2.genre
  )
;
