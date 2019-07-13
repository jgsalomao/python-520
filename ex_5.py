
'''

Cenário:
Quando um passageiro passar na catraca,
dado que ele possui cŕeditos suficientes para
abri-lá, o programa deve descontar os créditos e
abrir a catraca.

'''

import datetime

import unittest


PRECO_DA_PASSAGEM = 5.0




#############################################################
# Erros
#############################################################

class SaldoInsuficiente(Exception):
    pass

class ConcessionariaDiferente(Exception):
    pass

class TicketVencido(Exception):
    pass




#############################################################
# Classes
#############################################################

class Ticket:
    
    def __init__(self, saldo, concessionaria, validade):
        self.saldo = saldo
        self.concessionaria = concessionaria
        self.validade = validade

class Catraca:
    
    def __init__(self, concessionaria):
        self.concessionaria = concessionaria
        self.travada = True

    def liberar(self, ticket):
        
        if ticket.saldo < PRECO_DA_PASSAGEM:
            raise SaldoInsuficiente

        if ticket.concessionaria != self.concessionaria:
        	raise ConcessionariaDiferente

       	if ticket.validade < datetime.datetime.today():
       		raise TicketVencido

        ticket.saldo -= PRECO_DA_PASSAGEM




#############################################################
# Testes
#############################################################

class Euvira(unittest.TestCase):

    def test_saldo_insuficiente(self):
        
        ticket = Ticket(
            saldo = PRECO_DA_PASSAGEM - 1,
            concessionaria ='sptrans',
            validade = datetime.datetime.today() + datetime.timedelta(days=365)
        )

        catraca = Catraca(
            concessionaria ='sptrans'
        )

        with self.assertRaises(SaldoInsuficiente):
            catraca.liberar(ticket)



    def teste_concessionaria_diferente(self):

    	ticket = Ticket(
            saldo = PRECO_DA_PASSAGEM + 1,
            concessionaria ='sptrans',
            validade = datetime.datetime.today() + datetime.timedelta(days=365)
        )

    	catraca = Catraca(
            concessionaria ='EMTU')

    	with self.assertRaises(ConcessionariaDiferente):
            catraca.liberar(ticket)



    def teste_ticket_vencido(self):

    	ticket = Ticket(
            saldo = PRECO_DA_PASSAGEM + 1,
            concessionaria = 'sptrans',
            validade = datetime.datetime.today() - datetime.timedelta(days = 365)
        )

    	catraca = Catraca(
            concessionaria ='sptrans')

    	with self.assertRaises(TicketVencido):
            catraca.liberar(ticket)



    def teste_fluxo_feliz(self):

    	ticket = Ticket(
    		saldo = PRECO_DA_PASSAGEM +1,
    		concessionaria = 'sptrans',
    		validade = datetime.datetime.today() + datetime.timedelta(days = 365),
    	)

    	catraca = Catraca(
            concessionaria ='sptrans')

    	catraca.liberar(ticket)

    	self.assertEqual(ticket.saldo, 1)



if __name__ == "__main__":
    
	unittest.main()
