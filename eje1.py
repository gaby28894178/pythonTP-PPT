

nombre =  input("ingrese bunro ")

#function nombre (){}
# suma funcion suma  que recibe argumentos 
def suma(*args): 
    total = 0
    for j in args:
        total += j
    return total
#aca termina retorno la suma 
#resta 
def resta(*args):
    total = 0
    for num in args:
        total -= num
    return total
#aca termina retorno la resta

''' 1)- Escribir un programa que permita que el usuario ingrese su nombre. El programa debe emitir una salida con un mensaje de bienvenida que incluya el nombre ingresado. Ejemplo de ejecución: Ingrese su nombre: Juan Bienvenido Juan '''

#name=str(input("Ingrese su nombre "))
#print(f"bienvenido! '{name}'")

# name=str(input("Ingrese su nombre "))
# print("bienvenido! ",name)

'''2)- Escribir un programa que solicite al usuario su nombre y su edad, y luego muestre por pantalla un mensaje que diga "Hola, [nombre]. Tu edad es [edad] años." Ejemplo de ejecución: Ingrese su nombre: Juan Ingrese su edad: 30 Hola, Juan. Tu edad es 30 años. '''

# name1=str(input("Ingrese su nombre "))
# edad = int(input("Ingrese su edad "))
# print(f"\nSu nombre es ! '{name1}' usted tiene {edad} años de edad")

''' 3)- Escribir un programa que solicite al usuario su nombre y su edad, después pida una
cantidad de años y muestre por pantalla un mensaje que indique cuántos años tendrá la persona
después de sumarle a su edad la cantidad de años ingresada.
El mensaje debe tener el siguiente formato: 'Hola, [nombre].
Dentro de [cantidad] años tendrás [edad + cantidad] años'". 
Ejemplo: Si el usuario ingresa "Juan" y "20" y luego ingresa "5", 
el programa debe mostrar por pantalla "Hola, Juan. Dentro de 5 años tendrás 25 años". '''

# name=str (input("Ingrese su nombre profavor "))
# edad=int(input("Ingrese su edad "))
# year=int(input("Ingrese cuantos años esperar para fver su edad "))
# print(f'hola {name} su edad actual es de {edad} y en los proccimos {year} tendra {edad+year}').


''' 4)- Escribir un programa que solicite al usuario ingresar tres números enteros.
El programa debe mostrar por pantalla el resultado de sumar los tres números de la
siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]"
. Ejemplo: Si el usuario ingresa 1, 2 y 3, 
el programa debe mostrar por pantalla: "1 + 2 + 3 = 6".  '''
# num1=int(input("Ingrese numero1 "))
# num2=int(input("Ingrese numero2 "))
# num3=int(input("Ingrese numero3 "))
# print(f"la suma de {num1} + {num2} + {num3} = {num1+num2+num3}")



'''  5)- Escribir un programa que solicite al usuario ingresar dos notas de un alumno. 
El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: "
Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]". Ejemplo: Si el usuario ingresa
7 y 8, el programa debe mostrar por pantalla: 
"Notas: 7 , 8 ==> promedio: 7.5". 
'''
# nota1=int(input("Ingrerse nota1 "))
# nota2=int(input("Ingrerse nota2 "))
# nota3=int(input("Ingrerse nota3 "))
# print (f'\nTotal : \n\t [Nota1] + [Nota2] + [nota3] = {suma(nota1,nota2,nota3)}')

''' 6)- Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglón. Ejemplo de ejecución:     Ingrese la nota 1: 7     Ingrese la nota 2: 8     Ingrese la nota 3: 9     Notas: 7, 8, 9     Promedio: 8.0 '''


# nota1 = int(input("Ingrese nota "))
# nota2 = int(input("Ingrese nota "))
# nota3 = int(input("Ingrese nota "))
# promedio = nota1+nota2+nota3/3
# print(f'Nota , {nota1} Nota, {nota2} Nota, {nota3}\n Promedio:{round(promedio,2)}')

'''  7) Escribir un programa que permita ingresar un número entero. 
Debe mostrarse el número ingresado: a. Multiplicado por 10.
 (utilizar el operador *)
  a. Dividido por 10. (utilizar el operador /) 
  a. Elevado al cuadrado. (utilizar el operador **) Cada resultado debe mostrarse en una línea distinta.
   Ejemplo de ejecución: Ingrese un número entero: 5 5 * 10 = 50 5 / 10 = 0.5 5 ** 2 = 25 '''


num = int(input("Ingrese nota: "))
print('fel numero ingresado es: {num} ,\n su numero multiplicado por 10 es , {num*10:.2f} ,\n la divicion es, {num /5:.2f}\n Elevado al cuadrado. es {num**2:.2f}')

'''
8) Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y la cantidad de horas trabajadas por día, para calcular el salario semanal de un trabajador que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados, suponiendo que todas las horas tienen el mismo valor." Como pensarlo:
 
 1. Pedir al usuario que ingrese el valor monetario de una hora de trabajo y almacenarlo en una variable valor_hora. 
 
 2. Pedir al usuario que ingrese la cantidad de horas trabajadas por día por el trabajador y almacenarla en una variable horas_trabajadas_por_dia. Calcular el salario diario del trabajador multiplicando valor_hora por horas_trabajadas_por_dia. 
Calcular el salario semanal del trabajador multiplicando el salario diario por la cantidad de días hábiles de la semana. Para esto, puedes 

utilizar la constante dias_habiles definida como 5.

 4. Calcular la cantidad de horas trabajadas por el trabajador el sábado, que es la mitad de la cantidad de horas trabajadas por día hábil. Para esto, se puede utilizar la vaiable horas_sabado definida como horas_trabajadas_por_dia / 2. 5. Calcular el salario del trabajador por las horas trabajadas el sábado multiplicando valor_hora por horas_sabado.
 
  6. Sumar el salario semanal con el salario del sábado para obtener el salario total semanal del trabajador. 7. Mostrar el resultado del salario semanal en la pantalla. 
'''

# precio_hora = float(input("Ingrese precio actual de la hora trabajada "))
# horas_trabajadas = int (input("Ingrese cantidad de hora trabajadas en el dia: "))
# DIAS_HABILES = 5


# # intercambiar 2 numero
# def ordenar2 (n1,n2):
#     auxi=n1
#     n1=n2
#     n2=auxi 
#     return n1,n2
# #retorno los numeros 
# nota1=int(input("nota1 ingrese "))
# nota2=int(input("nota2 ingrese "))
# print(f"las notas son nmota1= {nota1} \nla nota2 = {nota2}")
# print(f"las notas ordenadas son, = {ordenar2(nota1 , nota2)} ")