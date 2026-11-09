from tkinter import Tk, Label

ventana = Tk()

ventana.title("Mi primer Ventana")
ventana.geometry("400x300")

etiqueta1 = Label(
    ventana,
    text="Hola desde Tkinter!",
    font=("Arial",18),
    fg="#065f46",
    bg="#d1fae5"
    )
etiqueta1.pack(pady=10)

ventana.mainloop()