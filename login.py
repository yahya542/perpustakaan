import tkinter as tk
from tkinter import messagebox
from mysql.connector import Error
import bcrypt
import pymysql #database

# Fungsi untuk mengecek login
def login():
    username = entry_username.get()
    npm = entry_npm.get()
    password = entry_password.get()
   

    # Koneksi ke database MySQL
    try:
        connection = pymysql.connect(
            host='localhost',  
            user='yahya',      
            password='deya2501',
            database='login_db'  
        )

        cursor = connection.cursor()
        query = "SELECT username, npm, password FROM users WHERE username = %s AND npm= %s"
        cursor.execute(query, (username, npm))
        result = cursor.fetchone()

        if result:
            stored_username, stored_npm, stored_password = result

            # Verifikasi password menggunakan bcrypt
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                messagebox.showinfo("Login Success", "Login Berhasil!")
            else:
                messagebox.showerror("Login Failed", "Username atau password salah.")
        else:
            messagebox.showerror("Login Failed", "Username tidak ditemukan.")
        
    except Error as d:
        messagebox.showerror("Error", f"Terjadi error: {d}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Setup form login
root = tk.Tk()
root.title("Form Login")

# Username Label & Entry
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Username Label & Entry
label_npm = tk.Label(root, text="npm")
label_npm.pack(pady=5)
entry_npm = tk.Entry(root)
entry_npm.pack(pady=5)


# Password Label & Entry
label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Button Login
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Start GUI
root.mainloop()
