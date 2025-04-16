import tkinter as tk
from tkinter import messagebox
def decrypt_monoalphabetic(ciphertext, cipher_alphabet):
    plain_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = []
    decryption_dict = {cipher_char: plain_char for plain_char, cipher_char in zip(plain_alphabet, cipher_alphabet)}
    for char in ciphertext:
        lower_char = char.lower()
        if lower_char in decryption_dict:
            decrypted_char = decryption_dict[lower_char]
            decrypted_text.append(decrypted_char.upper() if char.isupper() else decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def decrypt():
    ciphertext = entry_ciphertext.get()
    cipher_alphabet = entry_cipher_alpha.get().lower()

    if len(cipher_alphabet) != 26 or not cipher_alphabet.isalpha():
        messagebox.showerror("خطأ", "Cipher alphabet must contain exactly 26 letters.")
        return

    plaintext = decrypt_monoalphabetic(ciphertext, cipher_alphabet)
    output_label.config(text=f"Plaintext: {plaintext}")

window = tk.Tk()
window.title("Monoalphabetic Cipher Decryption")
window.geometry("400x250")
tk.Label(window, text="Encrypted Message:").pack(pady=5)
entry_ciphertext = tk.Entry(window, width=50)
entry_ciphertext.pack()
tk.Label(window, text="26-letter Cipher Alphabet:").pack(pady=5)
entry_cipher_alpha = tk.Entry(window, width=50)
entry_cipher_alpha.pack()
tk.Button(window, text="Decrypt", command=decrypt).pack(pady=10)
output_label = tk.Label(window, text="", fg="green")
output_label.pack(pady=10)
window.mainloop()