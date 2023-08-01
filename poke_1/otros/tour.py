import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

class App(customtkinter.CTk):

#     Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:


# 1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"

# 2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
# medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

# 3- Validar todos los datos.

# 4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.

# 5- Una vez ingresada la cantidad se debe pedir por cada excursión 
# el importe y el tipo de excursión (caminata  o vehículo). 
# informar cual es el precio más caro, el más barato y el promedio

# 6- Informar cual es el tipo de excursión (caminata  o vehículo) más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)

    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour 🚂", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        for _ in range(1):
            nombre = prompt("","Nombre")
            while nombre == None or not nombre.isalpha():
                nombre = prompt("reingrese","Nombre")
            edad = prompt("","Edad")
            while edad == None or not edad.isdigit():
                edad = prompt("reingrese", "Edad")
            edad = int(edad)
            genero = prompt("","Género")
            while genero == None or not genero.isalpha() or not genero == "masculino" and not genero == "femenino":
                genero = prompt("reingrese","Género")
            altura = prompt("","Altura en cm")
            while altura == None or not altura.isdigit():
                altura = prompt("reingrese","Altura en cm")
            altura = int(altura)
            print (f"usted es {nombre} tiene {edad} de edad y su género es {genero}") 

            if (altura < 140):
                print(f"Usted es bajo")
            elif(altura < 170):
                print(f"Usted es medio")
            elif(altura < 191):
                print(f"Usted es alto")
            else:
                print(f"Usted es muy alto")

        # 4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.
        cantidad = prompt("", "Cuantas excurciones quieres hacer?")
        while cantidad.isalpha() or int(cantidad) < 0 or int(cantidad) > 11:
            cantidad=prompt("reingrese", "Cuantas excurciones quieres hacer?")
        cantidad = int(cantidad)

        importe_mas_caro = 0
        importe_mas_barato = 0
        importe_promedio = 0
        
            
        lista_de_excursiones = []
        lista_de_importes = []
        lista_tipo_de_excursiones = []
        i = 0

        for excursiones in range(cantidad):
            excursion = prompt("", "Qué excursión quieres realizar?")
            lista_de_excursiones.append(excursion)

            i += 1

            importe_excursiones = prompt("", "Ingrese el importe de la excursion")
            while importe_excursiones == None or not importe_excursiones.isdigit():
                importe_excursiones = prompt("reingrese", "Ingrese el importe de la excursion")
            importe_excursiones = int(importe_excursiones)
            lista_de_importes.append(importe_excursiones)
            importe_promedio += importe_excursiones 

            tipo_de_excursiones = prompt("", "caminata o vehiculo?")
            while tipo_de_excursiones == None or not tipo_de_excursiones.isalpha() or tipo_de_excursiones != "caminata" and tipo_de_excursiones != "vehiculo":
                tipo_de_excursiones = prompt("reingrese", "caminata o vehiculo?")
            lista_tipo_de_excursiones.append(tipo_de_excursiones) 

        # 5- Una vez ingresada la cantidad se debe pedir por cada excursión
        # el importe y el tipo de excursión (caminata  o vehículo). 
        for i in range(len(lista_de_excursiones)):
            importe_excursiones = lista_de_importes[i]
            tipo_de_excursiones = lista_tipo_de_excursiones[i]

            print (f"tipo de excursión {i} - {tipo_de_excursiones} y el importe: {importe_excursiones}")

        # informar cual es el precio más caro, el más barato y el promedio
        if importe_excursiones > importe_mas_caro:
            importe_mas_caro = importe_excursiones
            excursion = lista_de_excursiones[i]
            print(f"el importe mas caro es: {i} - {importe_mas_caro} - {excursion}")

        if importe_excursiones < importe_mas_barato:
            importe_mas_barato = importe_excursiones
            excursion = lista_de_excursiones[i]
            print(f"el importe mas barato es: {i} - {importe_mas_barato} - {excursion}")

        importe_promedio = importe_promedio / len(lista_de_excursiones)
        print(f"el importe promedio es: {importe_promedio}")
            
            
         



            




            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()