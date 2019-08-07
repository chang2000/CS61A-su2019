.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest limit 20;

CREATE TABLE matchmaker AS
  SELECT stu_1.pet, stu_1.song, stu_1.color, stu_2.color
    FROM students AS stu_1, students AS stu_2
    WHERE stu_1.pet = stu_2.pet AND stu_1.song = stu_2.song AND stu_1.time < stu_2.time;

CREATE TABLE smallest_int_having AS
  SELECT time, smallest
    FROM students
    GROUP BY smallest HAVING COUNT(smallest) = 1;

