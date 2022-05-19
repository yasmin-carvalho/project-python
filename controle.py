from view import view
from modeloM import PedidoM


class Controle:

    def inicio(self):
        opcao = view.inicio()

        while opcao != 5:
            if opcao == 1:
                valores = view.coletaDadosPedido()
                dados = PedidoM.criaPedido(valores)
                status = PedidoM.cadastraPedido(dados)
                view.imprimeStatus(status)
                opcao = view.inicio()

            elif opcao == 2:
                orderid = view.coletaId()
                status = PedidoM.deletaPedido(orderid)
                view.imprimeStatus(status)
                opcao = view.inicio()

            elif opcao == 3:
                orderid = view.coletaId()
                registro = PedidoM.consultaPedido(orderid)
                view.imprimePedido(registro)
                opcao = view.inicio()

            elif opcao == 4:
                valores = view.coletaDadoUpdate()
                status = PedidoM.atualizaPedido(valores)
                view.imprimeStatus(status)
                opcao = view.inicio()


control = Controle()
control.inicio()
