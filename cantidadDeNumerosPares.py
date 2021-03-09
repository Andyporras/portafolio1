"""
nombre:
contadorDepares
entrada:
num: numero entero positivo 
salidad:
cantidad de numero pares que tiene el numero digita
restrinciones:
numero entero positivo mayor a cero

"""


def contadorDepares(num):
    if(isinstance(num,int) and num>=0):
        if(num==0):
            return 0
        elif(num%2)==0:
            return 1+contadorDepares(num//10)
        else:
            return contadorDepares(num//10)
    else:
        return print("dijite un entero positivo")

#---------------------------------------------------------------------------




def cantidadDeNumerosPares(num):
   if(isinstance(num,int)and num>0):
      return cantidadDeNumerosPares_aux(num,0)
   else:
      return "digite un numero entero positivo"
   

def cantidadDeNumerosPares_aux(numVerified,result):
   if(numVerified==0):
      return result
   elif(numVerified%2==0):
      return cantidadDeNumerosPares_aux(numVerified//10,result +1)
   else:
      return cantidadDeNumerosPares_aux(numVerified//10,result)
   
      
