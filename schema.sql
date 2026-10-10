CREATE DATABASE IF NOT EXISTS Yalla_Nlm_db;
USE Yalla_Nlm_db;


CREATE TABLE Student (
    Student_ID INT AUTO_INCREMENT PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Date_Of_Birth DATE,
    Age INT
);


CREATE TABLE Subject (
    Subject_ID INT AUTO_INCREMENT PRIMARY KEY,
    Student_ID INT NOT NULL,
    Subject_Name VARCHAR(100) NOT NULL,
    Description TEXT,
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID) ON DELETE CASCADE
);


CREATE TABLE Goals (
    Goal_ID INT AUTO_INCREMENT PRIMARY KEY,
    Student_ID INT NOT NULL,
    Goal_Name VARCHAR(150) NOT NULL,
    Deadline DATE,
    Status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID) ON DELETE CASCADE
);


CREATE TABLE Study_Session (
    Session_id INT AUTO_INCREMENT PRIMARY KEY,
    Subject_ID INT NOT NULL,
    Session_date DATE NOT NULL,
    Duration INT NOT NULL, 
    Notes TEXT,
    FOREIGN KEY (Subject_ID) REFERENCES Subject(Subject_ID) ON DELETE CASCADE
);

CREATE TABLE Tasks (
    Task_id INT AUTO_INCREMENT PRIMARY KEY,
    Subject_ID INT NOT NULL,
    Task_title VARCHAR(150) NOT NULL,
    Description TEXT,
    Due_date DATE,
    Status VARCHAR(50) DEFAULT 'Pending',
    Priority VARCHAR(20) DEFAULT 'Medium',
    FOREIGN KEY (Subject_ID) REFERENCES Subject(Subject_ID) ON DELETE CASCADE
);


CREATE TABLE Exam (
    Exam_ID INT AUTO_INCREMENT PRIMARY KEY,
    Subject_ID INT NOT NULL,
    Exam_Date DATE NOT NULL,
    Title VARCHAR(150) NOT NULL,
    Notes TEXT,
    FOREIGN KEY (Subject_ID) REFERENCES Subject(Subject_ID) ON DELETE CASCADE
);


-- SET FOREIGN_KEY_CHECKS = 0;

-- TRUNCATE TABLE Study_Session;
-- TRUNCATE TABLE Exam;
-- TRUNCATE TABLE Tasks;
-- TRUNCATE TABLE Subject;
-- TRUNCATE TABLE Student;

-- SET FOREIGN_KEY_CHECKS = 1;


-- SELECT * FROM student
-- SELECT * FROM subject
-- SELECT * FROM study_session
-- SELECT * FROM exam
-- SELECT * FROM tasks
-- SELECT * FROM goals