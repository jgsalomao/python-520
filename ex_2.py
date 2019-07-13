
def foo(a, b, c, *args):
    print(a, b, c)

foo(1, 2, 3)

args = [ 1, 2, 3, 4 ]
foo(*args)

def receber_notas():

    lista_de_notas= []
    finalizado = False

    while not finalizado:

        nota = input('Digite a nota ou "q" para sair: ')

        if nota == 'q':
            finalizado = True
        else:
            lista_de_notas.append(nota)

    return lista_de_notas

def processar_nota(nota):
    pass

def processar_notas(lista_de_notas):
    for nota in lista_de_notas:
processar_nota(nota)