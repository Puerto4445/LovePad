import customtkinter as tk
import tkinter as tc
from tkinter import filedialog, messagebox

class SimpleText:
    def __init__(self,root):
        self.root=root
        self.text_area = tk.CTkTextbox(self.root,font=("Times New Roman",20))
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_open_file = ""
    
    def New_file(self):
    # Función para crear un nuevo archivo
        self.text_area.delete("1.0", tk.END) 
        self.current_open_file = "" 
    
    def abrir(self):
        # Función para abrir un archivo
        file = filedialog.askopenfilename() 

        if file:
            self.text_area.delete("1.0", tk.END) 
            with open(file, "r") as f:
                self.text_area.insert("1.0", f.read())
            self.current_open_file = file 
    
    def save_file(self):
        # Función para guardar el contenido del área de texto en un archivo
        if not self.current_open_file: 
            new_file_path = filedialog.asksaveasfilename() 
            if new_file_path:
                self.current_open_file = new_file_path 
            else:
                return 
        with open(self.current_open_file, "w") as f: # Se abre el archivo en modo escritura
            f.write(self.text_area.get("1.0", tk.END))
    
    def quit_confirm(self):
        # Función para confirmar antes de cerrar la aplicación
        if messagebox.askokcancel("salir", "¿Deseas salir mi amor?"):
            self.root.destroy() 

#Ventana principal
root= tk.CTk()
root.geometry("900x400")
root.title("LovePad")
root.iconbitmap('img.ico')

#Menu
menu = tc.Menu(root)
config_menu = tc.Menu(menu, tearoff=0,)

# Creación de una instancia de la clase SimpleText para manejar las operaciones del área de texto
write = SimpleText(root)

#Definicion de los comandos del menu y sus funciones "ARCHIVO"
config_menu.add_command(label="Nuevo", command=write.New_file)
config_menu.add_command(label="Abrir", command=write.abrir)
config_menu.add_command(label="Guardar", command=write.save_file)
config_menu.add_separator()
config_menu.add_command(label="Salir", command=write.quit_confirm)

#tamaño letras del menu 
tamaño_fuente = 20
fuente_menu = ("Arial", tamaño_fuente)
for item in menu.winfo_children():
    item.config(font=fuente_menu)


#configuracion del menu y su integracion en la ventana
root.config(menu=menu)
menu.add_cascade(label="ARCHIVO", menu=config_menu)
menu.add_cascade(label="EDICION")


root.mainloop()