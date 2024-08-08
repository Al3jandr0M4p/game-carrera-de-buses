import os
import random
import time
from bus import Bus

def limpiar_consola():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    bus_1 = Bus()
    bus_2 = Bus()
    print("CARRERA DE BUSES!!")
    print("REPUBLICA DOMINICANA VS HAITI")
    
    time.sleep(2)
    while True:
        limpiar_consola()
        Bus.dibujar_inicio_pista()
        bus_1.dibujar_bus(random.randint(1, 2), "REPUBLICA DOMINICANA")
        Bus.dibujar_inicio_pista()
        bus_2.dibujar_bus(random.randint(1, 2), "HAITI")
        Bus.dibujar_inicio_pista()
        
        if bus_1.posicion >= 100 or bus_2.posicion >= 100:
            if bus_1.posicion >= 100:
                print("REPUBLICA DOMINICANA GANA!!")
            else:
                print("HAITI GANA!!")
            time.sleep(10)
            break
        
        time.sleep(0.1)

main()