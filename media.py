aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media > 5:
    print(f"{aluno} passou sua nota {media}")

else:
    print(f"{aluno} nao atingiu a media {media}")