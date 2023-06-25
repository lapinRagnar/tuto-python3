import tkinter as tk

window = tk.Tk()
window.title("Mon super app")
window.geometry("500x300")

hello = tk.Label(
  window, 
  text="hello world",
  bg="blue",
  fg="white",
  font=("arial", 20),
  width=15,
  height=2
)
hello.pack()
window.mainloop()

