#importacuon de libreria
import tkinter as tk
from tkinter import ttk,messagebox

#crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("libro de paciente y doctores")
ventana_principal.geometry("400x600")

#crear contenedor notebook
pestañas=ttk.Notebook(ventana_principal)

#crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
frame_doctores=ttk.Frame(pestañas)

#agregar pestaña al notebook
pestañas.add(frame_pacientes, text="pacientes")
pestañas.add(frame_doctores, text="doctores")


#mostrar las pestañas en la ventana 
pestañas.pack(expand=True, fill="both")

#nombre
labelNombre=tk.Label(frame_pacientes, text="nombre completo: ")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)

#fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes, text="fecha de Nacimiento")
labelFechaN.grid(row=1,column=0, sticky="w", pady=5, padx=5)
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1, column=1, sticky="w", pady=5, padx=5)

#edad(readol)
labelEdad=tk.Label(frame_pacientes, text="edad")
labelEdad.grid(row=2,column=0, sticky="w", pady=5, padx=5)
edad=tk.Entry(frame_pacientes, state="readonly")
edad.grid(row=2, column=1, sticky="w", pady=5, padx=5)

#genero
labelgenero=tk.Label(frame_pacientes, text="genero")
labelgenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("femenino")#valor por defecto
redioFemenino=ttk.Radiobutton(frame_pacientes, text="femenino", variable=genero, value="femenino")
redioFemenino.grid(row=3, column=1, sticky="w", pady=5, padx=5)


#grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text="grupo sanguineo")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryLabelGrupoSanginineo=tk.Entry(frame_pacientes)
entryLabelGrupoSanginineo.grid(row=5, column=1, sticky="w", pady=5, padx=5)

#tipo de seguro
labelTipoSeguro = tk.Label(frame_pacientes, text="Tipo de seguro")
labelTipoSeguro.grid(row=6, column=0, sticky="w", padx=5, pady=5)
tipo_seguro = tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro = ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable= tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", padx=5, pady=5)

#centro medico
labelCentroMedico = tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centro_medico = tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico = ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro sur"], textvariable= centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)

ventana_principal.mainloop()