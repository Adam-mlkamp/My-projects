-- 1
Select first_name, last_name, date_format(birthdate,"%M %d, %Y") as 'Sept Birthdays'
from student
where month(birthdate) = 9;

-- 2
select last_name, first_name, floor(datediff("2017-01-05",birthdate)/365) as Years, datediff("2017-01-05" , birthdate)%365 as Days, concat(floor(datediff("2017-01-05",birthdate)/365)," - Yrs, ", datediff("2017-01-05" , birthdate)%365," - Days") as "Years and Days"
from student
order by birthdate;

-- 3 
Select first_name, last_name
from student
JOIN section_has_student
  ON student.student_id = section_has_student.student_id
JOIN section
  ON section_has_student.section_id = section.section_id
JOIN faculty
  ON section.faculty_id = faculty.faculty_id
Where faculty_fname = "John"
order by last_name;

-- 4
Select faculty_fname, faculty_lname
from faculty
JOIN section
  ON section.faculty_id = faculty.faculty_id
join term
  on term.term_id = section.term_id
JOIN section_has_student
  ON section.section_id = section_has_student.section_id
join student
  on student.Student_id = section_has_student.student_id
where student.first_name = "Bryce" and term = "Winter"
order by faculty_lname;

-- 5
Select first_name, last_name
from student
JOIN section_has_student
  ON student.student_id = section_has_student.student_id
JOIN section
  ON section_has_student.section_id = section.section_id
JOIN course
  ON section.course_id = course.course_id
JOIN term
  ON term.term_id = section.term_id
Join department
  on department.department_id = course.department_id
where course_title = "Econometrics" and term = "Fall"
order by last_name;

-- 6
SELECT department.department_code , course_num, course_title
FROM student
JOIN section_has_student
  ON student.student_id = section_has_student.student_id
JOIN section
  ON section_has_student.section_id = section.section_id
JOIN course
  ON section.course_id = course.course_id
JOIN term
  ON term.term_id = section.term_id
Join department
  on department.department_id = course.department_id
Where first_name = "Bryce" and term = "Winter"
order by course_title;

-- 7
SELECT term , year , count(first_name) as Enrollment
FROM student
JOIN section_has_student
  ON student.student_id = section_has_student.student_id
JOIN section
  ON section_has_student.section_id = section.section_id
JOIN course
  ON section.course_id = course.course_id
JOIN term
  ON term.term_id = section.term_id
Join department
  on department.department_id = course.department_id
Where term = "Fall";

-- 8
Select college_name, count(course_title)
from  college c
join department d
  on c.college_id = d.college_id
join course co
  on co.department_id = d.department_id
  group by college_name
  order by college_name;
  
  -- 9
select faculty_fname, faculty_lname, (capacity * count(section_number)) as TeachingCapacity
from faculty f
join section s
  on f.faculty_id = s.faculty_id
join term t
  on t.term_id = s.term_id
where term = "Winter"
group by faculty_fname
order by TeachingCapacity;

-- 10
select last_name, first_name, sum(credit) as Credits
from student s
join section_has_student shs
   on s.student_id = shs.student_id
join section sec
    on sec.section_id = shs.section_id
join course c
   on c.course_id = sec.course_id
join term t
  on sec.term_id = t.term_id
where term = "Fall" 
group by first_name
having sum(credit) >= 3
order by credits desc;




