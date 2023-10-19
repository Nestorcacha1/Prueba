import tkinter as tk
from tkinter import messagebox

# Función para verificar el inicio de sesión
def iniciar_sesion():
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()

    # Aquí puedes agregar lógica para verificar las credenciales, por ejemplo:
    # if usuario == "usuario" and contraseña == "contraseña":
    if usuario == "admin" and contraseña == "admin":
        messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido, " + usuario + "!")
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")

# Etiquetas
usuario_label = tk.Label(ventana, text="Usuario:")
usuario_label.pack()
contraseña_label = tk.Label(ventana, text="Contraseña:")
contraseña_label.pack()

# Campos de entrada
usuario_entry = tk.Entry(ventana)
usuario_entry.pack()
contraseña_entry = tk.Entry(ventana, show="*")  # Mostrar asteriscos en lugar de la contraseña real
contraseña_entry.pack()

# Botón de inicio de sesión
iniciar_sesion_button = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
iniciar_sesion_button.pack()

ventana.mainloop()

print("Este una interfaz de usuario en python")