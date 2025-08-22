import tkinter as tk
from tkinter import messagebox
 
def nuevoPaciente():
    messagebox.showinfo("nuevo Paciente", "Registrar Paciente")
    ventanaRegistro = tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Paciente")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="cyan")
   
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre: ", bg="pink")
    nombreLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entryNombre = tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=5, pady=5, sticky="we")
    
    direccionLabel=tk.Label(ventanaRegistro,text="direccion: ", bg="pink")
    direccionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entryDireccion = tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1, column=1, padx=5, pady=5, sticky="we")
    
    telefonoLabel=tk.Label(ventanaRegistro,text="telefono: ", bg="pink")
    telefonoLabel.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entryTelefono = tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2, column=1, padx=5, pady=5, sticky="we")
   
    sexoLabel= tk.Label(ventanaRegistro, text="Sexo: ", bg="pink")
    sexoLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    sexo = tk.StringVar(value="Masculino")
    rbMasculino= tk.Radiobutton(ventanaRegistro,text="Masculino",variable= sexo, value= "Masculino")
    rbMasculino.grid(row=3,column=1,sticky="w")  
    rbFemenino= tk.Radiobutton(ventanaRegistro,text="Femenino",variable= sexo, value= "Femenino")
    rbFemenino.grid(row=3,column=2,sticky="w")
    
    #enfermedades base(checkbutton)
    enfLabel=tk.Label(ventanaRegistro,text="enfermedades base")
    enfLabel.grid(row=5,column=0,paxd=10,pady=5,sticky="w")
    diabetes=tk.BooleanVar()
    hipertencion=tk.BooleanVar()
    asma=tk.BooleanVar()
    
    cbDiabetes=tk.Checkbutton(ventanaRegistro,text="diabetes",variable=diabetes)
    cbDiabetes.grid(row=6,column=1,sticky="w")
    cbHipertencion=tk.Checkbutton(ventanaRegistro,text="hipertension",variable=hipertencion)
    cbHipertencion.grid(row=6,column=1,sticky="w")
    cbAsma=tk.Checkbutton(ventanaRegistro,text="asma",variable=asma,bg="pink")
    cbAsma.grid(row=6,column=1,sticky="w")
   
    def RegistrarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("diabetes")
        if hipertencion.get():
            enfermedades.apped("hipertencion")
        if asma.get():
            enfermedades.append("asma")
        if len(enfermedades)>0: 
            enfermedadesTexto=', '.join(enfermedades)
        else:
            enfermedadestexto='ninguna'   
        
            
        info=(f"Nombre:{entryNombre.get()}\n"
        f"direccion:{entryDireccion}\n"
        f"telefono:{entryTelefono}"
        f"Sexo:{sexo.get()}")
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
ventanaPrincipal.configure(bg="#a1f9ff")
 
 
 
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

