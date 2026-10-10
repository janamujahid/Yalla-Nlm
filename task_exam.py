import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456789",       
        database="Yalla_Nlm_db",    
        cursorclass=pymysql.cursors.DictCursor  
    )



def add_task(subject_id, task_title, description="", due_date=None, priority='Medium'):
    db = get_connection()
    cursor = db.cursor()
    query = """
        INSERT INTO Tasks (Subject_ID, Task_title, Description, Due_date, Status, Priority)
        VALUES (%s, %s, %s, %s, 'Pending', %s);
    """
    cursor.execute(query, (subject_id, task_title, description, due_date, priority))
    db.commit()
    db.close()
    return True

def view_tasks_by_subject(subject_id):
    db = get_connection()
    cursor = db.cursor()
    query = """
        SELECT Task_id, Task_title, Description, Due_date, Status, Priority 
        FROM Tasks 
        WHERE Subject_ID = %s
        ORDER BY Due_date ASC;
    """
    cursor.execute(query, (subject_id,))
    tasks = cursor.fetchall()
    db.close()
    return tasks

def mark_task_completed(task_id):
    db = get_connection()
    cursor = db.cursor()
    query = "UPDATE Tasks SET Status = 'Completed' WHERE Task_id = %s;"
    cursor.execute(query, (task_id,))
    db.commit()
    db.close()
    return True

def delete_task(task_id):
    db = get_connection()
    cursor = db.cursor()
    query = "DELETE FROM Tasks WHERE Task_id = %s;"
    cursor.execute(query, (task_id,))
    db.commit()
    db.close()
    return True


def add_exam(subject_id, title, exam_date, notes=""):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO Exam (Subject_ID, Title, Exam_Date, Notes) VALUES (%s, %s, %s, %s);"
    cursor.execute(query, (subject_id, title, exam_date, notes))
    db.commit()
    db.close()
    return True

def get_student_exams(student_id):
    db = get_connection()
    cursor = db.cursor()
    query = """
        SELECT Exam.Exam_ID, Exam.Title, Exam.Exam_Date, Exam.Notes, Subject.Subject_Name
        FROM Exam
        JOIN Subject ON Exam.Subject_ID = Subject.Subject_ID
        WHERE Subject.Student_ID = %s
        ORDER BY Exam.Exam_Date ASC;
    """
    cursor.execute(query, (student_id,))
    exams = cursor.fetchall()
    db.close()
    return exams

def delete_exam(exam_id):
    db = get_connection()
    cursor = db.cursor()
    query = "DELETE FROM Exam WHERE Exam_ID = %s;"
    cursor.execute(query, (exam_id,))
    db.commit()
    db.close()
    return True