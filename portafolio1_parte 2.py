"""
nombre:
pasarAentero
entrada:
num=numero entero mayor que cero
salida:
numero entero
retrincciones:
numero mayor que cero con decimales 
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
        return suma_aux(num,0)

def suma_aux(num,indice):
    if(num==0):
        return 0
    else:
        suma=num%10*10**indice
        return suma+suma_aux(num//10,indice+1)


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
        return contarDigitosFlotante(num*-1)
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
indice
entrada:
num=numero entero positivo.
indice= numero entero positivo
salida:
numero que esta en la posicion que pidio en el indice
retrincciones:
indice=numero entero positivo mayor o igual que 0
num=numero entero mayor que cero 
"""  
def indice(num,indice):
    if(isinstance(num,int)and num>0 and isinstance(indice,int)and indice>=0):
        largo= largo_aux(num)
        comparar=num-1
        return indice_aux(num,indice+1,largo,comparar)
    else:
        return "error, digite un numero entero positivo"

def indice_aux(num,indice,largo,comparar):
    if(num==0):
        return 0
    elif(num<comparar)and num>10:
        suma=num%10
        return suma+indice_aux(num%10//10,indice,largo,comparar)
    elif(num<comparar)and num<10:
        return num+indice_aux(num//10,indice,largo,comparar)
    elif(indice==largo):
        return num%10+indice_aux(num%10//10,indice,largo,comparar)
    else:
        largo=largo-indice
        return indice_aux(num//(10**largo),indice,largo,comparar)

def largo_aux(num):
    if(num==0):
        return 0
    else:
        return 1+largo_aux(num//10)

#---------------------------------------------------------------
"""
nombre:
sumaIndice
entrada:
numeros entero positivo
salida:
suma de los numero que se pidio en el indice
retrincciones:
num=numero entero mayor que 0
indice=numero entero positivo mayor o igual que cero
indice2=numero entero positivo mayor que cero cero
"""
def sumaIndice(num,indice1,indice2):
    if(isinstance(num,int)and isinstance(indice1,int)and isinstance(indice2,int)and indice1>=0 and indice2>=0):
        if(num>0):
            numeroAsumar=indice(num,indice1)
            numeroAsumar2=indice(num,indice2)
            suma=numeroAsumar*10+numeroAsumar2
            return suma+sumaIndice(num%10//10,numeroAsumar,numeroAsumar)
        else:
            return 0
    else:
        return "error,digite un numero entero positivo"
    
    




    


