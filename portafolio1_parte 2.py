"""
nombre:7
pasarAentero
entrada:
num=numero entero mayor que cero
salida:
numero entero
retrincciones:
numero con mayor que cero con decimales 
"""
def pasarAentero(num):
    if(isinstance(num,float) and num>0):
        #comprobacion de numero tipo flotante
        return pasarAentero_aux(num)
    else:
        return "El número debe ser positivo"

def pasarAentero_aux(num): 
    if(isinstance(num,float)):
        num=num%10**10*100000
        num=int(num)
        return pasarAentero_aux(num)
    elif(num%10==0):
        return pasarAentero_aux(num//10)
    else:
        return num


#--------------------------------------------------------
"""
nombre:
contarDigitosFlotante
entrada:
numero de tipo float
salida:
cantida de digito que tiene el numero
retrincciones:
numero de tipo flotante
"""

def contarDigitosFlotante(num):
    if(isinstance(num,float)and num>0):
        #comprobacion de numero tipo flotante
        num=num%10**10*100000
        num=int(num)
        if(num%10==0):
            return contarDigitosFlotante(num//10)
        else:
            return contarDigitosFlotante_aux(num)
    elif(num<0):
        return contarDigitosFlotante
    (num*-1)
    elif(num%10==0):
        return contarDigitosFlotante(num//10)
    elif(num>0):
        return contarDigitosFlotante_aux(num)
    else:
        return "digite un numero flotante"

def contarDigitosFlotante_aux(num):
    if(num==0):
        return 0
    else:
        return 1+contarDigitosFlotante_aux(num//10)

#------------------------------------------------------
"""
nombre:
indiceNumero
entrada:
num=numero entero positivo.
indice= numero entero positivo
salida:
numero que esta en la posicion que pidio en el indice
retrincciones:
indice=numero entero positivo mayor o igual que 0
num=numero entero mayor que cero 
"""  
def indiceNumero(num,indice):
    if(isinstance(num,int)and isinstance(indice,int)and num>0) :
        #comprobacion de numero entero positivo
        return indiceNumero_aux(num,indice)
    else:
        return "digite un numero entero positivo "

def indiceNumero_aux(num,indice):
    if(indice>=0):
        num=str(num)
        print(int(num[indice]))
    else:
        return
    

#---------------------------------------------------------------
"""
nombre:
contarNumero
entrada:
numeros entero positivo
salida:
suma de los numero que se pidio en el indice
retrincciones:
num=numero mayor que 0
indice=numero entero positivo mayor o igual que cero
indice2=numero entero positivo mayor que cero cero
"""
def contarNumero(num,indice,indice2):
    if(isinstance(num,int)and isinstance(indice,int)and isinstance(indice2,int)):
        #comprobacion de numero entero positivo
        return contarNumero_aux(num,indice,indice2)
    else:
        return "error,digite un numero entero positivo"

def contarNumero_aux(num,indice,indice2):
    if(num>0):
        num=str(num)
        print(int(num[indice])*10*1+int(num[indice2]))
    else:
        return "error,digite un numero entero positivo mayro que cero"
    
    




    
