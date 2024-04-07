import tkinter as tk 
from tkinter import filedialog, messagebox

class SimpleText:
    def __init__(self, root):
        # Inicialización de la clase
        self.root = root
        # Creación del área de texto usando el widget Text de Tkinter
        self.text_area = tk.Text(self.root,bg="#000000",fg="#fe019a", font=("Times New Roman",14))
        self.text_area.pack(fill=tk.BOTH, expand=1) 
        self.current_open_file = "" 

    def quit_confirm(self):
        # Función para confirmar antes de cerrar la aplicación
        if messagebox.askokcancel("salir", "¿Deseas salir mi amor?"):
            self.root.destroy() 

    def abrir(self):
        # Función para abrir un archivo
        file = filedialog.askopenfilename() 

        if file:
            self.text_area.delete("1.0", tk.END) 
            with open(file, "r") as f:
                self.text_area.insert("1.0", f.read())
            self.current_open_file = file 

    def New_file(self):
        # Función para crear un nuevo archivo
        self.text_area.delete("1.0", tk.END) 
        self.current_open_file = "" 

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

# Creación de la ventana principal
root = tk.Tk()
root.title("LOVEPAD")
root.geometry("700x570")

# Creación de la barra de menú
menu = tk.Menu(root)
config_menu = tk.Menu(menu, tearoff=0)

# Creación de una instancia de la clase SimpleText para manejar las operaciones del área de texto
write = SimpleText(root)

# Definición de los comandos del menú y asignación de las funciones correspondientes
config_menu.add_command(label="Nuevo", command=write.New_file)
config_menu.add_command(label="Abrir", command=write.abrir)
config_menu.add_command(label="Guardar", command=write.save_file)
config_menu.add_command(label="Salir", command=write.quit_confirm)

# Configuración del menú y su integración en la ventana principal
root.config(menu=menu)
menu.add_cascade(label="ARCHIVO", menu=config_menu)


root.mainloop()
