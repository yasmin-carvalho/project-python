from decimal import *
from datetime import datetime


class View():

    def inicio(self):
        return self.menu()

    def menu(self):
        print('#####MENU#####\n')
        print('[1] - Cadastrar um pedido')
        print('[2] - Deletar um pedido')
        print('[3] - Consultar um pedido')
        print('[4] - Alterar dados de um pedido')
        print('[5] - Sair\n')

        opcao = int(input('Escolha uma das opções acima: '))

        return opcao

    def coletaDadosPedido(self):
        orderid = input('Digite o identificador do pedido: ')
        customerid = input('Informe o cliente: ')
        employeeid = input('Informe o identificador do funcionario: ')
        orderdate = input('Informe a data do pedido AAAA-MM-DD: ')
        requireddate = input(
            'informe a data de fechamento do pedido AAAA-MM-DD: ')
        shippeddate = input('informe a data de envio do pedido AAAA-MM-DD: ')
        freight = input('Informe o frete: ')
        shipname = input('informe o local de envio: ')
        shipaddress = input('informe o endereço: ')
        shipcity = input('informe a cidade de envio: ')
        shipregion = input('informe a regiao de envio: ')
        shippostalcode = input('informe o CEP: ')
        shipcountry = input('informe o País: ')
        shipperid = input('informe o id do endereço de envio: ')

        ano, mes, dia = map(int, orderdate.split('-'))
        orderdate = datetime(ano, mes, dia)
        ano, mes, dia = map(int, requireddate.split('-'))
        requireddate = datetime(ano, mes, dia)
        ano, mes, dia = map(int, shippeddate.split('-'))
        shippeddate = datetime(ano, mes, dia)

        valores = [orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight,
                   shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid]
        return valores

    def coletaId(self):
        orderid = input('Digite o identificador do pedido: ')
        return orderid

    def coletaDadoUpdate(self):
        orderid = input('Digite o indentificador do pedido: ')
        campo = input('Digite o campo que deseja alterar: ')
        novoValor = input('Digite o novo valor: ')
        valores = [orderid, campo, novoValor]
        return valores

    def imprimePedido(self, pedido):
        if pedido is not None:
            print(f'Identificador: {pedido.pedido}')
            print(f'Cliente: {pedido.cliente}')
            print(f'Funcionário: {pedido.empregadoId}')
            print(f'Data do pedido: {pedido.data}')
            print(f'Data de fechamento do pedido: {pedido.requisicao}')
            print(f'Data de envio do pedido: {pedido.dataEnvio}')
            print(f'Frete: {pedido.frete}')
            print(f'Local de envio: {pedido.remetente}')
            print(f'Endereço: {pedido.endereco}')
            print(f'Cidade: {pedido.cidade}')
            print(f'Região: {pedido.regiao}')
            print(f'CEP: {pedido.postal}')
            print(f'País: {pedido.pais}')
            print(f'Id do endereço de envio: {pedido.remetenteId}')
        else:
            print('ERRO no processo')
            print('Pedido não identificado\n')

    def imprimeStatus(self, status):
        if status is not None:
            print(status)
        else:
            print('Erro no processo')


view = View()
