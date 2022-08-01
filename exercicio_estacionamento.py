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
        if len(self.carros_estacionados) > 0:
            for carro in self.carros_estacionados:
                print(carro)
        else:
            print('Não existem carros estacionados no momento.')


    def listar_motos_estacionadas(self):
        if len(self.motos_estacionadas) > 0:
            for moto in self.motos_estacionadas:
                print(moto)
        else:
            print('Não existem motos estacionadas no momento.')
    

    def estacionar_carro(self, modelo, placa, vaga_id):
        self.modelo = modelo
        self.placa = placa
        self.vaga = vaga_id
    
        if self.vagas_carro > 0:
            self.vagas_carro -= 1
            vaga_livre_carro = self.vagas_livres_carro.pop(0)
            vaga_livre_carro.placa = placa
            vaga_livre_carro.livre = False
            self.carros_estacionados.append(vaga_livre_carro)
            print(vaga_livre_carro)
      
            
    def estacionar_moto(self, modelo, placa, vaga_id):
        self.modelo = modelo
        self.placa = placa
        self.vaga = vaga_id
    
        if self.vagas_moto > 0:
            self.vagas_moto -= 1
            vaga_livre_moto = self.vagas_livres_moto.pop(0)
            vaga_livre_moto.placa = placa
            vaga_livre_moto.livre = False
            self.motos_estacionadas.append(vaga_livre_moto)
            print(vaga_livre_moto)
           
            

    def remover_carro(self,placa):
        for carro in self.carros_estacionados:
            if carro.placa == placa:
                carro_remover = self.carros_estacionados.index(carro)
                carro_removido = self.carros_estacionados.pop(carro_remover)
                carro_removido.livre = True
                self.vagas_livres_carro.append(carro_removido)
                print(f'Carro, placa: {placa} removido com sucesso.')
            else:
                print('Placa não encontrada.')


    def remover_moto(self,placa):
        for moto in self.motos_estacionadas:
            if moto.placa == placa:
                moto_remover = self.motos_estacionadas.index(moto)
                moto_removida = self.motos_estacionadas.pop(moto_remover)
                moto_removida.livre = True
                self.vagas_livres_moto.append(moto_removida)
                print(f'Moto, placa: {placa} removido com sucesso.')
            else:
                print('Placa não encontrada.')

        
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

print('PRIMEIRO STATUS')
estacionamento.status_estacionamento()

print('ESTACIONANDO CARRO')
estacionamento.estacionar_carro('Palio', 'EEE-1234', '2455353')
print('STATUS PÓS ESTACIONAMENTO CARRO')
estacionamento.status_estacionamento()


print('ESTACIONANDO MOTO')
estacionamento.estacionar_moto('PCX', 'FFF-0000', 'SYD353')
print('STATUS PÓS ESTACIONAMENTO CARRO E MOTO')
estacionamento.status_estacionamento()

print('LISTANDO CARROS E MOTOS ESTACIONADOS')
estacionamento.listar_carros_estacionados()
estacionamento.listar_motos_estacionadas()

print('REMOVENDO CARRO COM PLACA ERRADA')
estacionamento.remover_carro('OOO-1111')

print('REMOVENDO CARRO COM PLACA CORRETA')
estacionamento.remover_carro('EEE-1234')

print('STATUS PÓS REMOÇÃO DO CARRO')
estacionamento.status_estacionamento()

print('LISTANDO VAGAS DE CARRO')
estacionamento.listar_vagas_livres_carro()

print('REMOVENDO MOTO COM PLACA ERRADA')
estacionamento.remover_moto('EEE-1234')

print('REMOVENDO MOTO COM PLACA CORRETA')
estacionamento.remover_moto('FFF-0000')

print('STATUS PÓS REMOÇÃO DA MOTO')
estacionamento.status_estacionamento()

print('LISTANDO VAGAS DE MOTO')
estacionamento.listar_vagas_livres_moto()

print('LISTANDO VEICULOS ESTACIONADOS')
estacionamento.listar_carros_estacionados()
estacionamento.listar_motos_estacionadas()

# carro = Carro('EEE-1234','Palio')
