from config import config
from datetime import datetime
from decimal import *
from psycopg2.extensions import AsIs
import psycopg2


class Costumers():
    def consultaCostumers(id):
        stringSQL = 'SELECT * FROM northwind.customers WHERE customerid = %s;'
        registro = config.consultaBD(config, stringSQL, [id])
        if(len(registro[1]) != 0):
            return False
        else:
            return True


class Employees():
    def consultaEmployees(id):
        stringSQL = 'SELECT * FROM northwind.employees WHERE employeeid = %s;'
        registro = config.consultaBD(config, stringSQL, [id])
        if(len(registro[1]) != 0):
            return False
        else:
            return True


class Orders_details():
    def deletarorders_details(id):
        stringSQL = 'DELETE FROM northwind.order_details WHERE orderid = %s;'
        status = config.alteraBD(config, stringSQL, [id])


def shiperidTratamento(listaValores):
    if listaValores[13] == None:
        return -1
    else:
        return listaValores[13]


class clienteInvalido(Exception):
    pass


class funcionarioInvalido(Exception):
    pass


class Pedido():
    def __init__(self, orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid):
        self.pedido = orderid
        self.cliente = customerid
        self.empregadoId = employeeid
        self.data = orderdate
        self.requisicao = requireddate
        self.dataEnvio = shippeddate
        self.frete = freight
        self.remetente = shipname
        self.endereco = shipaddress
        self.cidade = shipcity
        self.regiao = shipregion
        self.postal = shippostalcode
        self.pais = shipcountry
        self.remetenteId = shipperid

    def criaPedido(listaValores):
        return Pedido(int(listaValores[0]), str(listaValores[1]),
                      int(listaValores[2]), listaValores[3], listaValores[4],
                      listaValores[5], Decimal(
                          listaValores[6]), str(listaValores[7]),
                      str(listaValores[8]), str(listaValores[9]),
                      str(listaValores[10]), str(
            listaValores[11]), str(listaValores[12]),
            int(shiperidTratamento(listaValores)))

    def cadastraPedido(pedido):
        string_sql = 'INSERT INTO northwind.orderns (orderid, customerid, employeeid, orderdate, requireddate, shippeddate, ' \
                     'freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        novo_registro = (pedido.pedido, pedido.cliente, pedido.empregadoId, pedido.data, pedido.requisicao,
                         pedido.dataEnvio, pedido.frete, pedido.remetente, pedido.endereco, pedido.cidade, pedido.regiao,
                         pedido.postal, pedido.pais, pedido.remetenteId)

        try:
            if Costumers.consultaCostumers(pedido.cliente):
                raise clienteInvalido()
            elif Employees.consultaEmployees(pedido.empregadoId):
                raise funcionarioInvalido()
        except clienteInvalido:
            return('Cliente não encontrado!')
        except funcionarioInvalido:
            return('Funcionário não encontrado!')
        else:
            status = config.alteraBD(config, string_sql, novo_registro)
            return status

    def deletaPedido(id):
        Orders_details.deletarorders_details(id)
        string_sql = 'DELETE FROM northwind.orders WHERE orderid = %s;'
        status = config.alteraBD(config, string_sql, [id])
        return status

    def consultaPedido(id):
        string_sql = 'SELECT * FROM northwind.orders WHERE orderid = %s;'
        registros = config.consultaBD(config, string_sql, [id])
        if(len(registros[1]) != 0):
            pedido = Pedido.criaPedido(registros[1][0])
            return pedido
        else:
            return None

    def atualizavaloresupdate(l):
        string_sql = """UPDATE northwind.orders SET %s = %s WHERE orderid = %s"""
        parametros = ((AsIs(l[1])), int(l[2]), int(l[0]))

        #status = config.alteraBD(config, string_sql, parametros)
        # return status
