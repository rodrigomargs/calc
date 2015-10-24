# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "rodma"
__date__ = "$18-oct-2015 16:17:33$"

bucle=1
while bucle!=0:
    print"******************"
    print"Escoge una opcion:"
    print"1)Sumar           "
    print"2)Restar          "
    print"3)Multiplicar     "
    print"4)Dividir         "
    print"5)Salir           "
    print"******************"
    select=input("Opcion:")
    if select==5:
        bucle=0
        print"Hasta pronto!"
    else:
        numa=input("Ingrese el primer numero:")
        numb=input("Ingrese el segundo numero:")
        if select==1:
            print"Suma de los numeros:",numa+numb
        if select==2:
            print"Resta de los numeros:",numa-numb
        if select==3:
         print"Multiplicacion de los numeros:",numa*numb
        if select==4:
            if numb ==0:
                print"Numeros diferentes de cero para dividir"
            else:
                print"Division de los numeros:",numa/numb
    
    
