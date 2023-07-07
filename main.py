import math

#imprime fecha y hora
import datetime

from trig import trig

fechaYhora = datetime.datetime.now()

archivoTrig = trig (math.pi)

# Abrir el archivo en modo escritura
with open("log.txt", "w") as archivo:
    archivo.write("Resultado de las operaciones:\n\n")

while True:
    
    print ("Fecha y hora:", fechaYhora)
    print ("que operacion te gustaria realizar:\n")
    
    print ("si quieres saber el seno de pi, presiona 1 \n")
    
    print ("si quieres saber el coseno de pi presiona 2 \n")
    
    print ("si quieres saber la tangente de pi, presiona 3 \n")
    
    print ("si quieres salir del programa, escribe salir \n")
    
    pregunta = input ("indique que operacion deseas realizar: \n")
    archivo.write("Operación seleccionada: " + pregunta + "\n")
 
    
    if pregunta == "salir":
        archivo.write("Programa finalizado.\n")
        break
    
    preguntaInt = int(pregunta)
    resultado = None
    
    
    if preguntaInt == 1:
        resultado = archivoTrig.seno
        print("El seno de pi es:", resultado)
        archivo.write("El seno de pi es: " + str(resultado) + "\n")
        
    elif preguntaInt == 2:
        resultado = archivoTrig.coseno
        print("El coseno de pi es:", resultado)
        archivo.write("El coseno de pi es: " + str(resultado) + "\n")
        
    elif preguntaInt == 3: 
        resultado = archivoTrig.tangente
        print("La tangente de pi es:", resultado)
        archivo.write("La tangente de pi es: " + str(resultado) + "\n")
        
    else:
        print ("error al ingresar datos. Selecciona una opcion valida. \n")
        archivo.write("Error al ingresar datos. Selecciona una opción válida.\n")
        
    archivo.write("\n")
    

            
  


        
    