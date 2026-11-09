from tkinter import Tk, Button, Label

def saludar(nombre):
    mensaje = f"Hola! {nombre}"
    Label(ventana, text=mensaje).pack()

ventana = Tk()

boton = Button(
                ventana,
                text="Saludar",
                command= lambda: saludar("Luis"),
                bg="#10b981",
                fg="white",
                font=("Arial",12,"bold")
                )

boton.pack(pady=20)

ventana.mainloop()