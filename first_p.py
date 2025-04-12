import tkinter as tk
from tkinter import messagebox  
arabic_letters = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
def decrypt_english(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result
def decrypt_arabic(text, shift):
    result = ""
    for char in text:
        if char in arabic_letters:
            index = arabic_letters.index(char)
            new_index = (index - shift) % len(arabic_letters)
            result += arabic_letters[new_index]
        else:
            result += char
    return result
def auto_decrypt():
    text = entry_text.get()
    expected = entry_expected.get().split()
    lang = lang_var.get()
    if not text:
        messagebox.showwarning("Warning", "Please enter the encrypted text first.")
        return
    result_box.delete(1.0, tk.END)
    found = False
    max_shift = 26 if lang == "en" else len(arabic_letters)
    for shift in range(max_shift):
        attempt = decrypt_english(text, shift) if lang == "en" else decrypt_arabic(text, shift)
        if expected:
            for word in expected:
                if word in attempt:
                    result_box.insert(tk.END, f"Correct shift: {shift}\nDecrypted text: {attempt}\n")
                    found = True
                    return
        else:
            result_box.insert(tk.END, f"Shift {shift}: {attempt}\n")
    if expected and not found:
        result_box.insert(tk.END, "No expected words found.\n")
def show_all():
    text = entry_text.get()
    lang = lang_var.get()
    if not text:
        messagebox.showwarning("Warning", "Please enter the encrypted text first.")
        return
    result_box.delete(1.0, tk.END)
    max_shift = 26 if lang == "en" else len(arabic_letters)
    for shift in range(max_shift):
        attempt = decrypt_english(text, shift) if lang == "en" else decrypt_arabic(text, shift)
        result_box.insert(tk.END, f"Shift {shift}: {attempt}\n")
def clear_all():
    entry_text.delete(0, tk.END)
    entry_expected.delete(0, tk.END)
    result_box.delete(1.0, tk.END)
root = tk.Tk()
root.title("Caesar Cipher Decryption")
root.geometry("500x500")
tk.Label(root, text="Encrypted text:").pack()
entry_text = tk.Entry(root, width=50)
entry_text.pack(pady=5)
tk.Label(root, text="Expected words (optional):").pack()
entry_expected = tk.Entry(root, width=50)
entry_expected.pack(pady=5)
lang_var = tk.StringVar(value="en")
tk.Label(root, text="Select language:").pack()
tk.Radiobutton(root, text="English", variable=lang_var, value="en").pack()
tk.Radiobutton(root, text="Arabic", variable=lang_var, value="ar").pack()
tk.Button(root, text="Auto Decrypt", command=auto_decrypt).pack(pady=5)
tk.Button(root, text="Show All Attempts", command=show_all).pack(pady=5)
tk.Button(root, text="Clear All", command=clear_all).pack(pady=5)
tk.Label(root, text="Results:").pack()
result_box = tk.Text(root, height=10, wrap="word")
result_box.pack(pady=5)
root.mainloop()