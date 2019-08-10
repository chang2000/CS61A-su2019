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
  SELECT d.name, s.size
    FROM dogs AS d, sizes AS s
    WHERE s.min < d.height AND d.height <= s.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d1.name
    FROM parents AS p, dogs AS d1, dogs as d2
    WHERE d1.name = p.child AND p.parent = d2.name ORDER BY d2.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT d1.name as dog1, d2.name as dog2
    from dogs as d1, dogs as d2, parents as p1, parents as p2
    where d1.name = p1.child and d2.name = p2.child and p1.parent = p2.parent
    and d1.name < d2.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT sib.dog1 ||" and "|| sib.dog2 ||" are "|| s1.size || " siblings"
    from siblings as sib, sizes as s1, sizes as s2, dogs as d1, dogs as d2
    where sib.dog1 = d1.name and sib.dog2 = d2.name and
        s1.min < d1.height and d1.height <= s1.max and
        s2.min < d2.height and d2.height <= s2.max
        and s1.size = s2.size ORDER BY d1.name DESC;

-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT d1.fur AS furr, sum(d1.height) AS summ
    FROM dogs AS d1
    -- WHERE d1.height < AVG(*)
    GROUP BY d1.fur
    HAVING d1.height < 1.3 * avg(d1.height) and d1.height > 0.7 * avg(d1.height)
    ;
