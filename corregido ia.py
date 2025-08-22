import tkinter as tk
from tkinter import messagebox

def nuevoDoctor():
    ventanaRegistro = tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Sistema de Registro de Doctores")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="paleTurquoise")

    # Nombre
    tk.Label(ventanaRegistro, text="Nombre completo:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entryNombre = tk.Entry(ventanaRegistro, bg="mintCream")
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")

    # Dirección
    tk.Label(ventanaRegistro, text="Dirección:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entryDireccion = tk.Entry(ventanaRegistro, bg="mintCream")
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")

    # Teléfono
    tk.Label(ventanaRegistro, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entryTelefono = tk.Entry(ventanaRegistro, bg="mintCream")
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")

    # Especialidad
    tk.Label(ventanaRegistro, text="Especialidad:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    especialidad = tk.StringVar(value="Pediatría")

    tk.Radiobutton(ventanaRegistro, text="Pediatría", variable=especialidad, value="Pediatría").grid(row=3, column=1, sticky="w")
    tk.Radiobutton(ventanaRegistro, text="Cardiología", variable=especialidad, value="Cardiología").grid(row=4, column=1, sticky="w")
    tk.Radiobutton(ventanaRegistro, text="Neurología", variable=especialidad, value="Neurología").grid(row=5, column=1, sticky="w")

    # Disponibilidad
    tk.Label(ventanaRegistro, text="Disponibilidad:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    disponibleMañana = tk.BooleanVar()
    disponibleTarde = tk.BooleanVar()
    disponibleNoche = tk.BooleanVar()

    tk.Checkbutton(ventanaRegistro, text="Mañana", variable=disponibleMañana).grid(row=6, column=1, sticky="w")
    tk.Checkbutton(ventanaRegistro, text="Tarde", variable=disponibleTarde).grid(row=7, column=1, sticky="w")
    tk.Checkbutton(ventanaRegistro, text="Noche", variable=disponibleNoche).grid(row=8, column=1, sticky="w")

    # Función para guardar datos
    def registrarDatos():
        disponibilidad = []
        if disponibleMañana.get():
            disponibilidad.append("Mañana")
        if disponibleTarde.get():
            disponibilidad.append("Tarde")
        if disponibleNoche.get():
            disponibilidad.append("Noche")

        disponibilidadTexto = ', '.join(disponibilidad) if disponibilidad else "No disponible"

        info = (
            f"Nombre: {entryNombre.get()}\n"
            f"Dirección: {entryDireccion.get()}\n"
            f"Teléfono: {entryTelefono.get()}\n"
            f"Especialidad: {especialidad.get()}\n"
            f"Disponibilidad: {disponibilidadTexto}"
        )

        messagebox.showinfo("Datos Registrados", info)
        ventanaRegistro.destroy()

    # Botón para guardar
    tk.Button(ventanaRegistro, text="Guardar Datos", command=registrarDatos).grid(row=15, column=1, columnspan=2, pady=18)

# Ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("600x400")
ventanaPrincipal.configure(bg="#8bedfa")

# Menú
barraMenu = tk.Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)

menuDoctores = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=nuevoDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)

ventanaPrincipal.mainloop()