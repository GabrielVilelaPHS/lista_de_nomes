import os
from funcoes import cadastrar_pessoa, listar_pessoas, criar_arquivo

criar_arquivo()

def controle_main(valor):
    
    if(valor == 1):
        cadastrar_pessoa()

    elif(valor == 2):
        listar_pessoas()

while(True):
    os.system('cls')

    print('--------- CONFIGURAÇÕES DE USUÁRIO --------\n')
    print('\nVOCE DESEJA FAZER?\n')
    print(f'(01) - CADASTRAR PESSOAS ')
    print(f'(02) - LISTAR PESSOAS CADASTRADAS ')


    while(True):
        try:
            resposta = int (input("\nRESPOSTA: "))

        except (ValueError, AttributeError):
            print('DIGITE UM NUMERO INTEIRO')
            os.system('pause')
            
        finally:

            if(resposta == 1 or resposta ==2 ):
                break
            else:
                print("NUMERO FORA DO INTERVALO")
                os.system('pause')
                continue
    val = input('\n' )
    controle_main(resposta)

