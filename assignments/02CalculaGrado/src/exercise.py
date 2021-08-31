def calcula_grado(numero):
    if numero >= 0.9 and numero <= 1:
        nota = "A"
    elif numero > 0.8 and numero <= 0.9:
        nota = "B" 
    elif numero > 0.7 and numero <= 0.8:  
        nota = "C" 
    elif numero >= 0.6 and numero <= 0.7:
        nota = "D"   
    elif numero < 0.6 and numero > 0: 
        nota = "F"
    else:
        nota = "score incorrecto" 
    return nota              

def main():
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))
if __name__=='__main__':
 main()
