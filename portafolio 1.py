
    
def divisores(num):
    if(isinstance(num,int) and num>0):
        return divisores_aux(num,num)
    else:
        return "El número debe ser mayor a cero y positivo"

def divisores_aux(num,contador):
    if contador==0:
        return None
    else:
        if(num%contador)==0:
            print(contador)
        return divisores_aux(num,contador-1)
#--------------------------------------------------------------------

def multiplicarRecursivo(num,factor):
    if(isinstance(num,int)and isinstance(factor,int)):
        return multiplicarRecursivo_aux(num,factor)
    else:
        return "digite un numero entero positivo"

def multiplicarRecursivo_aux(num,factor):
    if(factor==0):
        return 0
    else:
        return num+multiplicarRecursivo_aux(num,factor-1)

#-------------------------------------------------------------------


def divisionRecursivo(divisor,dividendo):
    if(isinstance(divisor,int)and isinstance(dividendo,int)and divisor>0):
       return divisionRecursivo_aux(dividendo,divisor,0)
    else:
        return "digite un numero entero positivo"

def divisionRecursivo_aux(divisor,dividendo,contar):
    if(divisor==contar):
        print("El resultado de la division es: ")
        return 0
    elif(contar>divisor):
        print("El resultado de la division es: ")
        return -1
    else:
       return 1+divisionRecursivo_aux(divisor,dividendo,contar+dividendo)

    
#-------------------------------------------------------------------------------------------
        

























    
