import os
import pymysql #database
from rich.console import Console #rich keseluruhan
from rich.table import Table #table
from rich.prompt import Prompt #ganti input
from rich.text import Text #text


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
2
def tambah_buku(judul, penulis, tahun_terbit):
    db = koneksi_db()
    if db is None:
        return
    try:
        cursor = db.cursor()
        sql = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
        cursor.execute(sql, (judul, penulis, tahun_terbit))
        db.commit()
        console.print("\n Buku berhasil ditambahkan!", style="white on green")
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
        
        print()
        table = Table( style="black on yellow ")  # Tabel dengan latar belakang putih
        table.add_column("ID", style="cyan", header_style="bold white on cyan")  # Gaya header
        table.add_column("Judul", style="magenta", header_style="bold white on magenta")  # Gaya header
        table.add_column("Penulis", style="green", header_style="bold white on green")  # Gaya header
        table.add_column("Tahun Terbit", style="blue", header_style="bold white on blue")  # Gaya header

        for buku in cursor.fetchall():
            table.add_row(str(buku[0]), buku[1], buku[2], str(buku[3]))

        # Panel untuk membungkus tabel
        console.print(table, style="white")  # Panel dengan latar belakang putih
    except pymysql.MySQLError as d:
        console.print(f"Kesalahan saat mengambil buku: {del}", style="red")
    


def hapus_buku(buku_id):
    db = koneksi_db()
    if db is None:
        return
    try:
        cursor = db.cursor()
        sql = "DELETE FROM buku WHERE id = %s"
        cursor.execute(sql, (buku_id,))
        db.commit()

        #cek id
        if cursor.rowcount > 0:
            console.print("Buku berhasil dihapus!", style="black on green")
        else : 
            console.print("id buku tidak tersedia!", style="black on red")

    except pymysql.MySQLError as e:
        console.print(f"Kesalahan saat menghapus buku: {e}", style="red")
    finally:
        cursor.close()
        db.close()

def main():
    # try:
    while True:
       
        console.print("\n\tAplikasi Perpustakaan\t\t", style=" bold black on yellow")
        console.print("\t1. Tambah Stok Buku\t\t", style="white on blue")
        console.print("\t2. Tampilkan Buku\t\t", style="white on blue")
        console.print("\t3. Hapus Buku\t\t\t", style="white on blue")
        console.print("\t4. Keluar\t\t\t", style="white on blue")
        pilihan = Prompt.ask(Text("Pilih opsi ", style="bold white on green"))


        if pilihan == '1':
            print("")
            judul = Prompt.ask(Text("\n Masukkan judul buku", style="black on yellow"))
            penulis = Prompt.ask(Text("\n Masukkan penulis buku", style="white on purple")) 
            tahun_terbit = Prompt.ask(Text("\n Masukkan tahun terbit", style="white on red"))
            tambah_buku(judul, penulis, tahun_terbit)
        elif pilihan == '2': 
            tampilkan_buku()
        elif pilihan == '3':
            buku_id = Prompt.ask(Text("\nMasukkan ID buku yang ingin dihapus", style="red"))
            hapus_buku(buku_id)  
        elif pilihan == '4':
            print()
            console.print("\t\t Terimakasih Telah Mengunjungi Perpustakan Kami🙏🙏\t\t", style="white on red")
            break
        else:
            console.print("Pilihan tidak valid.", style="white on blue")

    

if __name__ == "__main__":
    main()
