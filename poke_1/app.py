# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder d todos los pokemones de tipo Electrico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = ["Mario", "Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Psyduck", "Eevee", "Gengar", "Mewtwo", "Vaporeon", "pepe"]
        self.lista_poder_pokemones = [290, 170, 150, 70, 150, 60, 150, 100, 120, 180, 95, 100]
        self.lista_tipo_pokemones = ["psiquico", "electrico", "fuego", "planta", "agua", "normal", "agua", "normal", "fantasma", "psiquico", "agua", "fuego"]


    def btn_mostrar_informe_1(self):
        lista = self.lista_nombre_pokemones
        #para mostar la lista
            #el nombre q quiaras
        for i, pokemon in enumerate(lista):                                  
            print (f"{i} - {pokemon}")
            i += 1  


    def btn_mostrar_informe_2(self):
        #2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
        maximo_poder = 0
        for i, tipo in enumerate(self.lista_tipo_pokemones):

            if tipo == "electrico":
                poder = self.lista_poder_pokemones[i]

                if poder > maximo_poder:
                    maximo_poder = poder
                    nombre = self.lista_nombre_pokemones[i] 

        print(f"El nombre del pokemon es: {nombre} - {maximo_poder}")

    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
        print("------------------------------------------------")
        poder_minimo = 200
        for i, tipo in enumerate(self.lista_tipo_pokemones):

            if tipo == "psiquico":
                poder = self.lista_poder_pokemones[i]
                
                if poder < poder_minimo:
                    poder_minimo = poder
                    nombre = self.lista_nombre_pokemones[i]
        
        print(f"El nombre del pokemon tipo psiquico con el poder mas bajo es: {nombre} - {poder_minimo}")
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
        print("------------------------------------------------")
        promedio_electrico = 0
        contador_electrico = 0

        for i, tipo in enumerate(self.lista_tipo_pokemones):
            if tipo == "electrico":
                poder = self.lista_poder_pokemones[i]
                contador_electrico +=1
                promedio_electrico += poder
        
        promedio_electrico = promedio_electrico / contador_electrico
        print(f"El promedio de poder de todos los pokemones de tipo Electrico es: {promedio_electrico}")

    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
        print("------------------------------------------------")
        promedio_superior = 0
        i = 0
        contador = 0
        for i, poder in enumerate(self.lista_poder_pokemones):
            i+=1
            contador += 1
            promedio_superior += poder
        promedio_superior = promedio_superior / contador
        lista_nombres = [] #para sacar el promedio de todos los pokemones crear una lista de nombres
        for i, poder in enumerate(self.lista_poder_pokemones):
            if poder > promedio_superior:
                nombre = self.lista_nombre_pokemones[i]                           
                poder = self.lista_poder_pokemones[i]
                lista_nombres.append(nombre)
                print(f"Listado de todos los pokemones cuyo poder de pelea supere el valor promedio {nombre} | {poder}")


    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
        print("------------------------------------------------")
        porcentaje_tipo_agua = 0
        contador = 0
        for i, tipo in enumerate(self.lista_tipo_pokemones):
            contador += 1
            if tipo == "agua":
                poder = self.lista_poder_pokemones[i]
                if poder > 100:
                    porcentaje_tipo_agua += poder
        
        porcentaje_tipo_agua = porcentaje_tipo_agua / contador
        if porcentaje_tipo_agua > 0:
            print(f"el porcentaje de poder del tipo agua es:{porcentaje_tipo_agua}")
        else:
                    print(f"el tipo agua no tiene mas de 100 de poder")
        
        print("------------------------------------------------")
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.    
        for i, tipo in enumerate(self.lista_tipo_pokemones):
            if tipo == "fuego":
                poder = self.lista_poder_pokemones[i]
                poder = poder * 1.1
                if poder > 100:
                    nombre = self.lista_nombre_pokemones[i]
                    print(f"Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos: {nombre} - {poder}")

        print("------------------------------------------------")           
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
        for i, tipo in enumerate(self.lista_tipo_pokemones):
            if tipo == "electrico":
                poder = self.lista_poder_pokemones[i]
                poder = poder * 0.85
                if poder > 100 and poder < 150:
                    nombre = self.lista_nombre_pokemones[i]
                    print(f"pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos{nombre} - {poder}")
    def btn_mostrar_informe_3(self):
        pass



                    
                                    
            

            
                
        

    
    def btn_cargar_pokedex_on_click(self):
            for _ in range(1): # range(el numero de iteraciones)
                nombre_del_pokemon = prompt("", "Ingrese nombre de pokemon")
                while nombre_del_pokemon == None or not nombre_del_pokemon.isalpha():
                    nombre_del_pokemon = prompt("", "Reingrese nombre de pokemon")
                
                poder_del_pokemon = prompt("", "Ingrese poder de pokemon")
                while poder_del_pokemon == None or not poder_del_pokemon.isdigit() or int(poder_del_pokemon) < 50 or int(poder_del_pokemon) > 200:
                    poder_del_pokemon = prompt("", "Reingrese poder de pokemon")

                tipo_del_pokemon = prompt("", "Ingrese tipo de pokemon")
                while tipo_del_pokemon == None or not tipo_del_pokemon.isalpha() or tipo_del_pokemon != "agua" and tipo_del_pokemon != "psquico" and tipo_del_pokemon != "electrico":
                    tipo_del_pokemon = prompt("", "Reingrese tipo de pokemon")

                self.lista_nombre_pokemones.append(nombre_del_pokemon)
                self.lista_poder_pokemones.append(int(poder_del_pokemon))
                self.lista_tipo_pokemones.append(tipo_del_pokemon)


    
