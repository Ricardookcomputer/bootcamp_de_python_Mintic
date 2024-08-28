# como funcionan losmiteradores
# crear un alista de con algunos numeros
my_list=[1,2,3,4]
#obtner el iterador de la lista
#un interador  es un objeto que nos permite recorrer una coleccion (como una lista)
#una por uno
#usar el iterador para acceder a los elementos de la lista
#la funcion nmext() nos da el siguinet elemento en la coleccion  cada vez que se llama

my_iter=iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#iterar cadena de textop usando un iterador

text = "Hola mundo"
#crear un iterador para la cadena
#un iterador nos permite recorrer cada caracter de la cadena  uno por uno
iter_text=iter(text)
# iterar sobre cada caracter  de la cadena usando un bucle for
for char  in iter_text:
    print(char)
    # creaar un iterador que genere numeros impares desde 1 hasta el limite
    #range(1,limit+1,2)genera numeros comenzando en 1, con saltos de 2 ; hasta llegar a 9 ( el limite no se incluye)
    odd_iter=iter(range(1,10,2))
    #usar el iterador  para recorrer y mostrar cada impar generado

    for num in odd_iter:
        print(num)
        
   # definir una funcion generadora 
    def my_generator():
       # la palabra clave yield nos perimite devolver un valor y pausar  la funcion en ese punto
       yield 1# primer valor que se devuelve cuando  se llam la funcion
       yield 2  #el segundo valor que se devuelve cuando  se llam la funcion
       yield 3 # teercer valor que se devuelve cuando  se llam la funcion
       
    for value in my_generator():
           print(value)
    # fibonacci
    # la serie de Fibonacci hace referencia a que  vamos a obtner un valor sumado
    
    def fibonacci(limit):
        a,b=0,1
        #continaur generanfdo numeros mientras ha  sea menor que el limkite
        while a<limit:
         yield a # devolver el valor actual  de "a" pausar la ejecusuion  de la funcion
         a,b=b,a+b
         for num in fibonacci(10):
             print(num)
        
        
            



