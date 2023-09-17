import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

class TextBlockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Bloques de Texto")

        self.text_blocks = []
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(padx=10, pady=10)

        self.save_button = tk.Button(root, text="Guardar Bloque de Texto", command=self.save_text)
        self.save_button.pack(pady=5)

        self.export_button = tk.Button(root, text="Exportar Texto", command=self.export_text)
        self.export_button.pack(pady=5)

    def save_text(self):
        # Obtiene el texto de la caja de texto y lo guarda en la lista text_blocks
        text_block = self.text_area.get("1.0", tk.END)
        self.text_blocks.append(text_block)
        # Limpia la caja de texto
        self.text_area.delete("1.0", tk.END)

    def export_text(self):
        if self.text_blocks:
            # Abre un cuadro de diálogo para seleccionar la ubicación del archivo de exportación
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt")])
            if file_path:
                # Combina todos los bloques de texto con "---" como separadores
                combined_text = "---\n".join(self.text_blocks)
                # Escribe el texto combinado en un archivo
                with open(file_path, "w") as file:
                    file.write(combined_text)
                # Limpia la lista de bloques de texto
                self.text_blocks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = TextBlockApp(root)
    root.mainloop()

