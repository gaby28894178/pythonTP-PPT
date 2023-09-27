#importo coloram  y destructuro y traigo init fore style 
from  colorama import  init, Fore, Style
#inicio el init 
init()
#importo random para  q la pc juege aleatoriuamente los numeros 
import random
#importo el os sys de  sistema para limpiar pantalla
import os, sys

#limpio segun el sistema la pantaya 
def limpiar():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
        
#******creo las variables a usar
jugada=""
user = ""
vidas = 3
enpate = 0
contador = 0
ganadas = 0
pcj=0
user = input(Fore.BLUE+"Deberíamos tener un nombre de jugador: ")

while vidas != 0:
    limpiar()
    print(Fore.CYAN +f""" \t\t
{Fore.RED}⓿,➊,➌,➍,➎,➏,➐,➑,➒,➊⓿⓿,➊,➌,➍,➎,➏,➐,➑,➒,➊⓿⓿,➊,➌,➍,➎,➏,➐,➑,➒,➊⓿
\t\t{Fore.GREEN}✨✨✨✨ Bienvenidos Al Reto Mix PPT -✨✨✨
\t\t\t{Fore.RESET} JUGADOR:{Fore.CYAN} {user.upper()} {Fore.RESET} SE ENFRENTA A{Fore.CYAN} PC{Fore.RESET}
\t╔══════════════════════════════════════════════════════════════╗
\t║{Fore.MAGENTA}✂ ✂ ✂ ✂ ✂ ✂ ✂ ✂{Fore.RESET} : VR 0.1 {[vidas]}Vidas: ♥ ♥ ♥\t       ║      
\t║══════════════════════════════════════════════════════════════║
\t║  1].PIEDRA    ║Recuerde que tan║  1.PIEDRA GANA A TIJERA.    ║
\t║  2].PAPEL     ║Solo cuenta con ║  2.PAPEL  GANA A PIEDRA.    ║
\t║  3].TIJERAS   ║   Tres Vidas   ║  3.TIJERA GANA A PAPEL..    ║
\t╚══════════════════════════════════════════════════════════════╝
 \t {Fore.GREEN} USUARio:{user.upper()} {ganadas}:{Fore.CYAN} Empates: {enpate} :{Fore.GREEN} |{Fore.YELLOW} PC: {pcj}  ♥ ♥ ♥  | Vidas: {vidas} ♥ ♥ ♥ \n
\t\t[1]-🅿 🅸 🅴 🅳 🆁 🅰 - [2] 🅿 🅰 🅿 🅴 🅻 - [3] 🆃 🅸 🅹 🅴 🆁 🅰 🆂
⓿,➊,➌,➍,➎,➏,➐,➑,➒,➊⓿⓿,➊,➌,➍,➎,➏,➐,➑,➒,➊⓿⓿,➊,➌,➍,➎,➏,➐,➑,➒,➊⓿
""")
    contador = contador - 1 
    pc = random.randint(0, 2) + 1
    while jugada not in ['1','2','3']: 
        jugada = input( f"\tEl jugador {Fore.GREEN}{user.upper()} Selecciona: ")
    jugada = int (jugada)
      # imprimo lo q juega user y pc 
    #_print(f"jugador {jugada}  PC {pc}")
    
    if jugada == pc:
        #print("Es empate")# igualdad 
        enpate = enpate + 1 # sumo enpate
    elif (jugada == 1 and pc == 2) or (jugada == 2 and pc == 3) or (jugada == 3 and pc == 1):
        #print(f"Gana pc {pc}")# gana pc
        vidas = vidas - 1 #pierdo vida
        pcj = pcj+1
    else:
       # print(f"Gana User {jugada} pc elije {pc}") # si no gana user 
        ganadas = ganadas + 1 #sumo la ganada
   

if ganadas >pcj:
    print("Gana Usuario ", user.upper()," Con ",ganadas ," PC tiene",pcj)
else:
    print("Gana PC  Con ",pcj, " Usuario Tiene ",ganadas )



    
