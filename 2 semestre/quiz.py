class calculadora:
    valor1=0
    valor2=0
    valor3=0

    def inicio(self,):
        pregunta= input ("¿que operacion desea realizar? suma, resta, multiplicacion o divison: ")
        valor1= int(input ("ingrese el primer valor "))
        valor2= int(input ("ingrese el segundo valor "))
        valor3= int(input ("ingrese el tercer valor" ))

        
        if pregunta == 'suma':
            print("el resultado es: ", valor1+valor2+valor3)
        elif pregunta== 'resta':
            self.valor1, self.valor2= input().split()
            print("el resultado es: ", valor1-valor2)

        elif pregunta== 'multiplicacion':
            self.valor1, self.valor2= input().split()
            print("el resultado es: ", valor1*valor2)

        elif pregunta == 'division':
            self.valor1, self.valor2= input().split()
            print("el resultado es: ", valor1%valor2)

        else:
            print ('error')




operacion=calculadora()
operacion.inicio()