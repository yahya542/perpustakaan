
import os
import pymysql
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Mengubah warna latar belakang terminal
def set_terminal_color():
    os.system('color F1')

def reset_terminal_color():
    os.system('color')  # Mengatur ulang ke warna default

# Inisialisasi console
console = Console()

def koneksi_db():
    try:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="deya2501",
            database="perpustakaan"
        )
    except pymysql.MySQLError as e:
        console.print(f"Kesalahan koneksi database: {e}", style="red")
        return None

def tambah_buku(judul, penulis, tahun_terbit):
    db = koneksi_db()
    if db is None:
        return
    try:
        cursor = db.cursor()
        sql = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
        cursor.execute(sql, (judul, penulis, tahun_terbit))
        db.commit()
        console.print("Buku berhasil ditambahkan!", style="white on blue")
    except pymysql.MySQLError as e:
        console.print(f"Kesalahan saat menambahkan buku: {e}", style="red")
    finally:
        cursor.close()
        db.close()

def tampilkan_buku():
    db = koneksi_db()
    if db is None:
        return
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM buku")
        
        table = Table(title="Daftar Buku")
        table.add_column("ID", style="cyan", header_style="bold cyan")
        table.add_column("Judul", style="magenta", header_style="bold magenta")
        table.add_column("Penulis", style="green", header_style="bold green")
        table.add_column("Tahun Terbit", style="blue", header_style="bold blue")

        for buku in cursor.fetchall():
            table.add_row(str(buku[0]), buku[1], buku[2], str(buku[3]))

        # Menggunakan Panel untuk mengatur latar belakang menjadi putih
        console.print(Panel(table, style="white"))  # Panel dengan latar belakang putih
    except pymysql.MySQLError as e:
        console.print(f"Kesalahan saat mengambil buku: {e}", style="red")
    finally:
        cursor.close()
        db.close()

def hapus_buku(buku_id):
    db = koneksi_db()
    if db is None:
        return
    try:
        cursor = db.cursor()
        sql = "DELETE FROM buku WHERE id = %s"
        cursor.execute(sql, (buku_id,))
        db.commit()
        console.print("Buku berhasil dihapus!", style="white on blue")
    except pymysql.MySQLError as e:
        console.print(f"Kesalahan saat menghapus buku: {e}", style="red")
    finally:
        cursor.close()
        db.close()
def main():
    set_terminal_color() 
    try:
        while True:
            console.print("\n\t\tAplikasi Perpustakaan\t", style="black on yellow")
            console.print("\t1. Tambah Buku\t\t", style="white on blue")
            console.print("\t2. Tampilkan Buku\t", style="white on blue")
            console.print("\t3. Hapus Buku\t\t", style="white on blue")
            console.print("\t4. Keluar\t\t", style="white on blue")
            
            # Menggunakan Prompt untuk mendapatkan input dengan latar belakang khusus
            pilihan = Prompt.ask("Pilih opsi:", style="white on blue", background="black")

            if pilihan == '1':
                judul = Prompt.ask("Masukkan judul buku:", style="white on blue", background="black")
                penulis = Prompt.ask("Masukkan penulis buku:", style="white on blue", background="black")
                tahun_terbit = Prompt.ask("Masukkan tahun terbit:", style="white on blue", background="black")
                tambah_buku(judul, penulis, tahun_terbit)
            elif pilihan == '2':
                tampilkan_buku()
            elif pilihan == '3':
                buku_id = Prompt.ask("Masukkan ID buku yang ingin dihapus:", style="white on blue", background="black")
                hapus_buku(buku_id)  
            elif pilihan == '4':
                console.print("Keluar dari aplikasi.", style="white on blue")
                break
            else:
                console.print("Pilihan tidak valid.", style="white on blue")
    finally:
        reset_terminal_color()  # Kembalikan warna saat keluar
