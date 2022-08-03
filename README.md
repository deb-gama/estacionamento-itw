# PROJETO ESTACIONAMENTO ITW

Este projeto tem como principal objetivo demonstrar alguns conceitos aprendidos na Aula de Python da formação ITW (Instruct The Woman) pela Womakers Code bem como habilidades anteriormente adquiridas.

Os principais conceitos presentes são:

- POO
- Herança
- Modelagem de classes
- Lógica em Python
- Conventional Commits
- GIT

## Bibiotecas utilizadas

- UUID

## Descrição das Regras de Negócio:

- Pátio com 50 vagas
- 25 vagas para motos e 25 vagas para carros
- Carros e motos identificados por suas placas
- Vagas identificadas por um número (id único)
- Carros só estacionam em vagas para carros, motos estacionam prefrencialmente em vagas para motos, mas podem estacionar em vagas de carro caso não hajam mais vagas de moto disponíveis
- Quando o dono vier buscar o carro, devemos poder saber automaticamente qual carro está em qual vaga (placa X- vaga - id X)
- Deve ser possível saber quantas vagas ainda estão disponíveis para estacionar- motos e carros

## Funcionamento do projeto

    Com base no desafio proposto, foi criado um sistema básico de controle de estacionamento que poderia ser utilizado em um negócio de qualquer porte. O projeto é customizado com o nome do estabelecimento e o número de vagas de motos e carros é criado dinamicamente assim como os Id's de cada vaga.

## Como utilizar:

- Execute o arquivo python pelo terminal da sua IDE e siga o passo-a-passo indicado no terminal. As regras de negócio foram atendidas com a criação de um menu que realiza as funções solicitadas.

**MENU**

- "Estacionar" realiza o cadastro do veículo e sua confirmação, busca uma das vagas disponíveis e associa o veículo a ela. Depois de removido o veiculo, a vaga é colocada novamente na lista de vagas livres para uso.

- "Remover" realiza a saída do veículo do estacionamento e do sistema através da sua placa.

- O "Status do Estacionamento" indica o total de vagas que o estacionamento possui e quantas vagas de cada tipo estão disponíveis no momento da consulta.

- "Buscar Carro" permite consultar os detalhes do veículo estacionado através de busca feita pela placa do mesmo. Esta opção retorna o ID e a placa do veículo como pede uma das regras, com algumas informações adicionais

- "Listar veículos estacionados" permite verificar uma lista completa de veículos estacionados no momento da consulta por tipo.

## Demonstrações adicionais

A partir da linha 366 existem funções criadas para validar as regras de negócio de forma automática com funções que chamam os métodos sem o uso da interação com o terminal. Para visualizá-los, comente o trecho de código referente a primeira execução e siga as instruções documentadas.

## Implementações futuras

Funcionalidade de alteração de determinados dados previamente cadastrados com o uso de Sette e Getters.
