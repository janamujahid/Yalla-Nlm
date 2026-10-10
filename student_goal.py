import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456789",       
        database="Yalla_Nlm_db",    
        cursorclass=pymysql.cursors.DictCursor  
    )


def register_student(name, email, password, dob, age):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        "SELECT Student_ID FROM Student WHERE Email = %s",
        (email,)
    )
    if cursor.fetchone():
        print("Account already exists with this email.")
        db.close()
        return None
    query = """
        INSERT INTO Student
        (Student_Name, Email, Password, Date_Of_Birth, Age)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, password, dob, age))
    db.commit()
    student_id = cursor.lastrowid
    db.close()
    print("Account created successfully!")
    return student_id

def login_student(email, password):
    db = get_connection()
    cursor = db.cursor()
    query = "SELECT * FROM Student WHERE Email = %s AND Password = %s;"
    cursor.execute(query, (email, password))
    student = cursor.fetchone() 
    db.close()
    return student

def get_student_profile(student_id):
    db = get_connection()
    cursor = db.cursor()
    query = "SELECT Student_Name, Email, Date_Of_Birth, Age FROM Student WHERE Student_ID = %s;"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    db.close()
    return student


def add_goal(student_id, goal_name, deadline, status='Pending'):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO Goals (Student_ID, Goal_Name, Deadline, Status) VALUES (%s, %s, %s, %s);"
    cursor.execute(query, (student_id, goal_name, deadline, status))
    db.commit()
    db.close()
    return True

def get_student_goals(student_id):
    db = get_connection()
    cursor = db.cursor()
    query = "SELECT Goal_ID, Goal_Name, Deadline, Status FROM Goals WHERE Student_ID = %s ORDER BY Deadline ASC;"
    cursor.execute(query, (student_id))
    goals = cursor.fetchall()
    db.close()
    return goals

def update_goal_status(goal_id, new_status):
    db = get_connection()
    cursor = db.cursor()
    query = "UPDATE Goals SET Status = %s WHERE Goal_ID = %s;"
    cursor.execute(query, (new_status, goal_id))
    db.commit()
    db.close()
    return True

def delete_goal(goal_id):
    db = get_connection()
    cursor = db.cursor()
    query = "DELETE FROM Goals WHERE Goal_ID = %s;"
    cursor.execute(query, (goal_id,))
    db.commit()
    db.close()
    return True