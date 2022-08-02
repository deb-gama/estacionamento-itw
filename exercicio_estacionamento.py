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
import os

# devo saber o total vagas
# total de vagas de cada tipo
# total de vagas livres
class Estacionamento():
    def __init__(self, nome):
        self.vagas_carro = 0
        self.vagas_moto = 0
        self.vagas_livres_carro = []
        self.vagas_livres_moto = []
        self.carros_estacionados = []
        self.motos_estacionadas = []
        self.nome = nome

    # def alterar_nome_estacionamento(self, nome):
    #     self.nome = nome

    def status_estacionamento(self):
        self.vagas_moto = len(self.vagas_livres_moto) + len(self.motos_estacionadas)
        self.vagas_carro = len(self.vagas_livres_carro) + len(self.carros_estacionados)
        self.total = self.vagas_carro + self.vagas_moto

        print(f'Este estacionamento possui um total de {self.total} vagas, sendo {self.vagas_moto} vagas de moto e {self.vagas_carro} vagas de carro.')
        print(f'No momento, existem {len(self.vagas_livres_moto)} vagas livres para moto e {len(self.vagas_livres_carro)} vagas livres para carros.')
    

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
    

    def estacionar_carro(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
    
        if self.vagas_carro > 0:
            self.vagas_carro -= 1
            vaga_livre_carro = self.vagas_livres_carro.pop(0)
            vaga_livre_carro.placa = placa
            vaga_livre_carro.livre = False
            self.carros_estacionados.append(vaga_livre_carro)
            print(vaga_livre_carro)
        else:
            print('Não existem vagas livres para carros no momento.')
      
            
    def estacionar_moto(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
    
        if self.vagas_moto > 0:
            self.vagas_moto -= 1
            vaga_livre_moto = self.vagas_livres_moto.pop(0)
            vaga_livre_moto.placa = placa
            vaga_livre_moto.livre = False
            self.motos_estacionadas.append(vaga_livre_moto)
            print(vaga_livre_moto)
    
        elif self.vagas_carro > 0:
            self.vagas_carro -= 1
            vaga_livre_moto = self.vagas_livres_carro.pop(0)
            vaga_livre_moto.placa = placa
            vaga_livre_moto.livre = False
            self.carros_estacionados.append(vaga_livre_moto)
            print(vaga_livre_moto)
        else:
            print('Não existem vagas livres para motos no momento.')

    def __str__(self) -> str:
        return 
           
            

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

    def __str__(self) -> str:
        if not self.livre:
            return f'Vaga tipo: {self.tipo}, Id - {self.vaga_id}, Status - Ocupada, Placa - {self.placa}'
        else:
            return f'Vaga tipo: {self.tipo}, Id - {self.vaga_id}, Status - Livre'


class Veiculo:
    def __init__(self):
        self.estacionado = False
        self.placa = ''
        self.modelo = ''
        self.tipo = 'Veículo'

    def estacionar(self, estacionamento):
        self.estacionado = True

        if self.tipo == 'Carro':
            estacionamento.estacionar_carro(self.modelo, self.placa)
            print('Carro estacionado')

        if self.tipo == 'Moto':
            estacionamento.estacionar_moto(self.modelo, self.placa)
            print('Moto estacionada')

    
    def sair_da_vaga(self,estacionamento, placa):
        self.estacionado = False

        if self.tipo == 'Carro':
            estacionamento.remover_carro(placa)

        if self.tipo == 'Moto':
            estacionamento.remover_moto(placa)
    


class Carro(Veiculo):
    def __init__(self, modelo, placa):
        super().__init__()
        self.tipo = 'Carro'
        self.placa = placa
        self.modelo = modelo

    def __str__(self) -> str:
        if self.estacionado is True:
            return f'{self.modelo} placa {self.placa} - Estacionado'
        else:
            return f'{self.modelo} placa {self.placa} - Aguardando para estacionar'



class Moto(Veiculo):
    def __init__(self, modelo, placa):
        super().__init__()
        self.tipo = 'Moto'
        self.placa = placa
        self.modelo = modelo

    def __str__(self) -> str:
        if self.estacionado is True:
            return f'{self.modelo} placa {self.placa} - Estacionado'
        else:
            return f'{self.modelo} placa {self.placa} - Aguardando para estacionar'






# EXECUTANDO O CÓDIGO

print('-------------------------------------------')
print('Bem vindo ao Instruct Parking Lot! Por favor digite o nome do seu Estacionamento:')
nome_estacionamento = str(input())
estacionamento = Estacionamento(nome_estacionamento)

print(f'{nome_estacionamento} é ótimo tê-los conosco.Por favor informe a quantidade de vagas para motos:')
qtdade_vagas_moto = int(input())

print('Por favor nos informe a quantidade de vagas para carros:')
qtdade_vagas_carro = int(input())


def criando_vagas(qtdade_vaga_carros, qtdade_vagas_motos):
    for _ in range(qtdade_vagas_motos):
        vaga_moto = VagaMoto()
        estacionamento.vagas_livres_moto.append(vaga_moto)

    for _ in range(qtdade_vaga_carros):
        vaga_carro = VagaCarro()
        estacionamento.vagas_livres_carro.append(vaga_carro)

criando_vagas(qtdade_vagas_carro, qtdade_vagas_moto)

print('-------------------------------------------')
estacionamento.status_estacionamento()

def menu():
    print('-------------------------------------------')
    msg_menu = 'O que você deseja fazer?\nPara estacionar digite "e"\nPara remover veiculo da vaga digite "r"\nPara consultar o status digite "s":'
    print(msg_menu)

    opcao_cadastrar = str(input()) 

    if opcao_cadastrar == 's':
        print('-------------------------------------------')
        estacionamento.status_estacionamento()

    if opcao_cadastrar == 'r':
        print('-------------------------------------------')
        print('O veiculo é um carro ou uma moto? Digite "m" para moto ou "c" para carro:')
        tipo = str(input())
        print('-------------------------------------------')
        print('Digite a placa do carro que deseja remover:')
        placa = str(input())

        # if tipo == 'c':
        #     veiculo = filter(placa,estacionamento.carros_estacionados)
        #     print(list(veiculo))
          
        # if tipo == 'm':
        #     veiculo = estacionamentomotos_estacionadas.find(placa)
        #     if veiculo != -1:
        #         print(estacionamento.motos_estacionadas[veiculo])
        else: 
            print('Veículo não encontrado Por favor confira o número da placa novamente.')

        

        # buscar veiculo pela placa
        # executar função de remoção
        
        
        

    if opcao_cadastrar == 'e':
        print('-------------------------------------------')
        print('Que tipo de vaga você deseja cadastrar? Digite c para carro ou m para moto:')
        tipo_de_vaga_opcao = str(input()) 
    

        if tipo_de_vaga_opcao == 'c':
            print('Digite o modelo do veículo:')
            modelo = str(input())
            print('Digite a placa do veiculo:')
            placa = str(input())
            carro_cadastrado = Carro(modelo,placa)
            print(carro_cadastrado)
            print('-------------------------------------------')
            print('Estacionar? s para sim, n para não:')
            resposta = str(input())
            if resposta == 's':
                print(f'Concluído! Detalhes da operação:')
                carro_cadastrado.estacionar(estacionamento)

        if tipo_de_vaga_opcao == 'm':
            print('Digite o modelo do veículo:')
            modelo = str(input())
            print('Digite a placa do veiculo:')
            placa = str(input())
            moto_cadastrada = Moto(modelo,placa)
            print(moto_cadastrada)
            print('-------------------------------------------')
            print('Estacionar? s para sim, n para não:')
            resposta = str(input())
            if resposta == 's':
                print(f'Concluído! Detalhes da operação:')
                moto_cadastrada.estacionar(estacionamento)

    


while estacionamento:
    menu()



# print('-------------------------------------------')
# print('CARRO DESOCUPANDO VAGA')
# carro_cadastrado.sair_da_vaga(estacionamento)

# print('-------------------------------------------')
# print('STATUS PÓS REMOÇÃO DO CARRO')
# estacionamento.status_estacionamento()

# print('-------------------------------------------')
# print('LISTANDO VAGAS DE CARRO, VAGA DESOCUPADA VOLTA PARA O FINAL DA LISTA DE VAGAS LIVRES')
# estacionamento.listar_vagas_livres_carro()

# print('-------------------------------------------')
# print('STATUS DO CARRO QUE ACABOU DE SAIR DA VAGA')
# print(carro_cadastrado)


# print('-------------------------------------------')
# print('MOTO DESOCUPANDO VAGA')
# moto_cadastrada.sair_da_vaga(estacionamento)

# print('-------------------------------------------')
# print('STATUS PÓS REMOÇÃO DA MOTO')
# estacionamento.status_estacionamento()

# print('-------------------------------------------')
# print('LISTANDO VAGAS DE MOTO')
# estacionamento.listar_vagas_livres_moto()


# print('-------------------------------------------')
# print('LISTANDO VEICULOS ESTACIONADOS')
# estacionamento.listar_carros_estacionados()
# estacionamento.listar_motos_estacionadas()

