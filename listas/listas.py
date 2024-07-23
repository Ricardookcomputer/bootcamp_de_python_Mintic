to_do=[ " fue un dia lleno de muchas actividades de trabajo",
       "sali en mi espacio de descanso para apartar cita  con la pediatra para la niña ",
       "y ahora en la clsee de bootcamp"
       
       ]
print(to_do)

numbers=[1,2,3,4,"cinco"]
print(numbers)
print (type(numbers))

mix=["uno",2,3.14,True,[1,2,3]]
print(mix)
print (len(mix))
print("primer elemento:"[0],mix[0])
print("segundo elemento:",mix[1])
print("tercer elemento:",mix[2])
print("cuarto elemento",mix[3])
print("ultimo elemento:",mix[-1])

mix.append(False)
print(mix)
mix.append("Ricardo")
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))

numbers=[1,2,100,90,45,3,4,5]
print(numbers)
print("mayor",max(numbers))
print("menor",min(numbers))
del numbers[-1]
print(numbers)

del numbers[:2]
print(numbers)
del (numbers)
#print(numbers)
    