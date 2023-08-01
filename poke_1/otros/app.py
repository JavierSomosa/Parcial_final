'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        lista_nombres = ["pepe", "coco", "jorge", "ñaña"]
        lista_edades = [28, 29, 30, 31,]
        lista_tecnologias = ["js", "python", "asp.net"]
        lista_generos = ["nb", "nb", "f", "m"]
        lista_puestos = ["sr", "jr", "sr", "jr"]
            
            # for _ in range(10):
            #     nombre = prompt("", "Nombre")
            #     while nombre == None or not nombre.isalpha():
            #         nombre = prompt("reingresar", "Nombre")
            #     lista_nombres.append(nombre)

            #     edad = prompt("", "Edad")
            #     while edad == None or not edad.isdigit() or int(edad) < 18:
            #         edad = prompt("reingresar", "Edad")
            #     edad = int(edad)
            #     lista_edades.append(edad)

            #     genero = prompt("","Género")
            #     while genero == None or not genero.isalpha() or genero != "f" and genero != "m" and genero != "nb":
            #         genero = prompt("reingresar","Género")
            #     lista_generos.append(genero)

            #     tecnologia = prompt("","Tecnología")
            #     while tecnologia == None or not tecnologia.isalpha() or tecnologia != "python" and tecnologia != "js" and tecnologia != "asp.net":
            #         tecnologia = prompt("reingresar","Tecnología")
            #     lista_tecnologias.append(tecnologia)

            #     puesto = prompt("", "Puesto")
            #     while puesto == None or not puesto.isalpha() or puesto != "jr" and puesto != "ssr" and puesto != "sr":
            #         puesto = prompt("reingresar", "Puesto")
            #     lista_puestos.append(puesto)

        i = 0
        contador_nb = 0
        for i, genero in enumerate(lista_generos):
            if genero == "nb":
                programan_nb = lista_tecnologias[i]
                if programan_nb == "asp.net" or programan_nb == "js":
                    contador_nb += 1
                edad_nb = lista_edades[i]
                if edad_nb >= 25 and edad_nb <= 40:
                    if lista_puestos[i] == "sr":
                        print(f"{lista_nombres[i]} es un postulante de genero no binario (NB) que programan en {programan_nb} y tiene una edad entre 25 y 40")
                    else:
                        print(f"{lista_nombres[i]} es un postulante de genero no binario (NB) que programan en {programan_nb} y tiene una edad entre 25 y 40")
            
            
            i += 1

        if contador_nb > 0:
            print(f"la cantidad de genero no binario (NB) que programan en ASP.NET o JS es {contador_nb}")
        else:
            print("No se encontraron postulantes de genero no binario (NB) que programan en ASP.NET o JS")


        promedio_de_edades = 0
        edad_mas_joven = 1000
        i = 0
        for edad in lista_edades:
            promedio_de_edades += edad
            puesto_del_mas_joven = lista_puestos[i]
            if puesto_del_mas_joven == "jr":
                if edad_mas_joven > edad:
                    nombre_mas_joven = lista_nombres[i]
                    edad_mas_joven = edad
            i += 1
        print(f"la persona mas joven en jr es {nombre_mas_joven} - {edad_mas_joven}")        
        promedio_de_edades /= len(lista_edades)
        print(f"El promedio de edades por género es {promedio_de_edades}")



        contador_python = 0
        contador_js = 0
        contador_asp = 0
        for tecnologia in lista_tecnologias:
            if tecnologia == "python":
                contador_python += 1
            elif tecnologia == "js":
                contador_js += 1
            else:
                contador_asp += 1
        if contador_python > contador_js and contador_python > contador_asp:
            print(f"La tecnología con más postulantes es pythom con {contador_python}")
        elif contador_js > contador_asp:
            print(f"La tecnología con más postulantes es JS con {contador_js}")
        else:
            print(f"La tecnología con más postulantes es ASP.NET con {contador_asp}")

        contador_postulantes_nb = 0
        contador_postulantes_f = 0
        contador_postulantes_m = 0
        for genero in lista_generos:
            if genero == "nb":
                contador_postulantes_nb += 1
            elif genero == "f":
                contador_postulantes_f += 1
            else:
                contador_postulantes_m += 1
        
        contador_postulantes_nb /= len(lista_generos)
        contador_postulantes_f /= len(lista_generos)
        contador_postulantes_m /= len(lista_generos)

        print(f"El porcentaje de postulantes de cada genero es nb: {contador_postulantes_nb} f:{contador_postulantes_f} m:{contador_postulantes_m}") 
             
            

#     Informar por pantalla:
# a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
# cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
# b. Nombre del postulante Jr con menor edad.
# c. Promedio de edades por género.
# d. Tecnologia con mas postulantes (solo hay una).
# e. Porcentaje de postulantes de cada genero.



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
