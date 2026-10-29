import time
import winsound


def tiempo(minutos,tipo):
    winsound.Beep(1000,1000)
    print(f"----Haz entrado en tiempo de {tipo}------")
    for i in range(0,minutos):
        falta=minutos-i
        print(f"falta {falta} minutos")
        time.sleep(60)
        
        
    
b="descanso"
c="trabajo"    
while True:
    for a in range(0,4):
        tiempo(25,c)
        if a!=3:
            tiempo(6,b)
    tiempo(15,b)
  
    