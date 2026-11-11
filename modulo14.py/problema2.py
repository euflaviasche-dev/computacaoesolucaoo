palavras = []
maiores = []
menores = []

for i in range(5):
    palavra = input("Digite uma palavra:")
    palavras.append(palavra)

for palavra in palavras:
    if len(palavra) > 5:
        maiores.append(palavra)
    else:
        menores.append(palavra)

print("\nPalavras com 6 ou mais letras:")
print(maiores)

print('\nPalavras com menos de 6 letras:')
print(menores)
