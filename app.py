from flask import Flask, render_template  # 🔴 นำเข้า Flask และฟังก์ชันสำหรับแสดง HTML
from db import get_connection  # 🔴 นำเข้าฟังก์ชันเชื่อมต่อ MySQL จาก db.py

app = Flask(__name__)  # 🔴 สร้าง Flask App

@app.route("/")  # 🔴 สร้าง route สำหรับหน้าแรก
def index():
    conn = get_connection()  # 🔴 เชื่อมต่อฐานข้อมูล
    cursor = conn.cursor()  # 🔴 สร้าง cursor เพื่อรันคำสั่ง SQL
    cursor.execute("SELECT PN, Name, Price1, SUnit FROM product LIMIT 100")  # 🔴 ดึงข้อมูลสินค้า 100 รายการ
    products = cursor.fetchall()  # 🔴 เก็บผลลัพธ์ทั้งหมดไว้ในตัวแปร
    conn.close()  # 🔴 ปิด connection
    return render_template("index.html", products=products)  # 🔴 ส่งข้อมูลไปที่ template HTML

if __name__ == "__main__":  # 🔴 ถ้ารันไฟล์นี้โดยตรง
    app.run(host="0.0.0.0", port=5000, debug=True)  # 🔴 เปิด Web Server บนทุก IP (เข้าผ่าน LAN ได้)