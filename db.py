import pymysql  # 🔴 ใช้เชื่อมต่อ MySQL ด้วยไลบรารี pymysql

def get_connection():
    return pymysql.connect(  # 🔴 สร้างและส่งคืน connection object
        host="118.172.199.229",     # 🔴 ชื่อเซิร์ฟเวอร์ (localhost ถ้าอยู่เครื่องเดียวกัน)
        user="root",          # 🔴 ชื่อผู้ใช้ MySQL (ค่าเริ่มต้นมักเป็น root)
        password="",          # 🔴 รหัสผ่าน MySQL (ถ้าไม่มีให้เว้นว่าง)
        database="newstock",  # 🔴 ชื่อฐานข้อมูล MySQL ที่ sync ข้อมูลไว้
        charset="utf8mb4",    # 🔴 รองรับภาษาไทย
        cursorclass=pymysql.cursors.DictCursor  # 🔴 ให้ผลลัพธ์ออกมาเป็น dict (ใช้ key ได้)
        Update db.py with public IP for Render connection

        
    )
