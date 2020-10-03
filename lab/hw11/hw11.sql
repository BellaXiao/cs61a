CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT A.name, B.size from dogs A, sizes B
  where A.height > B.min
  and A.height <= B.max
  ;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT A.child from parents A, dogs B
  where A.parent = B.name
  order by B.height desc
  ;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT A.child as sib1, B.child as sib2 
  from parents A, parents B
  where A.parent = B.parent
  and A.child < B.child
  ;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT A.sib1 || " and " || A.sib2 || " are " || B1.size || " siblings"
  from siblings A, size_of_dogs B1, size_of_dogs B2
  where A.sib1 = B1.name
  and A.sib2 = B2.name
  and B1.size = B2.size
  ;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT into stacks_helper 
  select name, height, height from dogs order by height;
Insert into stacks_helper
  select A.dogs||", "||B.name, A.stack_height+B.height, B.height
  from stacks_helper A, dogs B
  where A.last_height < B.height;
Insert into stacks_helper
  select A.dogs||", "||B.name, A.stack_height+B.height, B.height
  from stacks_helper A, dogs B
  where A.last_height < B.height;
Insert into stacks_helper
  select A.dogs||", "||B.name, A.stack_height+B.height, B.height
  from stacks_helper A, dogs B
  where A.last_height < B.height;



CREATE TABLE stacks AS
  SELECT dogs, stack_height from stacks_helper
  where stack_height >= 170
  ;
























