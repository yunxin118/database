from flask import Blueprint, render_template
import mysql.connector

join_blueprint = Blueprint("join_blueprint", __name__)

# 連接 MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ruby2302",
        database="user_data"
    )

# 聯結查詢，顯示預約詳細資料
@join_blueprint.route("/join")
def join_results():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT Appointment.appointment_id, Patient.name AS patient_name, Doctor.name AS doctor_name,
               Doctor.specialization, Appointment.appointment_date, Appointment.diagnosis
        FROM Appointment
        JOIN Patient ON Appointment.patient_id = Patient.patient_id
        JOIN Doctor ON Appointment.doctor_id = Doctor.doctor_id
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("appointments_results.html", results=results)
