from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ruby2302",  # 替換為你的 MySQL 密碼
        database="user_data"
    )

# 根路由，將根目錄導向到 /appointments
@app.route('/')
def index():
    return redirect(url_for('appointments'))

@app.route('/appointments')
def appointments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT Appointment.appointment_id, Patient.name AS patient_name, Doctor.name AS doctor_name,
               Doctor.specialization, Appointment.appointment_date, Appointment.diagnosis
        FROM Appointment
        JOIN Patient ON Appointment.patient_id = Patient.patient_id
        JOIN Doctor ON Appointment.doctor_id = Doctor.doctor_id
    """
    cursor.execute(query)
    appointments = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('appointments.html', appointments=appointments)

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    patient_name = request.form['patient_name']
    doctor_name = request.form['doctor_name']
    specialization = request.form['specialization']
    appointment_date = request.form['appointment_date']
    diagnosis = request.form.get('diagnosis')

    conn = get_db_connection()
    cursor = conn.cursor()

    # 插入新的患者
    cursor.execute("INSERT INTO Patient (name) VALUES (%s)", (patient_name,))
    patient_id = cursor.lastrowid

    # 插入新的醫生
    cursor.execute("INSERT INTO Doctor (name, specialization) VALUES (%s, %s)", (doctor_name, specialization))
    doctor_id = cursor.lastrowid

    # 插入預約
    cursor.execute("""
        INSERT INTO Appointment (patient_id, doctor_id, appointment_date, diagnosis)
        VALUES (%s, %s, %s, %s)
    """, (patient_id, doctor_id, appointment_date, diagnosis))
    
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('appointments'))

@app.route('/delete_appointment', methods=['POST'])
def delete_appointment():
    appointment_id = request.form['appointment_id']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Appointment WHERE appointment_id = %s", (appointment_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('appointments'))

if __name__ == '__main__':
    app.run(debug=True)
