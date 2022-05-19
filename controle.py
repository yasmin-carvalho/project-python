from view import view
from modelo import Pedido


class Controle:

    def inicio(self):
        opcao = view.inicio()

        while opcao != 5:
            if opcao == 1:
                valores = view.coletaDadosPedido()
                dados = Pedido.criaPedido(valores)
                status = Pedido.cadastraPedido(dados)
                view.imprimeStatus(status)
                opcao = view.inicio()

            elif opcao == 2:
                orderid = view.coletaId()
                status = Pedido.deletaPedido(orderid)
                view.imprimeStatus(status)
                opcao = view.inicio()

            elif opcao == 3:
                orderid = view.coletaId()
                registro = Pedido.consultaPedido(orderid)
                view.imprimePedido(registro)
                opcao = view.inicio()

            elif opcao == 4:
                valores = view.coletaDadoUpdate()
                status = Pedido.atualizavaloresupdate(valores)
                view.imprimeStatus(status)
                opcao = view.inicio()


controlller = Controle()
controlller.inicio()
