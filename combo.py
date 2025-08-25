import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
ventana=tk.Tk()
ventana.title("ejemplo Combobox")
ventana.geometry("300x200")
#etiqueta
etiqueta=tk.Label(ventana,text="seleccione especialidad: ")
etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#crear combobox
opciones=["cardiologia","neurologia","pedriatria","dermatologia"]
combo=ttk.Combobox(ventana,values=opciones,state="readoly")
combo.current(0)#seleccionar primera opcion 
combo.grid(row=0, column=1, padx=10, pady=10)

#funcion ´para mostar
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("seleccion",f"has elegido:{seleccion}")
#boton para confirmar seleccion
bonton=tk.Button(ventana, text="aceptar", command=mostrar)
bonton.grid(row=1, column=0, columnspan=2, pady=15)

ventana.mainloop()