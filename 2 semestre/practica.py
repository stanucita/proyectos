class Triangulo:
    def inicializar(self):

        self.ladoa, self.ladob, self.ladoc= input().split()

    def imprimir(self):

        print("lado a:", self.ladoa)
        print("lado b:", self.ladob)
        print("lado c:", self.ladoc)
    
    def mayor(self):
        
        if self.ladoa>self.ladob and self.ladoa>self.ladoc:
            print("el lado mayor es: ", self.ladoa)
        elif self.ladob>self.ladoc:
            print("el lado mayor es: ", self.ladob)
        else:
            print ("el lado mayor es: ", self.ladoc)

    def tipo(self):
        if self.ladoa== self.ladob and self.ladoa!=self.ladoc:
            print("el triangulo es isoceles")
        elif self.ladoa!= self.ladob and self.ladoa!=self.ladoc:
            print("el triangulo es escaleno")
        else:
            print("el triangulo es equilatero")

figura=Triangulo()
figura.inicializar()
figura.imprimir()
figura.mayor()
figura.tipo()