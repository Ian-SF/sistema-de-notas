alunos = []
medias = []
situacoes = []

    # cadastrar alunos
for i in range(10):
    aluno = input(f"\nAluno {i + 1}: ")
    alunos.append(aluno)
    n1 = float(input(f"Digite uma nota: "))
    n2 = float(input(f"Digite uma segunda nota: "))
    media = (n1 + n2) / 2
    medias.append(media)


    if media < 7:
        print(f"{aluno}, sua média é {media}, ou seja, você está reprovado!")
        situacoes.append("Reprovado!")
    else:
        print(f"{aluno}, sua média é {media}, ou seja, você está aprovado!")
        situacoes.append("Aprovado!")


print("\n===== RELATÓRIO FINAL =====")

# variável de aprovados e reprovados, necessita para fazer a contagem de cada
aprovados = 0
reprovados = 0
soma_medias = 0


    # mostrar relatorio
for i in range(len(alunos)):
    print("Aluno:",alunos [i], "| Média:",medias [i],"|", situacoes[i])

    # conta os aprovados e reprovados
    if situacoes[i] == "Aprovado!":
        aprovados += 1
    else:
        reprovados += 1
    # acumular a contagem de cada media
    soma_medias += medias[i]
    media_turma = soma_medias/len(alunos)

print("==============================\n")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
print(f"Média da turma: {media_turma}")

