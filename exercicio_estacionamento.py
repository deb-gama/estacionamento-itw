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
class Estacionamento():
    def __init__(self):
        self.vagas_carro = 0
        self.vagas_moto = 0
        self.vagas_livres_carro = []
        self.vagas_livres_moto = []
        self.carros_estacionados = []
        self.motos_estacionadas = []

    def status_estacionamento(self):
        self.vagas_moto = len(self.vagas_livres_moto) + len(self.motos_estacionadas)
        self.vagas_carro = len(self.vagas_livres_carro) + len(self.carros_estacionados)
        self.total = self.vagas_carro + self.vagas_moto

        print(f'Este estacionamento possui um total de {self.total} vagas, sendo {self.vagas_moto} vagas de moto e {self.vagas_carro} vagas de carro.')
        print(f'No momento, existem {len(self.vagas_livres_moto)} vagas livres para moto e {len(self.vagas_livres_carro)} vagas livres para carros.')
        return self.total

    def listar_vagas_livres_moto(self):
        for vaga in self.vagas_livres_moto:
            print(vaga)
    

    def listar_vagas_livres_carro(self):
        for vaga in self.vagas_livres_carro:
            print(vaga)
    

    def listar_carros_estacionados(self):
        for carro in self.carros_estacionados:
            print(carro)
    

    def estacionar_carro(self, carro, placa, vaga_id):
        self.carro = carro
        self.placa = placa
        self.vaga = vaga_id
    
        if self.vagas_carro > 0:
            self.vagas_carro -= 1
            vaga_livre_carro = self.vagas_livres_carro.pop(0)
            vaga_livre_carro.placa = placa
            vaga_livre_carro.livre = False
            self.carros_estacionados.append(vaga_livre_carro)
            self.listar_carros_estacionados()
            
            
                
        # print(f'O carro {self.carro}, placa {self.placa} está estacionado na vaga {self.vaga}')
        # print(f'O total de vagas livres para carros agora é {self.vagas_carro}')

        
# estacionamento = Estacionamento()
# estacionamento.status_estacionamento()
# estacionamento.estacionar_carro('Ford Ka','EXX-1234','1')
# estacionamento.estacionar_carro('Palio', 'EEE-2222', '2')
# estacionamento.status_estacionamento()

class Vaga:
    def __init__(self):
        self.vaga_id = 0
        self.livre = False
        self.placa = ''
        self.tipo = 'Vaga'
    
class VagaMoto(Vaga):
    def __init__(self):
        super().__init__()
        self.vaga_id = uuid.uuid4()
        self.tipo = 'Moto'
        self.livre = True
        # print(f'Vaga tipo: {self.tipo}, Id - {self.vaga_id}')

    def __str__(self) -> str:
        if not self.livre:
            return f'Vaga tipo: {self.tipo}, Id - {self.vaga_id}, Status - Ocupada, Placa: {self.placa}'
        else:
            return f'Vaga tipo: {self.tipo}, Id - {self.vaga_id}, Status - Livre'


class VagaCarro(Vaga):
    def __init__(self):
        super().__init__()
        self.vaga_id = uuid.uuid4()
        self.tipo = 'Carro'
        self.livre = True
        # print(f'Vaga tipo: {self.tipo}, Id - {self.vaga_id}')

    def __str__(self) -> str:
        if not self.livre:
            return f'Vaga tipo: {self.tipo}, Id - {self.vaga_id}, Status - Ocupada, Placa - {self.placa}'
        else:
            return f'Vaga tipo: {self.tipo}, Id - {self.vaga_id}, Status - Livre'




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



estacionamento = Estacionamento()

def criando_vagas():
    for _ in range(25):
        vaga_moto = VagaMoto()
        estacionamento.vagas_livres_moto.append(vaga_moto)
        vaga_carro = VagaCarro()
        estacionamento.vagas_livres_carro.append(vaga_carro)

criando_vagas()
estacionamento.status_estacionamento()

estacionamento.estacionar_carro('Palio', 'EEE-1234', '2455353')
estacionamento.status_estacionamento()
estacionamento.listar_carros_estacionados()




# carro = Carro('EEE-1234','Palio')
