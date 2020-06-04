def cifrar(texto, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz 1234567890!@#$%¨&*()'
    textoCypto =''
    for c in texto:
        CaractereIndice = alfabeto.index(c)
        textoCrypto += alfabeto[((CaractereIndice + chave) % (len(alfabeto)))]
    return textoCrypto
def decifrar(texto, chave):
    return
def quebrar(texto):
    return
print("Cifra de cezar em Phyton")
print('''
    [1] Cifrar / Criptografar
    [2] Decifrar / Decriptar
    [3] Decifrar na força bruta
    [4] Sair
''')
ValidOp = False
while ValidOp == False:
    op = int(input("selecione uma opção:"))
    if op == 1:
        print("Cifrar")
        
    elif op == 2:
        print("Decifrar")
    elif op == 3:
        print("Força bruta vulgo grosseria")
    elif op == 4:
        print("Programa fechado")
        break
