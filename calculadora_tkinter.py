# calculadora_tkinter.py

import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x500")

        self.expresion = ""
        self.entrada_texto = tk.StringVar()

        self.crear_componentes()

    def crear_componentes(self):
        entrada_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        entrada_frame.pack(side=tk.TOP)

        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=self.entrada_texto, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        entrada.grid(row=0, column=0)
        entrada.pack(ipady=10)

        botones_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        botones_frame.pack()

        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for (texto, fila, columna, col_span) in botones:
            self.crear_boton(texto, fila, columna, col_span)

    def crear_boton(self, texto, fila, columna, col_span=1):
        if texto == '=':
            boton = tk.Button(self.root, text=texto, width=32, height=3, bd=0, bg="#eee", cursor="hand2",
                              command=lambda: self.operar())
        elif texto == 'C':
            boton = tk.Button(self.root, text=texto, width=10, height=3, bd=0, bg="#f33", fg="white", cursor="hand2",
                              command=lambda: self.limpiar())
        else:
            boton = tk.Button(self.root, text=texto, width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                              command=lambda t=texto: self.agregar(t))

        boton.grid(row=fila, column=columna, columnspan=col_span, padx=1, pady=1)

    def agregar(self, valor):
        self.expresion += str(valor)
        self.entrada_texto.set(self.expresion)

    def limpiar(self):
        self.expresion = ""
        self.entrada_texto.set("")

    def operar(self):
        try:
            resultado = str(eval(self.expresion))
            self.entrada_texto.set(resultado)
            self.expresion = resultado
        except Exception as e:
            messagebox.showerror("Error", "Operación inválida")
            self.entrada_texto.set("")
            self.expresion = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
