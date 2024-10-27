import mysql.connector

# 設定資料庫連線
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ruby2302",  # 替換為你的 MySQL 密碼
        database="user_data"
    )

# 建立資料表
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 建立 Patient 表格
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patient (
            patient_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT
        )
    """)

    # 建立 Doctor 表格
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Doctor (
            doctor_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            specialization VARCHAR(100)
        )
    """)

    # 建立 Appointment 表格，關聯 Patient 和 Doctor
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Appointment (
            appointment_id INT AUTO_INCREMENT PRIMARY KEY,
            patient_id INT,
            doctor_id INT,
            appointment_date DATE,
            diagnosis VARCHAR(255),
            FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
            FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

# 執行建立表格
if __name__ == "__main__":
    create_tables()
