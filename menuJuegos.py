import os, sys

#limpio segun el sistema la pantaya 
def limpiar():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
        

while True:
    
    print('''
    \t╔════════════════════════════════════╗
    \t  1 PIEDRA PAPEL TIJERAS
    \t  2 ADIVINA EL NUMERO 
    \t  0 SALIR
    \t╚════════════════════════════════════╝
    \t Ingrese opción: ''')
    opcion= input('\t  Seleccione juegos: ')
    if opcion in ['0','1','2']:
        if opcion == '0':
            exit()
        elif  opcion =='1':
            limpiar()
            print("opcion 1")
        elif opcion =='2':
            limpiar()
            print ("Opcion 2")
    
    else:
        limpiar()
        print("Opcion no valida")
    
        