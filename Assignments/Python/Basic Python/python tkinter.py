import tkinter as tk

root = tk.Tk()
root.title("Tkinter Application")
root.geometry("200x200")


def say_hello():
    print("Hello there!")
    print("see ya!")


hello_button = tk.Button(root, text="Click here to print the text", command=say_hello)
hello_button.pack(pady=80)

root.mainloop()
