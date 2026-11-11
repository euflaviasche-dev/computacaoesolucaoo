def criar_registro():

    registro = dict()

    registro['artista'] = input("Digite o nome do artista: ")
    registro['titulo'] = input("Digite o título do LP: ")
    registro['quantidade_faixas'] = int(input("Digite a quantidade de faixas: "))
    registro['duracao_total'] = float(input("Digite a duração total (em minutos): "))

    return registro

acervo = []

continuar = 'S'

while continuar == 'S':

    lp = criar_registro()

    acervo.append(lp)

    continuar = input('Deseja adicionar outro LP? (S/N): ').upper()

print('\nAcervo musical:')

for item in acervo:
    print(f"Artista: {item['artista']}")
    print(f"Título: {item['titulo']}")
    print(f"Faixas: {item['quantidade_faixas']}")
    print(f"Duração: {item['duracao_total']} min")
    print("-" * 30)