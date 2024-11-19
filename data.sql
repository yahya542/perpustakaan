CREATE DATABASE perpustakaan;

USE perpustakaan;

CREATE TABLE buku (
    buku_id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(255) NOT NULL,
    penulis VARCHAR(255) NOT NULL,
    tahun_terbit INT,
    tersedia BOOLEAN DEFAULT TRUE
);
