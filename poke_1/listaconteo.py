import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []
        self.lista_negativos = []

    def btn_comenzar_ingreso_on_click(self):
        suma_acumulada = 0
        suma_acumulada_negativos = 0
        for _ in range(100):
            numero = prompt("Ingrese", "Ingrese un numero")
            if numero == None or numero.isalpha():
               break
            numero = int(numero)
            if numero > 0:
                self.lista.append(numero)
            else:
                self.lista_negativos.append(numero)
    def btn_mostrar_estadisticas_on_click(self):
        contador_de_ceros = 0
        suma_acumulada = 0
        suma_acumulada_negativos = 0
        i = 0
        i_suma = 0
        minimo_negativo = self.lista_negativos[0]
        maximo_positivo = self.lista[0]
        promedio_negativos = 0
        for numero in range(len(self.lista_negativos)):
            numero = self.lista_negativos[i]
            suma_acumulada_negativos += numero
            i += 1
            if numero == 0:
                contador_de_ceros += 1
            if numero < minimo_negativo:
                minimo_negativo = numero

        for numero in range(len(self.lista)):
            numero = self.lista[i_suma]
            suma_acumulada += numero
            i_suma += 1
            if numero > maximo_positivo:
                maximo_positivo = numero

        promedio_negativos = suma_acumulada_negativos / len(self.lista_negativos)
        print(f"la suma acumulada de todos los positivos: {suma_acumulada}")
        print(f"la suma acumulada de todos los negativos : { suma_acumulada_negativos}")
        print(f"Cantidad de números positivos ingresados: {len(self.lista)}")
        print(f"Cantidad de números negativos ingresados: {len(self.lista_negativos)}")
        print(f"Cantidad de ceros: {contador_de_ceros}")
        print(f"El minimo de los negativos: {minimo_negativo}")
        print(f"El maximo de los positivos: {maximo_positivo}")
        print(f"El promedio de los negativos: {promedio_negativos}")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
