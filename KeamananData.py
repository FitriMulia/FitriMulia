import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def encrypt_text():
    try:
        plaintext = entry_text.get()
        shift = int(entry_shift.get())
        ciphertext = caesar_encrypt(plaintext, shift)
        result_label.config(text=f"Teks terenkripsi: {ciphertext}")
    except ValueError:
        messagebox.showerror("Input Error", "Silakan masukkan nilai pergeseran yang valid (angka).")

def decrypt_text():
    try:
        ciphertext = entry_text.get()
        shift = int(entry_shift.get())
        plaintext = caesar_decrypt(ciphertext, shift)
        result_label.config(text=f"Teks asli: {plaintext}")
    except ValueError:
        messagebox.showerror("Input Error", "Silakan masukkan nilai pergeseran yang valid (angka).")

app = tk.Tk()
app.title("Caesar Cipher - Enkripsi & Dekripsi")
app.geometry("400x300")

tk.Label(app, text="Masukkan Teks:").pack(pady=5)
entry_text = tk.Entry(app, width=40)
entry_text.pack()

tk.Label(app, text="Masukkan Pergeseran (Shift):").pack(pady=5)
entry_shift = tk.Entry(app, width=10)
entry_shift.pack()

encrypt_button = tk.Button(app, text="Enkripsi", command=encrypt_text)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(app, text="Dekripsi", command=decrypt_text)
decrypt_button.pack(pady=5)

result_label = tk.Label(app, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

app.mainloop()
