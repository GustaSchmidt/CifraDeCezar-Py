######################################################################################################
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
#                                                                                                    #
######################################################################################################
global alfabeto
alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
global PalavrasComuns
PalavrasComuns =[]
# Menu do programa
def main(online = True):
    while online == True:
        print('''
            [1] Cifrar
            [2] Decifrar
            [3] Força Bruta

            [S] Sair
        ''')
        op = input("selefcione uma opção: ")
        if op == '1':
            cifrar()
        elif op == '2':
            decifrar()
        elif op == '3':
            print("ForceBreak")
            print('''
                [1] Adiquirir texto apartir de arquivo(.txt)
                [2] Digitar texto (recomendado para mensagens curtas)

                [S] Voltar ao menu
            ''')
            op3 = input("selecione uma opção: ")
            if op3 == '1':
                print("renomeie o arquivo para 'forceB.txt' e coloque o arquivo na mesma pasta que o programa")
                input("tecle enter para continuar...")
                arquivo = open('forceB.txt', 'r')
                texto = arquivo.read()
                print(ForceBreak(texto))
                arquivo.close()
            elif op3 == '2':
                texto = str(input("digite a mensagem cifrada: "))
                print(ForceBreak(texto))
            elif (op3 == 'S') or (op3 == 's'):
                pass
        elif (op == 's') or (op == 'S'):
            online = False
            print("o programa foi fechado")
        else:
            print("opção invalida")
def cifrar():
    print("cifrar")
    print('''
        [1] Adiquirir texto apartir de arquivo(.txt)
        [2] Digitar texto (recomendado para mensagens curtas)

        [S] Voltar ao menu
    ''')
    op = input("selecione uma opção: ")
    if op == '1':
        print("renomeie o arquivo para 'cifrar.txt' e coloque o arquivo na mesma pasta que o programa")
        input("tecle enter para continuar...")
        chave = int(input("Digite a chave [1-26]: "))
        arquivo = open('cifrar.txt', 'r')
        texto = arquivo.read()
        # Criptografar
        cifra = ''
        for caractere in texto:
            if (caractere in alfabeto):
                IndexCaractere = alfabeto.index(caractere)
                cifra += alfabeto[(IndexCaractere + chave) % len(alfabeto)]
            else:
                cifra += caractere
        arquivo.close()
        arquivo = open((str(chave) +'.txt'), 'w')
        arquivo.writelines(cifra)
        arquivo.close()
        print("seu texto cifrado foi armazenado como " + str(chave) +".txt na pasta onde esta o programa")
        input("tecle enter voltar ao menu...")
        return
    elif op == '2':
        texto = str(input("Digite a mensagem a cifrar: "))
        chave = int(input("Digite a chave [1-26]: "))
        # Criptografar
        cifra = ''
        for caractere in texto:
            if (caractere in alfabeto):
                IndexCaractere = alfabeto.index(caractere)
                cifra += alfabeto[(IndexCaractere + chave) % len(alfabeto)]
            else:
                cifra += caractere
        return print(cifra)
    elif (op == 's')or (op == 'S'):
        return

def decifrar():
    print("decifrar")
    print('''
        [1] Adiquirir texto apartir de um arquivo(.txt)
        [2] Digitar texto (recomendado para mensagens curtas)

        [S] Voltar ao menu
    ''')
    op = input("selecione uma opção: ")
    if op == '1':
        print("renomeie o arquivo para 'decifrar.txt' e coloque o arquivo na mesma pasta do programa")
        input("tecle enter para continuar...")
        chave = int(input("Digite a chave [1-26]: "))
        arquivo = open('decifrar.txt', 'r')
        texto = arquivo.read()
        # Decriptografar
        cifra = ''
        for caractere in texto:
            if (caractere in alfabeto):
                IndexCaractere = alfabeto.index(caractere)
                cifra += alfabeto[(IndexCaractere - chave) % len(alfabeto)]
            else:
                cifra += caractere
        arquivo.close()
        arquivo = open(str(chave)+"decifrado.txt", 'w')
        arquivo.writelines(cifra)
        arquivo.close()
        print("Seu texto decifrado foi armazenado como " + str(chave) +"decifrado.txt na pasta onde esta o programa")
        input("tecle enter para voltar ao menu...")
        return
    elif op == '2':
        texto = str(input("Digite a mensagem cifrada: "))
        chave = int(input("Digite a chave [1-26]: "))
        # Decriptografar
        cifra = ''
        for caractere in texto:
            if (caractere in alfabeto):
                IndexCaractere = alfabeto.index(caractere)
                cifra += alfabeto[(IndexCaractere - chave) % len(alfabeto)]
            else:
                cifra += caractere
        print(cifra)
        return
    elif (op == 's') or (op == 'S'):
        return
    else:
        print("opção invalida")
        return

def ForceBreak(texto):
    chave = 0
    legivel = False
    while legivel == False:
        cifra = ''
        for caractere in texto:
            if (caractere in alfabeto):
                IndexCaractere = alfabeto.index(caractere)
                cifra += alfabeto[(IndexCaractere - chave) % len(alfabeto)]
            else:
                cifra += caractere
        print(cifra)
        # debug manual de verificação de inteligibilidade
        print('''
            [1] Texto ilegivel
            [2] Texto legivel
        ''')
        op = int(input("selecione uma opção: "))
        if op == 1:
            chave += 1
        elif op == 2:
            sucesso = "texto decifrado: chave ="+ str(chave) + " texto =" + cifra
            return sucesso
        else:
            print("opção não existe")

main()
