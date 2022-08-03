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
    def __init__(self, nome):
        self.vagas_carro = 0
        self.vagas_moto = 0
        self.vagas_livres_carro = []
        self.vagas_livres_moto = []
        self.carros_estacionados = []
        self.motos_estacionadas = []
        self.nome = nome


    def status_estacionamento(self):
        self.total = self.vagas_carro + self.vagas_moto

        print(f'{self.nome} possui um total de {self.total} vagas, sendo {self.vagas_moto} vagas de moto e {self.vagas_carro} vagas de carro.')
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
                print(f'Moto, placa: {placa} removida com sucesso.')
            else:
                print('Placa não encontrada.')

    
    def consultar_por_placa(self, veiculo, placa):
        if veiculo == 'Moto':
            if len(self.motos_estacionadas) <= 0:
                print('Não existem motos estacionadas.')
            else:
                for moto in self.motos_estacionadas:
                    if moto.placa == placa:
                        print(moto)
                    else:
                        print('Placa não encontrada.')
        if veiculo == 'Carro':
            if len(self.carros_estacionados) <= 0:
                print('Não existem carros estacionadas.')
            else:
                for carro in self.carros_estacionados:
                    if len(self.carros_estacionados) <=0:
                        print('Não existem carros estacionados.')
                    if carro.placa == placa:
                        print(carro)
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






# # EXECUTANDO O CÓDIGO

# print('-------------------------------------------')
# print('Bem vindo ao Instruct Parking Lot! Por favor digite o nome do seu Estacionamento:')
# nome_estacionamento = str(input())
# estacionamento = Estacionamento(nome_estacionamento)
# estacionamento_login = True

# print(f'{nome_estacionamento} é ótimo tê-los conosco.Por favor informe a quantidade de vagas para motos:')
# qtdade_vagas_moto = int(input())

# print('Por favor nos informe a quantidade de vagas para carros:')
# qtdade_vagas_carro = int(input())


def criando_vagas(qtdade_vaga_carros, qtdade_vagas_motos):
    for _ in range(qtdade_vagas_motos):
        vaga_moto = VagaMoto()
        estacionamento.vagas_moto = qtdade_vagas_motos
        estacionamento.vagas_livres_moto.append(vaga_moto)

    for _ in range(qtdade_vaga_carros):
        vaga_carro = VagaCarro()
        estacionamento.vagas_carro = qtdade_vaga_carros
        estacionamento.vagas_livres_carro.append(vaga_carro)

# criando_vagas(qtdade_vagas_carro, qtdade_vagas_moto)

# print('-------------------------------------------')
# estacionamento.status_estacionamento()


# def menu():
#     print('-------------------------------------------')
#     msg_menu = 'O que você deseja fazer?\nEstacionar: digite "e"\nRemover veículo da vaga: "r"\nStatus do Estacionamento: "s"\nBuscar carro: "b"\nListar veiculos estacinados: "l"\nSair: "CTRL+c"'
#     print(msg_menu)

#     opcao = str(input()) 

#     if opcao == 's':
#         print('-------------------------------------------')
#         estacionamento.status_estacionamento()
 

#     if opcao == 'l':
#         print('-------------------------------------------')
#         print('Lista de carros: "c"\nLista de motos: "m')
#         tipo = str(input())

#         if tipo == 'c':
#             print('-------------------------------------------')
#             estacionamento.listar_carros_estacionados()

#         if tipo == 'm':
#             print('-------------------------------------------')
#             estacionamento.listar_motos_estacionadas()
        

#     if opcao == 'b':
#         print('-------------------------------------------')
#         print('O veiculo é um carro ou uma moto? Digite "m" para moto ou "c" para carro:')
#         tipo = str(input())

#         if tipo == 'c':
#             print('Digite a placa do veiculo que deseja consultar:')
#             placa = str(input())
#             veiculo = 'Carro'
#             print('-------------------------------------------')
#             estacionamento.consultar_por_placa(veiculo, placa)
       
#         if tipo == 'm':
#             print('Digite a placa do veículo que deseja consultar:')
#             placa = str((input))
#             veiculo = 'Moto'
#             print('-------------------------------------------')
#             estacionamento.remover_moto(placa, veiculo)
 
 

#     if opcao == 'r':
#         print('-------------------------------------------')
#         print('O veiculo é um carro ou uma moto? Digite "m" para moto ou "c" para carro:')
#         tipo = str(input())
#         print('-------------------------------------------')
#         print('Digite a placa do veículo que deseja remover:')
#         placa = str(input())

#         if tipo == 'c':
#             print('-------------------------------------------')
#             estacionamento.remover_carro(placa)
#         if tipo == 'm':
#             print('-------------------------------------------')
#             estacionamento.remover_moto(placa)
       

#     if opcao == 'e':
#         print('-------------------------------------------')
#         print('Que tipo de vaga você deseja cadastrar? Digite c para carro ou m para moto:')
#         tipo_de_vaga_opcao = str(input()) 
    

#         if tipo_de_vaga_opcao == 'c':
#             print('Digite o modelo do veículo:')
#             modelo = str(input())
#             print('Digite a placa do veiculo:')
#             placa = str(input())
#             carro_cadastrado = Carro(modelo,placa)
#             print(carro_cadastrado)
#             print('-------------------------------------------')
#             print('Estacionar? s para sim, n para não:')
#             resposta = str(input())
#             if resposta == 's':
#                 print('-------------------------------------------')
#                 print(f'Concluído! Detalhes da operação:')
#                 carro_cadastrado.estacionar(estacionamento)

#         if tipo_de_vaga_opcao == 'm':
#             print('Digite o modelo do veículo:')
#             modelo = str(input())
#             print('Digite a placa do veiculo:')
#             placa = str(input())
#             moto_cadastrada = Moto(modelo,placa)
#             print(moto_cadastrada)
#             print('-------------------------------------------')
#             print('Estacionar? s para sim, n para não:')
#             resposta = str(input())
#             if resposta == 's':
#                 print('-------------------------------------------')
#                 print(f'Concluído! Detalhes da operação:')
#                 moto_cadastrada.estacionar(estacionamento)


# while estacionamento:
#     menu()


# COBRINDO REGRAS DE NEGÓCIO

estacionamento = Estacionamento('Teste')

criando_vagas(25,25)

estacionamento.status_estacionamento()

moto = Moto('PCX', 'EEE-1234')
carro = Carro('Palio', 'EEE-1234')

# REGRA: Motos devem estacionar preferencialmente nas vagas de moto. Se acabarem, podem estacionar nas vagas livres de carro

# -----
# DESCOMENTE PARA VER RESPOSTA NO CONSOLE
# for _ in range(37):
#     estacionamento.estacionar_moto(moto.modelo, moto.placa)

# for _ in range(51):
#     estacionamento.estacionar_moto(moto.modelo, moto.placa)


# Carros estacionam apenas nas 25 vagas de carros disponíveis
# for _ in range(25):
#     estacionamento.estacionar_carro(carro.modelo, carro.placa)