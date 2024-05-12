#Descrevendo o código acima, ele inicia na linha 2 quando é exigido a inputação de um valor 
def descriptografar_cifra_cesar(texto_cifrado, chave):
    texto_descriptografado = ""
#Encriptação do texto, caractere por caractere
    for caractere in texto_cifrado:
        if caractere.isalpha():
#Função ord, que transforma em número
            codigo = ord(caractere)
            codigo -= chave
#Caso o número seja  as ordenadas de "A" ou "Z".
            if codigo < ord('a'):
                codigo += 26
            elif codigo > ord('z'):
                codigo -= 26
            texto_descriptografado += chr(codigo)
        else:
            texto_descriptografado += caractere
    return texto_descriptografado

#Código inicia aqui, pedindo a inputação do texto
texto_cifrado = input("Digite o texto cifrado: ")
#A chave a ser utilizada, não pode ser maior ou igual que 26
chave = int(input("Digite a chave de descriptografia: "))

texto_descriptografado = descriptografar_cifra_cesar(texto_cifrado, chave)
print("Texto descriptografado:", texto_descriptografado)
