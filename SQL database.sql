-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema University
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `University` ;

-- -----------------------------------------------------
-- Schema University
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `University` DEFAULT CHARACTER SET utf8 ;
USE `University` ;

-- -----------------------------------------------------
-- Table `University`.`college`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `University`.`college` ;

CREATE TABLE IF NOT EXISTS `University`.`college` (
  `college_id` INT NOT NULL,
  `college_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`college_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `University`.`department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `University`.`department` ;

CREATE TABLE IF NOT EXISTS `University`.`department` (
  `department_id` INT NOT NULL,
  `department_name` VARCHAR(50) NOT NULL,
  `department_code` VARCHAR(4) NOT NULL,
  `college_id` INT NOT NULL,
  PRIMARY KEY (`department_id`),
  INDEX `fk_department_college1_idx` (`college_id` ASC) VISIBLE,
  CONSTRAINT `fk_department_college1`
    FOREIGN KEY (`college_id`)
    REFERENCES `University`.`college` (`college_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `University`.`Student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `University`.`Student` ;

CREATE TABLE IF NOT EXISTS `University`.`Student` (
  `Student_id` INT NOT NULL,
  `first_name` VARCHAR(25) NOT NULL,
  `last_name` VARCHAR(25) NOT NULL,
  `gender` ENUM("M", "F") NOT NULL,
  `city` VARCHAR(30) NOT NULL,
  `State` VARCHAR(2) NOT NULL,
  `birthdate` DATE NOT NULL,
  PRIMARY KEY (`Student_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `University`.`course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `University`.`course` ;

CREATE TABLE IF NOT EXISTS `University`.`course` (
  `course_id` INT NOT NULL,
  `credit` INT NOT NULL,
  `course_title` VARCHAR(45) NOT NULL,
  `department_id` INT NOT NULL,
  `course_num` VARCHAR(3) NOT NULL,
  PRIMARY KEY (`course_id`),
  INDEX `fk_course_department1_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `fk_course_department1`
    FOREIGN KEY (`department_id`)
    REFERENCES `University`.`department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `University`.`term`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `University`.`term` ;

CREATE TABLE IF NOT EXISTS `University`.`term` (
  `term_id` INT NOT NULL,
  `year` YEAR NOT NULL,
  `term` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`term_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `University`.`faculty`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `University`.`faculty` ;

CREATE TABLE IF NOT EXISTS `University`.`faculty` (
  `faculty_id` INT NOT NULL,
  `faculty_fname` VARCHAR(15) NOT NULL,
  `faculty_lname` VARCHAR(20) NOT NULL,
  `capacity` INT NOT NULL,
  PRIMARY KEY (`faculty_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `University`.`section`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `University`.`section` ;

CREATE TABLE IF NOT EXISTS `University`.`section` (
  `section_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `term_id` INT NOT NULL,
  `section_number` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  PRIMARY KEY (`section_id`),
  INDEX `fk_section_course1_idx` (`course_id` ASC) VISIBLE,
  INDEX `fk_section_term1_idx` (`term_id` ASC) VISIBLE,
  INDEX `fk_section_faculty1_idx` (`faculty_id` ASC) VISIBLE,
  CONSTRAINT `fk_section_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `University`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_term1`
    FOREIGN KEY (`term_id`)
    REFERENCES `University`.`term` (`term_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_faculty1`
    FOREIGN KEY (`faculty_id`)
    REFERENCES `University`.`faculty` (`faculty_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `University`.`section_has_Student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `University`.`section_has_Student` ;

CREATE TABLE IF NOT EXISTS `University`.`section_has_Student` (
  `section_id` INT NOT NULL,
  `Student_id` INT NOT NULL,
  PRIMARY KEY (`section_id`, `Student_id`),
  INDEX `fk_section_has_Student_Student1_idx` (`Student_id` ASC) VISIBLE,
  INDEX `fk_section_has_Student_section_idx` (`section_id` ASC) VISIBLE,
  CONSTRAINT `fk_section_has_Student_section`
    FOREIGN KEY (`section_id`)
    REFERENCES `University`.`section` (`section_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_has_Student_Student1`
    FOREIGN KEY (`Student_id`)
    REFERENCES `University`.`Student` (`Student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



-- Insert for College
insert into college values
	(1,"College of Physical Science and Engineering"),
    (2,"College of Business and Communication"),
    (3,"College of Language and Letters");

-- Insert for Faculty
insert into faculty values
	(1,"Marty","Morring",30),
    (2,"Nate","Norris",50),
    (3,"Ben","Barrus",35),
    (4,"John","Jensen",30),
    (5,"Bill","Barney",35);
    
-- Insert for Student
insert into student values
	(1,"Paul","Miller", "M", "Dallas", "TX","1996-02-22"),
	(2,"Katie","Smith", "F", "Provo", "UT","1995-07-22"),
	(3,"Kelly","Jones", "F", "Provo", "UT","1998-06-22"),
	(4,"Devon","Merrill", "M", "Mesa", "AZ","2000-07-22"),
	(5,"Mandy", "Murdock", "F", "Topeka", "KS","1996-11-22"),
	(6,"Alece", "Adams", "F", "Rigby", "ID","1997-05-22"),
	(7,"Bryce", "Carlson", "M", "Bozeman", "MT","1997-11-22"),
	(8,"Preston", "Larsen", "M", "Decatur", "TN","1996-09-22"),
	(9,"Julia", "Madsen", "F", "Rexburg", "ID","1998-09-22"),
	(10,"Susan", "Sorensen", "F", "Mesa", "AZ","1998-08-09");
    
-- Insert for term values
insert into term values
	(1,2019,"Fall"),
    (2,2018,"Winter");

-- Insert into department
insert into department values
	(1,"Computer Information Technology","CIT",1),
    (2,"Economics","ECON",2),
    (3,"Humanities and Philosophy","HUM",3);
    
-- Insert into course
insert into course values
	(1,3,"Intro to Databases",1,"111"),
    (2,4,"Econometrics",2,"388"),
    (3,3,"Micro Economics",2,"150"),
    (4,2,"Classical Heritage",3,"376");
    
-- Insert for Section
insert into section values
	(1,1,1,1,1),  -- Marty 
    (2,3,1,1,2),  -- Nate
    (3,3,1,2,2), -- Nate
    (4,2,1,1,3), -- Ben
    (5,4,1,1,4), -- John
    (6,1,2,2,1), -- Marty
    (7,1,2,3,5),  -- Bill
    (8,3,2,1,2),  -- Nate
    (9,3,2,2,2), -- Nate
    (10,4,2,1,4); -- John
    
-- Insert for Section_has_students
insert into section_has_student values
	(7,6),
	(6,7),
	(8,7),
	(10,7),
	(5,4),
	(9,9),
	(4,2),
	(4,3),
	(4,5),
	(5,5),
	(1,1),
	(3,1),
	(9,8),
	(6,10);

