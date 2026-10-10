from datetime import date
from student_goal import register_student, login_student, add_goal, get_student_goals, update_goal_status, delete_goal
from subject_session import add_subject, get_student_subjects, search_subject, delete_subject, log_study_session, view_session_history, get_total_study_hours_for_student
from task_exam import add_task, view_tasks_by_subject, mark_task_completed, delete_task, add_exam, get_student_exams, delete_exam

def menu(title, options):
    print(f"\n--- {title.upper()} ---")
    for k, v in options.items():
        print(f"{k}. {v}")
    return input("\nSelect: ").strip()

def auth_menu():
    opt = menu("Welcome to Yalla Nlm", {"1": "Login", "2": "Register", "3": "Exit"})
    if opt == '1':
        user = login_student(input("Email: "), input("Password: "))
        if user: print(f"\nWelcome, {user['Student_Name']}!")
        else: print("\nInvalid credentials.")
        return user
    elif opt == '2':
        args = [input(f"{f}: ") for f in ["Name", "Email", "Password", "DOB (YYYY-MM-DD)", "Age"]]
        print("Registered successfully!" if register_student(*args) else "Failed.")
    elif opt == '3':
        exit()

def manage_subjects(sid):
    opt = menu("Subjects", {"1": "View", "2": "Add", "3": "Search", "4": "Delete"})
    if opt == '1':
        for s in get_student_subjects(sid): print(f"[{s['Subject_ID']}] {s['Subject_Name']}: {s['Description']}")
    elif opt == '2':
        add_subject(sid, input("Name: "), input("Desc: "))
    elif opt == '3':
        for s in search_subject(sid, input("Search: ")): print(f"[{s['Subject_ID']}] {s['Subject_Name']}")
    elif opt == '4':
        delete_subject(input("Subject ID: "))

def manage_sessions(sid):
    opt = menu("Study Sessions", {"1": "Log Session", "2": "History"})
    if opt == '1':
        log_study_session(int(input("Subject ID: ")), date.today(), int(input("Minutes: ")), input("Notes: "))
    elif opt == '2':
        for s in view_session_history(int(input("Subject ID: "))):
            print(f"Date: {s['Session_date']} | Duration: {s['Duration']} mins | Notes: {s['Notes']}")

def manage_goals(sid):
    opt = menu("Goals", {"1": "View", "2": "Add", "3": "Update Status", "4": "Delete"})
    if opt == '1':
        for g in get_student_goals(sid): print(f"[{g['Goal_ID']}] {g['Goal_Name']} ({g['Deadline']}) -> {g['Status']}")
    elif opt == '2':
        add_goal(sid, input("Goal: "), input("Deadline (YYYY-MM-DD): "))
    elif opt == '3':
        update_goal_status(int(input("Goal ID: ")), input("Status: "))
    elif opt == '4':
        delete_goal(int(input("Goal ID: ")))

def manage_tasks(sid):
    opt = menu("Tasks", {"1": "View", "2": "Add", "3": "Complete", "4": "Delete"})
    if opt == '1':
        for t in view_tasks_by_subject(int(input("Subject ID: "))):
            print(f"[{t['Task_id']}] {t['Task_title']} | Priority: {t['Priority']} | Status: {t['Status']}")
    elif opt == '2':
        add_task(int(input("Subject ID: ")), input("Title: "), input("Desc: "), input("Due (YYYY-MM-DD): ") or None, input("Priority: ") or 'Medium')
    elif opt == '3':
        mark_task_completed(int(input("Task ID: ")))
    elif opt == '4':
        delete_task(int(input("Task ID: ")))

def manage_exams(sid):
    opt = menu("Exams", {"1": "View", "2": "Schedule", "3": "Delete"})
    if opt == '1':
        for e in get_student_exams(sid): print(f"[{e['Exam_ID']}] {e['Title']} ({e['Subject_Name']}) on {e['Exam_Date']}")
    elif opt == '2':
        add_exam(int(input("Subject ID: ")), input("Title: "), input("Date (YYYY-MM-DD): "), input("Notes: "))
    elif opt == '3':
        delete_exam(int(input("Exam ID: ")))

def main():
    student = None
    actions = {"1": manage_subjects, "2": manage_sessions, "3": manage_goals, "4": manage_tasks, "5": manage_exams}
    
    while True:
        if not student:
            student = auth_menu()
        else:
            sid = student['Student_ID']
            print(f"\n=== DASHBOARD ({student['Student_Name']}) | Total Hours: {get_total_study_hours_for_student(sid)} hrs ===")
            opt = menu("Main Menu", {"1": "Subjects", "2": "Sessions", "3": "Goals", "4": "Tasks", "5": "Exams", "6": "Logout"})
            if opt in actions:
                actions[opt](sid)
            elif opt == '6':
                student = None

if __name__ == "__main__":
    main()