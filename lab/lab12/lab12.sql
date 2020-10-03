.read fa18data.sql

-- Q2
CREATE TABLE obedience AS
  SELECT seven, denero from students;

-- Q3
CREATE TABLE smallest_int AS
  SELECT time, smallest from students
  where smallest > 13
  order by smallest
  limit 20
  ;

-- Q4
CREATE TABLE matchmaker AS
  SELECT A.pet, A.song, A.color, B.color
  from students A, students B
  where A.time < B.time
  and A.pet = B.pet
  and A.song = B.song


  ;
