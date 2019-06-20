class Carros:
    def __init__(self,consumoCombust):
        self.consumoCombust = consumoCombust
        self.quantidadeCombust = 0

    def andar(self,km):
        consumoCombust = km/self.consumoCombust
        self.quantidadeCombust = self.quantidadeCombust - consumoCombust

    def obterGasolina(self):
        print('Quantidade de combustível que resta: ', self.quantidadeCombust)

    def adicionarGasolina(self, quantidade):
        self.quantidadeCombust = self.quantidadeCombust + quantidade

minhaCaminhonete = Carros(15)
minhaCaminhonete.adicionarGasolina(20)
minhaCaminhonete.andar(100)
minhaCaminhonete.obterGasolina()
