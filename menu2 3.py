import tkinter as tk
from tkinter import messagebox
 
def nuevoPaciente():
    messagebox.showinfo("nuevo Paciente", "Registrar Paciente")
    ventanaRegistro = tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Paciente")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="cyan")
 
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre: ", bg="Pink")
    nombreLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entryNombre = tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=5, pady=5, sticky="we")
   
    direccionLabel=tk.Label(ventanaRegistro,text="Direccion: ", bg="Pink")
    direccionLabel.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entryDireccion = tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=2, column=1, padx=5, pady=5, sticky="we")
 
    telefonoLabel=tk.Label(ventanaRegistro,text="Telefono: ", bg="Pink")
    telefonoLabel.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    entryTelefono = tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=3, column=1, padx=5, pady=5, sticky="we")
 
    sexoLabel= tk.Label(ventanaRegistro, text="Sexo: ", bg="Pink")
    sexoLabel.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    sexo = tk.StringVar(value="Masculino")
    rbMasculino= tk.Radiobutton(ventanaRegistro,text="Masculino",variable= sexo, value= "Masculino")
    rbMasculino.grid(row=4,column=1,sticky="w")  
    rbFemenino= tk.Radiobutton(ventanaRegistro,text="Femenino",variable= sexo, value= "Femenino")
    rbFemenino.grid(row=4,column=2,sticky="w")
   
    enfLabel = tk.Label(ventanaRegistro, text="Enfermedades base:", bg="pink")
    enfLabel.grid(row=5, column=0, padx= 10, pady=5, sticky="w")
    diabetes = tk.BooleanVar()
    hipertension = tk.BooleanVar()
    asma = tk.BooleanVar()
   
    cbDiabetes = tk.Checkbutton(ventanaRegistro, text="Diabetes", variable=diabetes, bg="pink")
    cbDiabetes.grid(row=5, column=1, sticky="w")
    cbHipertension = tk.Checkbutton(ventanaRegistro, text="Hipertension", variable=hipertension, bg="pink")
    cbHipertension.grid(row=6, column=1, sticky="w")
    cbAsma = tk.Checkbutton(ventanaRegistro, text="Asma", variable=asma, bg="pink")
    cbAsma.grid(row=7, column=1, sticky="w")
   
    def RegistrarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertension")
        if asma.get():
            enfermedades.append("Asma")
        if len(enfermedades)> 0:
            enfermedadesTexto=', '.join(enfermedades)
        else:
            enfermedadesTexto= 'Ninguna'
 
        info=(f"Nombre: {entryNombre.get()}\n"
        f"Direccion: {entryDireccion.get()}\n"
        f"Telefono: {entryTelefono.get()}\n"
        f"Sexo: {sexo.get()}\n"
        f"Enfermedades: {enfermedadesTexto}")
        messagebox.showinfo("Datos Registrados", info)
        ventanaRegistro.destroy()
    btnRegistrar =tk.Button(ventanaRegistro, text="Datos Registrados", command=RegistrarDatos)
    btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)
 
def buscarPaciente():
    messagebox.showinfo("buscar Paciente", "buscar Paciente")
 
def eliminarPaciente():
    messagebox.showinfo("Eliminar Paciente", "eliminar Paciente")
 
def nuevoDoctor():
    messagebox.showinfo("Nuevo Doctor","Registrar Doctor")
 
def buscarDoctor():
    messagebox.showinfo("buscar Doctor","buscar Doctor")
 
def eliminarDoctor():
    messagebox.showinfo("Eliminar Doctor", "eliminar Doctor")
 
ventanaPrincipal= tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("800x600")
ventanaPrincipal.configure(bg="#9cd3e0")
 
 
#Barra de menu
 
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)
 
menuPacientes=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Pacientes", menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente",command=nuevoPaciente)
menuPacientes.add_command(label="Eliminar Paciente",command= eliminarPaciente)
menuPacientes.add_command(label="Buscar Paciente",command=buscarPaciente)
 
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir", command=ventanaPrincipal.quit)
 
#Barra de menu doctores
 
menuDoctores=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor",command= nuevoDoctor)
menuDoctores.add_command(label="Eliminar Doctor",command= eliminarDoctor)
menuDoctores.add_command(label="Buscar Doctor",command= buscarDoctor)
 
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)
 
#ayuda
 
menuAyuda=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda:messagebox.showinfo("Acerca de","Version 1.0 - Sistema Biomedcina"))
 
 
 
ventanaPrincipal.mainloop()
 