import tkinter as tk
from tkinter import messagebox
import random

personajes = ["Profesor Plum", "Señorita Escarlata", "Coronel Mostaza", "Señora Blanca", "Reverendo Verde"]
locaciones = ["Casa", "Hotel o cuarto", "Cocina", "Biblioteca", "Salón de baile"]
armas = ["Candelabro", "Soga", "Llave inglesa", "Pistola", "Cuchillo"]

culpable, arma, locacion = random.choice(personajes), random.choice(armas), random.choice(locaciones)

def mostrar_ventana_opciones(opciones, tipo_opcion):
    ventana_opciones = tk.Toplevel(root)
    ventana_opciones.title(f"Adivinar {tipo_opcion}")
    
    tk.Label(ventana_opciones, text=f"Elige una opción para adivinar el {tipo_opcion}:").pack(pady=10)
    
    for i, opcion in enumerate(opciones, start=1):
        tk.Radiobutton(ventana_opciones, text=opcion, variable=elegido, value=i).pack()
    
    tk.Button(ventana_opciones, text="Adivinar", command=lambda: adivinar(tipo_opcion, ventana_opciones)).pack(pady=10)

def adivinar(tipo_opcion, ventana_opciones):
    global intentos
    respuesta = elegido.get()
    if tipo_opcion == "culpable":
        respuesta = personajes[respuesta - 1]
    elif tipo_opcion == "arma":
        respuesta = armas[respuesta - 1]
    else:
        respuesta = locaciones[respuesta - 1]
    
    intentos -= 1
    
    if intentos == 0:
        messagebox.showinfo("Fin del juego", f"Te quedaste sin intentos. El culpable era {culpable}, utilizó {arma} en la {locacion}.")
        jugar_nuevamente()
    elif respuesta == culpable or respuesta == arma or respuesta == locacion:
        messagebox.showinfo("¡Correcto!", f"¡Acertaste! El {tipo_opcion} es {respuesta}")
        ventana_opciones.destroy()
        if intentos == 0:
            jugar_nuevamente()
    else:
        messagebox.showinfo("Incorrecto", "Respuesta incorrecta. Inténtalo de nuevo.")

def jugar_nuevamente():
    respuesta = messagebox.askyesno("Jugar de nuevo", "¿Quieres jugar de nuevo?")
    if respuesta:
        global intentos, culpable, arma, locacion
        culpable, arma, locacion = random.choice(personajes), random.choice(armas), random.choice(locaciones)
        intentos = 3
    else:
        root.destroy()

root = tk.Tk()
root.title("Clue: Adivina al Culpable")

intentos = 3
elegido = tk.IntVar()

# Mostrar opciones para adivinar el culpable
tk.Button(root, text="Adivinar el culpable", command=lambda: mostrar_ventana_opciones(personajes, "culpable")).pack(pady=20)

# Mostrar opciones para adivinar el arma
tk.Button(root, text="Adivinar el arma", command=lambda: mostrar_ventana_opciones(armas, "arma")).pack(pady=20)

# Mostrar opciones para adivinar la locación
tk.Button(root, text="Adivinar la locación", command=lambda: mostrar_ventana_opciones(locaciones, "locación")).pack(pady=20)

root.mainloop()
