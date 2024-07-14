import tkinter


window = tkinter.Tk()
window.title("Secret Notes")
window.config(pady=30, padx=30)
window.minsize(width=350,height=600)

canvas = tkinter.Canvas(height=100, width=100)
logo = tkinter.PhotoImage(file="topsecret.png")
canvas.create_image(0,0,image=logo)
canvas.pack()

title_label = tkinter.Label(text="Enter your title",font=("Arial",15,"bold"))
title_label.pack()
title_entry = tkinter.Entry(width=25)
title_entry.pack()

secret_label = tkinter.Label(text="Enter your secret",font=("Arial",15,"bold"))
secret_label.pack()
secret_text = tkinter.Text(width=40, height=25)
secret_text.pack()

key_label = tkinter.Label(text="Enter master key",font=("Arial",15,"normal"))
key_label.pack()
key_entry = tkinter.Entry(width=20)
key_entry.pack()

save_button = tkinter.Button(text="Save & Encrypt",command=)
save_button.pack()
decrypt_button = tkinter.Button(text="Decrypt",command=)
decrypt_button.pack()









window.mainloop()