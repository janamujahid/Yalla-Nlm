import pymysql
from datetime import date

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456789",       
        database="Yalla_Nlm_db",    
        cursorclass=pymysql.cursors.DictCursor  
    )


def add_subject(student_id, subject_name, description=""):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO Subject (Student_ID, Subject_Name, Description) VALUES (%s, %s, %s);"
    cursor.execute(query, (student_id, subject_name, description))
    db.commit()
    db.close()
    return True

def get_student_subjects(student_id):
    db = get_connection()
    cursor = db.cursor()
    query = "SELECT Subject_ID, Subject_Name, Description FROM Subject WHERE Student_ID = %s;"
    cursor.execute(query, (student_id,))
    subjects = cursor.fetchall()
    db.close()
    return subjects


def update_subject(subject_id, subject_name, description):
    db = get_connection()
    cursor = db.cursor()
    query = "UPDATE Subject SET Subject_Name = %s, Description = %s WHERE Subject_ID = %s;"
    cursor.execute(query, (subject_name, description, subject_id))
    db.commit()
    db.close()
    return True

def delete_subject(subject_id):
    db = get_connection()
    cursor = db.cursor()
    query = "DELETE FROM Subject WHERE Subject_ID = %s;"
    cursor.execute(query, (subject_id,))
    db.commit()
    db.close()
    return True

def search_subject(student_id, search_name):
    db = get_connection()
    cursor = db.cursor()
    query = "SELECT Subject_ID, Subject_Name, Description FROM Subject WHERE Student_ID = %s AND Subject_Name LIKE %s;"
    cursor.execute(query, (student_id, f"%{search_name}%"))
    subjects = cursor.fetchall()
    db.close()
    return subjects


def log_study_session(subject_id, session_date, duration, notes=""):
    db = get_connection()
    cursor = db.cursor()
    query = """
        INSERT INTO Study_Session (Subject_ID, Session_date, Duration, Notes)
        VALUES (%s, %s, %s, %s);
    """
    cursor.execute(query, (subject_id, session_date, duration, notes))
    db.commit()
    db.close()
    return True

def view_session_history(subject_id):
    db = get_connection()
    cursor = db.cursor()
    query = """
        SELECT Session_id, Session_date, Duration, Notes 
        FROM Study_Session 
        WHERE Subject_ID = %s
        ORDER BY Session_date DESC;
    """
    cursor.execute(query, (subject_id,))
    
    sessions = cursor.fetchall()
    db.close()
    return sessions

def get_total_study_hours_for_student(student_id):
    db = get_connection()
    cursor = db.cursor()
    query = """
        SELECT SUM(s.Duration) AS total_minutes
        FROM Study_Session s
        JOIN Subject sub ON s.Subject_ID = sub.Subject_ID
        WHERE sub.Student_ID = %s;
    """
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    db.close()
    
    total_minutes = result['total_minutes'] if result and result['total_minutes'] else 0
    return round(total_minutes / 60, 2)

def check_if_student_studied_today(student_id):
    db = get_connection()
    cursor = db.cursor()
    today = date.today()
    query = """
        SELECT COUNT(*) as count
        FROM Study_Session s
        JOIN Subject sub ON s.Subject_ID = sub.Subject_ID
        WHERE sub.Student_ID = %s AND s.Session_date = %s;
    """
    cursor.execute(query, (student_id, today))
    result = cursor.fetchone()
    db.close()
    return result['count'] > 0 if result else False
