from tkinter import *
from tkinter import messagebox
import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt_notes():
    title = title_entry.get()
    message = secret_text.get("1.0",END)
    key = key_entry.get()

    if len(title)==0 or len(message)==0 or len(key)==0:
        messagebox.showwarning(title="Error!",message="Enter all infos!")
    else:
        message_encrpyted = encode(key, message)
        try:
            with open("mysecrets.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrpyted}")
        except FileNotFoundError:
            with open("mysecrets.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{message_encrpyted}")
        finally:
            title_entry.delete(0,END)
            secret_text.delete("1.0",END)
            key_entry.delete(0,END)

def decrypt_notes():
    encrypted_message = secret_text.get("1.0",END)
    master_key = key_entry.get()

    if len(encrypted_message)==0 or len(master_key)==0:
        messagebox.showwarning(title="Error!",message="Enter all infos!")
    else:
        try:
            decrypted_message = decode(master_key, encrypted_message)
            secret_text.delete("1.0",END)
            secret_text.insert("1.0", decrypted_message)
        except:
            messagebox.showwarning(title="Error!", message="Please enter encrypted message!")


#INTERFACE

window = Tk()
window.title("Secret Notes")
window.config(pady=30, padx=30)
window.minsize(width=350,height=600)

title_label = Label(text="Enter your title",font=("Arial",15,"bold"))
title_label.pack()
title_entry = Entry(width=25)
title_entry.pack()

secret_label = Label(text="Enter your secret",font=("Arial",15,"bold"))
secret_label.pack()
secret_text = Text(width=40, height=25)
secret_text.pack()

key_label = Label(text="Enter master key",font=("Arial",15,"normal"))
key_label.pack()
key_entry = Entry(width=20)
key_entry.pack()

save_button = Button(text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack()
decrypt_button = Button(text="Decrypt", command=decrypt_notes)
decrypt_button.pack()

window.mainloop()