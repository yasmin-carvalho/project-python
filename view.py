from decimal import *
from datetime import datetime


class View():

    def inicio(self):
        return self.menu()

    def menu(self):
        print('--- MENU ---')
        print('[1] - Cadastrar um produto')
        print('[2] - Deletar um produto')
        print('[3] - Consultar um produto')
        print('[4] - Alterar dados de um produto')
        print('[5] - Sair\n')

        opcao = int(input('Digite a opção desejada: '))

        return opcao

    def coletadadosproduto(self):
        productid = input('Digite o identificador do produto: ')
        productname = input('Digite o nome do produto: ')
        supplierid = input('Digite o identificador do fornecedor: ')
        categoryid = input('Digite o identificador da categoria: ')
        quantityperunit = input(
            'Digite a quantidade de produtos por embalagem: ')
        unitprice = input('Digite o preço do produto: ')
        unitsinstock = input('Digite a quantidade de unidade no estoque: ')
        unitsonorder = input(
            'Digite a quantidade de unidades disponiveis para venda: ')
        reorderlevel = input('Digite nivel do produto: ')
        discontinued = input('O produto esta descontinuado?: ')
        valores = [productid, productname, supplierid, categoryid, quantityperunit, unitprice,
                   unitsinstock, unitsonorder, reorderlevel, discontinued]
        return valores

    def recebeCodproduto(self):
        productid = input('Digite o identificador do produto: ')
        return productid

    def coletaMod(self):
        productid = input('Digite o indentificador do produto: ')
        campo = input('Digite o campo que deseja alterar: ')
        newValue = input('Digite o novo valor: ')
        valores = [productid, campo, newValue]
        return valores

    def imprimeProduto(self, prod):
        if prod is not None:
            print(f'Id: {prod.id}')
            print(f'Nome: {prod.nome}')
            print(f'Fornecedor: {prod.fornecedor}')
            print(f'Categoria: {prod.categoria}')
            print(f'Quantidade por embalagem: {prod.quantidadeEmbalagem}')
            print(f'Preço Unitario: {prod.precoUnitario}')
            print(f'Estoque: {prod.estoque}')
            print(f'Vendas: {prod.vendas}')
            print(f'Nivel: {prod.nivel}')
            print(f'Descontinuado: {prod.descontinuado}\n\n')

        else:
            print('Produto não encontrado!')

    def imprimeStatus(self, string):
        print(string)


view = View()
