#Reto # 5 - Julio Cesar Palacio Ojeda - Grupo 23
#Aplicación para registrar los datos de los estudiantes que se postulan al departamento de 
#prácticas académicas de una de las universidades extranjeras.
#Datos de Entrada: lista con todos los códigos de identificación de los estudiantes
#que se han postulado

import datetime

#Inicializamos lista de postulados (enviada por el departamento de
#prácticas académica de la universidad) 
lista_postu = [1001,1002,1003,1004,1005,1006,11125,10009,90125,9901254]
#Inicializar variables
cola = []
inscritos = {}

#función asignación de turno:
#1.Valida que el documento del estudiante este en la lista enviada por el departamento de prácticas

def asig_turno(lista_postu, codigo):    
    if codigo in lista_postu:
        cola.append(codigo)
    
    return cola          
    

#función llama al estudiante respectivo de acuerdo con su posición en la cola y
#registra los siguientes datos en un diccionario:
##Identificación
##Nombre
##Edad
##Inscrito a prácticas (Ingeniería civil, Ingeniería de sistemas, Ingeniería electrónica)
##Fecha y hora del registro

def inscrito_dpa(cola):
    identif = cola.pop(0)
    print('Estudiante con numero de identificación #: ', identif)
    nombre = str(input('Ingrese su nombre: '))
    edad = int(input('Ingrese su edad: '))
    print('Ingrese la facultad donde va a relizar la practica:\n1. Ingenieria Civil\n2. Ingenieria de Sistemas\n3. Ingenieria Electronica')
    facultad = int(input())
    hora_registro = datetime.datetime.now()

    inscritos[identif] = (nombre,edad, facultad, hora_registro)

    return inscritos

#funcion que cuenta y da el % de los inscritos por tipo de programa 
def inscritos_porprograma(inscritos):
    contar1=0
    contar2=0
    contar3=0
    
    for i in inscritos:
        if inscritos[i][2] == 1:
            contar1 += 1
        if inscritos[i][2] == 2:
            contar2 += 1    
        if inscritos[i][2] == 3:
            contar3 += 1    

    print('El total de inscritos en la facultad de Ingenieria Civil son: ', contar1)
    print('El total de inscritos en la facultad de Ingenieria de Sistemas son: ', contar2)
    print('El total de inscritos en la facultad de Ingenieria Electronica son: ', contar3)

    total = contar1+contar2+contar3

    print('El % de inscritos en la facultad de Ingenieria Civil es: ', round(contar1/total, 2))
    print('El % de inscritos en la facultad de Ingenieria de Sistemas es: ', round(contar2/total, 2))
    print('El % de inscritos en la facultad de Ingenieria Electronica es: ', round(contar3/total, 2)) 

    
#Ciclo para asignar un turno al estudiante de manera consecutiva de acuerdo con el orden
#de llegada
#2.Valida que el estudiante no se haya inscrito ya
n = int(input('Ingrese la cantidad de estudiantes que llegaron: '))
i=0
while i<n:
    cod = int(input('Ingrese el número de identificación del estudiante que se postula: '))
    if cod not in lista_postu:
        print('El estudiante no se encuentra postulado\n')
    elif cod not in inscritos.keys():
        asig_turno(lista_postu, cod)
        inscrito_dpa(cola)       
    else:
        print('Estudiante ya se encuentra inscrito\n')

    i += 1    

    
print('El total de inscritos a practica son: ', len(inscritos))
inscritos_porprograma(inscritos)


###################################RESULT##################################################   

#######################ESTE PROGRAMA IMPRIMIRA LO SIGUIENTE#################################    
##Ingrese la cantidad de estudiantes que llegaron: 6
##Ingrese el número de identificación del estudiante que se postula: 1001
##Estudiante con numero de identificación #:  1001
##Ingrese su nombre: julio palacio
##Ingrese su edad: 35
##Ingrese la facultad donde va a relizar la practica:
##1. Ingenieria Civil
##2. Ingenieria de Sistemas
##3. Ingenieria Electronica
##1
##Ingrese el número de identificación del estudiante que se postula: 1002
##Estudiante con numero de identificación #:  1002
##Ingrese su nombre: marta gomez
##Ingrese su edad: 45
##Ingrese la facultad donde va a relizar la practica:
##1. Ingenieria Civil
##2. Ingenieria de Sistemas
##3. Ingenieria Electronica
##1
##Ingrese el número de identificación del estudiante que se postula: 1003
##Estudiante con numero de identificación #:  1003
##Ingrese su nombre: jaime palacio
##Ingrese su edad: 36
##Ingrese la facultad donde va a relizar la practica:
##1. Ingenieria Civil
##2. Ingenieria de Sistemas
##3. Ingenieria Electronica
##2
##Ingrese el número de identificación del estudiante que se postula: 1004
##Estudiante con numero de identificación #:  1004
##Ingrese su nombre: oscar heinz
##Ingrese su edad: 30
##Ingrese la facultad donde va a relizar la practica:
##1. Ingenieria Civil
##2. Ingenieria de Sistemas
##3. Ingenieria Electronica
##2
##Ingrese el número de identificación del estudiante que se postula: 1005
##Estudiante con numero de identificación #:  1005
##Ingrese su nombre: michael jaxko
##Ingrese su edad: 45
##Ingrese la facultad donde va a relizar la practica:
##1. Ingenieria Civil
##2. Ingenieria de Sistemas
##3. Ingenieria Electronica
##3
##Ingrese el número de identificación del estudiante que se postula: 1006
##Estudiante con numero de identificación #:  1006
##Ingrese su nombre: axl rose
##Ingrese su edad: 50
##Ingrese la facultad donde va a relizar la practica:
##1. Ingenieria Civil
##2. Ingenieria de Sistemas
##3. Ingenieria Electronica
##3
##El total de inscritos a practica son:  6
##El total de inscritos en la facultad de Ingenieria Civil son:  2
##El total de inscritos en la facultad de Ingenieria de Sistemas son:  2
##El total de inscritos en la facultad de Ingenieria Electronica son:  2
##El % de inscritos en la facultad de Ingenieria Civil es:  0.33
##El % de inscritos en la facultad de Ingenieria de Sistemas es:  0.33
##El % de inscritos en la facultad de Ingenieria Electronica es:  0.33    

    
    







