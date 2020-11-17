import os

def criar_arquivo():
    flag = 0

    dir_path = os.path.dirname(os.path.realpath(__file__))
    lista_arquivos = os.listdir(dir_path)

    for item in lista_arquivos:
        if (item == "nome.txt"):
            flag = 1

    if(flag == 0):
        with open("nome.txt", 'w') as arquivo:
            pass


def cadastrar_pessoa():
    nome = input('DIGITE UM NOME: ')

    with open("nome.txt", 'a') as arquivo:
        arquivo.write(nome+"\n")


def listar_pessoas():
    lista = []
    with open("nome.txt") as arquivo:
        
        for line in arquivo:
            lista_retira_barra_n = line.split('\n')
            lista.append(lista_retira_barra_n[0])

    if(len(lista) == 0):
        print("NÃO HÁ NOMES CADASTRADOS")
    else:
        print (f"LISTA DE NOMES:\n {lista}\n")
    
    os.system('pause')