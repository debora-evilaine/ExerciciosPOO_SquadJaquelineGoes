# Crie uma classe que modele o objeto "carro".
# 2. Um carro tem os seguintes atributos: ligado, cor, modelo,
# velocidade.
# 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
# desacelera.
# 4. Crie uma instância da classe carro.
# 5. Faça o carro "andar" utilizando os métodos da sua classe.
# 6. Faça o carro "parar" utilizando os métodos da sua classe


class Carro():
    def __init__(self, ligado, cor, modelo, velocidade):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade
        self.__limite = 100

    def liga(self):
        self.ligado = True
        print("O carro está ligado.")
        print(self.ligado)

    def desliga(self):
        self.ligado = False
        print("O carro está desligado.")
        print(self.ligado)

    def acelera(self, kilometro):
        if kilometro > self.__limite:
            print("Você não pode ir acima do limite.")
        else:
            self.velocidade += kilometro
            print("O carro está acelerando!")
    
    def desacelera(self, kilometro):
        self.velocidade -= kilometro
        print("O carro está desacelerando!")


    def desligar(self):
        if self.velocidade > 0:
            while self.velocidade > 0:
                self.velocidade -= 1
            self.ligado = False
            print("O carro está desligado.")
            print(self.ligado)
        else:
            print("O carro já está desligado.")




carro1 = Carro(False, "vermelho", "Gol", 50)
print(vars(carro1))
carro1.desligar()


    

    
    



        
