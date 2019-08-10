.read lab13.sql

CREATE TABLE su19favpets AS
  SELECT pet, count(*)
    from students
    group by pet order by count(pet) limit 10;


CREATE TABLE su19dog AS
  SELECT pet, count(*) AS count
    FROM students
    WHERE pet='dog' GROUP BY pet;


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) as count
    FROM students
    WHERE seven='7' GROUP BY instructor;
