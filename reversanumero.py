
        

""""
nombre reversanumero
entrada:
n: entero positivo
salidas:
entero mayor a cero que el numero en
restriciones:
entero positivo mayor o igual a cero
"""
def reversaNum(num):
    if(isinstance(num, int)):
        if(num >=0):
            if(num <=10):
                return num
            else:
                return reversaNum_aux(num, contarDigitos_v3(num))
        else:
            return print("El número debe ser positivo")
    else:
        return print("Error: el numero no es entero")

def reversaNum_aux(num, largo):
    if largo == 0:
        return 0
    else:
        return(num %10)*(10**(largo -1)) + reversaNum_aux(num//10, largo - 1)





def contarDigitos_v3(num):
    if(isinstance(num, int)==False):
        return print("error")
    elif(num ==0):
        return 1
    else:
        return contarDigitos_aux(num)
    
def contarDigitos_aux(n):
    if(n == 0):
        return 0
    else:
        return 1 + contarDigitos_aux(n//10)





    
       

        
        
