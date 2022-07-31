# REGRAS DE NEGÓCIO

# ESTACIONAMENTO:
#  - pátio com 50 vagas
#  - 25 vagas para motos e 25 vagas para carros
#  - carros e motos identificados por suas placas
#  - vagas identificadas por um número (id único)
#  - carros só estacionam em vagas para carros, motos estacionam prefrencialmente em vagas para motos, mas podem estacionar em vagas de carro caso não hajam mais vagas de moto disponíveis
#  - quando o dono vier buscar o carro, devemos poder saber automaticamente qual carro está em qual vaga (placa X- vaga - id X)
#  - deve serpossível saber quantas vagas ainda estão disponíveis para estacionar- motos e carros

import uuid

# devo saber o total vagas
# total de vagas de cada tipo
# total de vagas livres
class Estacionamento:
    def __init__(self):
        self.vagas_carro = 25
        self.vagas_moto = 25
        self.vagas_livres_carro = 25
        self.vagas_livres_moto = 25

    def status_estacionamento(self):
        self.total = self.vagas_carro + self.vagas_moto
        print(f'Este estacionamento possui um total de {self.total} vagas, sendo {self.vagas_moto} vagas de moto e {self.vagas_carro} vagas de carro.')
        print(f'No momento, existem {self.vagas_livres_moto} vagas livres para moto e {self.vagas_livres_carro} vagas livres para carros.')
        return self.total

    def vagas_livres_moto(self):
        print(f'O estacionamento possui {self.vagas_livres_moto} vagas livres para motos')
        return self.vagas_livres_moto

    def vagas_livres_carro(self):
        print(f'O estacionamento possui {self.vagas_livres_carro} vagas livres para motos')
        return self.vagas_livres_moto

    def estacionar_carro(self, carro, placa, vaga_id):
        self.carro = carro
        self.placa = placa
        self.vaga = vaga_id
        self.vagas_livres_carro -= 1
        print(f'O carro {self.carro}, placa {self.placa} está estacionado na vaga {self.vaga}')
        print(f'O total de vagas livres para carros agora é {self.vagas_livres_carro}')

        
# estacionamento = Estacionamento()
# estacionamento.status_estacionamento()
# estacionamento.estacionar_carro('Ford Ka','EXX-1234','1')
# estacionamento.estacionar_carro('Palio', 'EEE-2222', '2')
# estacionamento.status_estacionamento()

class Vaga:
    def __init__(self, placa):
        self.vaga_id = 0
        self.livre = False
        self.placa = placa
        self.tipo = 'Vaga'
    
class VagaMoto(Vaga):
    def __init__(self, placa):
        super().__init__(placa)
        self.vaga_id = uuid.uuid4()
        self.tipo = 'Moto'
        print(f'Vaga tipo: {self.tipo}, Placa: {self.placa}, Id - {self.vaga_id}')

class VagaCarro(Vaga):
    def __init__(self, placa):
        super().__init__(placa)
        self.vaga_id = uuid.uuid4()
        self.tipo = 'Carro'
        print(f'Vaga tipo: {self.tipo}, Placa: {self.placa}, Id - {self.vaga_id}')

# placas = ['eee-1234','eee-1235','eee-1236']
# vagas = []

# for placa in placas:
#     vaga = VagaMoto(placa)

# for placa in placas:
#     vaga = VagaCarro(placa)
  

class Carro:
    def __init__(self, placa, modelo):
        self.estacionado = False
        self.placa = placa
        self.modelo = modelo

        if self.estacionado is True:
            print(f'{self.modelo} placa {self.placa} - Estacionado')
        else :
            print(f'{self.modelo} placa {self.placa} - Aguardando para estacionar')



carro = Carro('EEE-1234','Palio')
