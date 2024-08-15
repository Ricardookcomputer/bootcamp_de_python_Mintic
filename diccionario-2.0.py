numbers={1:"uno",2:"dos",3:"tres"}#en llaves
print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])
information={"nombre":"Ricardo",
             "apellido":"Maldonado",
             "esta feliz":True,
              "estatura":1.80 }
print(information)
del information["apellido"]
print(information)
clave=information.keys()
print(clave)
print(type(clave))
values=information.values()
print(values)

pairs=information.items()
print(pairs)

contacts={"Ricardo":   {"Apellido":"Maldonado", "Altura":1.80,
                        "edad":39, "Telefono":3229264620,
                        "Signo sodiacal": "Virgo",
                        "Serie favorita":"the choose","cancion favorita" :"ok computer",
                        "Lugar soñado de vacaiones": "ibiza" ,"habilidad":"escuchar","pasatiempo":"leer",
                        "Heroe o personas que mas admiras":"Gabriel Garcia Marquez",
                        "Libro que mas te ha impactado":"cien años de soledad",
                        "cenar con alguien":"obama","superpoderes":"realidad aumentada",
                        "logro personal":"aprender programacion python"
                      },"Quini":{"Apellido":"donoso","estatura":1.15,"edad":7}
    
}

print(contacts)