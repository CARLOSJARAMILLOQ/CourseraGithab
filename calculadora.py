#funcion de entrada de datos
def entrada_datos():
    while True:    
        try: 
            numero1=float(input('ingrese el primer numero: '))
            numero2=float(input('ingrese el segundo numero '))
            return numero1,numero2
        except ValueError:
            print('Por favor ingrese solo numeros!\n')
            
#funcion de resultado
def resultados(operacion,resultado):
    print(f'el resultado de la {operacion} es: {resultado}\n')
#funcion de la suma
def suma(numero1,numero2):
    resultado = numero1 + numero2
    resultados("Suma",resultado)
#funcion de la Resta
def resta(numero1,numero2):
    resultado = numero1 - numero2
    resultados("Resta",resultado)
#funcion de la multiplicacion
def multiplicacion(numero1,numero2):
    resultado = numero1 * numero2
    resultados("Multiplicacion",resultado)
#funcion de la division
def division(numero1,numero2):
    if numero2 == 0:
        return 'no se puede dividir por cero.'
    else:
        resultado = numero1 / numero2
        resultados("Division",resultado)
#Funcion de potencia
#funcion de la calculadora basica
def calculadora():
    print('*** Calculadora basica ***')
    #inicio del programa
    while True:
        
        print('Seleccione la operacion a ejecutar como: 1, 2, 3, 4')
        print('1. SUMA')
        print('2. RESTA')
        print('3. MULTIPLICACION')
        print('4. DIVISION')
        print('5. SALIR')
        
        opcion=input('Ingrese una opcion: ')
        
        if opcion == "5":
            break
        try:
            if opcion == "1":
                numero1,numero2 =entrada_datos()
                print('*** SUMA ***')
                print(f'{suma(numero1,numero2)}\n')
            elif opcion == "2":
                numero1,numero2 =entrada_datos()
                print('*** RESTA ***')
                print(f'{resta(numero1,numero2)}\n')
            elif opcion == "3":
                numero1,numero2 =entrada_datos()
                print('*** MULTIPLICACION ***')
                print(f'{multiplicacion(numero1,numero2)}\n')
            elif opcion == "4":
                numero1,numero2 =entrada_datos()
                print('*** DIVISSION ***')
                print(f'{division(numero1,numero2)}\n')
            else:
                print('Seleccione una de las opciones\n')
        except ValueError:
            print("por favor, ingrese solo numeros.\n")

calculadora()  

