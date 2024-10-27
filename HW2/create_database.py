import mysql.connector
from mysql.connector import Error

def create_database_and_tables():
    try:
        # 連接到 MySQL 伺服器
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ruby2302"  # 替換為你的 MySQL 密碼
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            # 建立資料庫
            cursor.execute("CREATE DATABASE IF NOT EXISTS user_data")
            cursor.execute("USE user_data")

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

            # 建立 Appointment 表格，並加入外鍵
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

            print("資料庫和表格已成功建立。")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL 連線已關閉。")

# 執行建立資料庫和表格的函式
if __name__ == "__main__":
    create_database_and_tables()