if __name__ == "__main__":
    app = App()
    app.mainloop()


    #     cantidad_psiquico = 0
    #     cantidad_electrico = 0
    #     cantidad_fuego = 0
    #     cantidad_planta = 0
    #     cantidad_agua = 0
    #     cantidad_normal = 0
    #     lista_cantidades_por_tipo = [0, 0, 0, 0, 0, 0]
    #     for tipo in self.lista_tipo_pokemones:

    #         match tipo:
    #             case 'psíquico':
    #                 cantidad_psiquico += 1
    #                 lista_cantidades_por_tipo[0] += 1
    #             case 'eléctrico':
    #                 cantidad_electrico += 1
    #                 lista_cantidades_por_tipo[1] += 1
    #             case 'fuego':
    #                 cantidad_fuego += 1
    #                 lista_cantidades_por_tipo[2] += 1
    #             case 'planta':
    #                 cantidad_planta += 1
    #                 lista_cantidades_por_tipo[3] += 1
    #             case 'agua':
    #                 cantidad_agua += 1
    #                 lista_cantidades_por_tipo[4] += 1
    #             case 'normal':
    #                 cantidad_normal += 1
    #                 lista_cantidades_por_tipo[5] += 1

    #     tipo_maximo = None
    #     cantidad_maxima = 0

    #     lista_tipos = ["psíquico", "eléctrico", "fuego", "planta", "agua", "normal"]
    #     lista_cantidades_por_tipo = [cantidad_psiquico, cantidad_electrico,cantidad_fuego,cantidad_planta,cantidad_agua,cantidad_normal]

    #     indice_mayor = None
    #     i = 0
    #     for cantidad in lista_cantidades_por_tipo:

    #         if cantidad > cantidad_maxima:
    #             cantidad_maxima = cantidad
    #             indice_mayor = i
                
    #         i += 1
        

    #     tipo_mayor = lista_tipos[indice_mayor]

        
    #     print(f"El tipo mayor es {tipo_mayor}")

    #     print("--------------------------------------")
    #     acumulador = 0

    #     for poder in self.lista_poder_pokemones:
    #         acumulador += poder

    #     cantidad = len(self.lista_poder_pokemones)

    #     if cantidad == 0:
    #         print("Lista vacia")
    #     else:

    #         promedio = acumulador / cantidad
    #         print(f"Promedio = {promedio}")

    #         lista_nombres = []
    #         for i, poder in enumerate(self.lista_poder_pokemones):

    #             if poder > promedio:
    #                 nombre = self.lista_nombre_pokemones[i]
    #                 poder = self.lista_poder_pokemones[i]
    #                 lista_nombres.append(nombre)
    #                 print(f"Nombre {nombre} | {poder}")
            