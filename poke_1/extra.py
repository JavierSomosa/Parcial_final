import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

A) Al presionar el botón ‘Agregar' se debera cargar el nombre* y el precio** en sus respectivas listas.

* SOLO LETRAS MAYUSCULAS (A-Z)
** Enteros positivos

Si existe error al validar indicarlo mediante un Alert, cambiar el fondo del campo de texto con error
Si se cargo  coctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI AMBOS SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los articulos, sus precios y su posicion en la lista (por terminal)

C) Informar 
    1- Articulo mas caro
    2- Articulo mas barato
    3- Precio promedio
    4- Articulos que son mas caros que el promedio
    5- Articulos que son mas baratos que el promedio




'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_nombre_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Nombre Articulo")
        self.txt_nombre_articulo.grid(row=0, padx=20, pady=20)

        self.txt_precio_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.btn_agregar = customtkinter.CTkButton(
            master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(
            master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20,
                               columnspan=2, sticky="nsew")

        self.lista_nombre_articulo = ['TV', 'LICUADORA']
        self.lista_precio_articulo = [1000, 200]

    def btn_agregar_on_click(self):
        nombre = self.txt_nombre_articulo.get()
        if nombre == None or not nombre.isalpha():
            alert("Error", "Nombre no valido")

        precio_articulo = self.txt_precio_articulo.get()
        if precio_articulo == None or not precio_articulo.isdigit() or int(precio_articulo) < 1:
            alert("Error", "Precio no valido")

        self.lista_nombre_articulo.append(nombre)
        self.lista_precio_articulo.append((precio_articulo))
        
        alert("Actualizo", "correctamente")
        
# B) Al precionar el boton mostrar se deberan listar los articulos, sus precios y su posicion en la lista (por terminal)

# C) Informar 
#     1- Articulo mas caro
#     2- Articulo mas barato
#     3- Precio promedio
#     4- Articulos que son mas caros que el promedio
#     5- Articulos que son mas baratos que el promedio
    def btn_mostrar_on_click(self):
        i = 0
        for _ in range(len(self.lista_nombre_articulo)):
            print(f"{self.lista_nombre_articulo[i]} - {self.lista_precio_articulo[i]}") 
            i += 1

    def btn_informar_on_click(self):
        articulo_mas_caro = 0
        articulo_mas_barato = 10000
        promedio_de_precios = 0
        i=0

        for i, precio in enumerate(self.lista_precio_articulo):
            precio = self.lista_precio_articulo[i]
            if precio > articulo_mas_caro:
                articulo_mas_caro = precio
                articulo_mas_caro_nombre = self.lista_nombre_articulo[i]
            elif precio < articulo_mas_barato:
                articulo_mas_barato = precio
                articulo_mas_barato_nombre = self.lista_nombre_articulo[i]
            
            promedio_de_precios += precio
            
            i += 1
        promedio_de_precios = promedio_de_precios/len(self.lista_precio_articulo)
        print(f"articulo mas caro es: {articulo_mas_caro_nombre} y vale {articulo_mas_caro}")
        print(f"articulo mas barato es: {articulo_mas_barato_nombre} y vale {articulo_mas_barato}")
        print(f"el promedio de precios es: {promedio_de_precios}")
        
        for i, precio in enumerate(self.lista_precio_articulo):
            precio = self.lista_precio_articulo[i]
            if precio > promedio_de_precios:
                print(f"{self.lista_nombre_articulo[i]} es mas caro que el promedio y vale {precio}")
            else:
                print(f"{self.lista_nombre_articulo[i]} es mas barato que el promedio y vale {precio}")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
