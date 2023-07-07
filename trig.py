import math
import datetime

#creando el atributo pi
pi = math.pi

#creando una clase trig
class trig:
    
    def __init__ (self, angulo):
        self.angulo = angulo
        self.seno = math.sin(math.radians(angulo))
        self.coseno = math.cos(math.radians(angulo))
        self.tangente = math.tan(math.radians(angulo))
        
resultado = trig (pi)

print ("seno: ", resultado.seno)