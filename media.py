nota1 = float(input("nota 1 = "))
nota2 = float(input("nota 2 = "))
nota3 = float(input("nota 3 = "))
media = (nota1 + nota2 + nota3) / 3
print(f"media = {round(media, 2)}")
 
if media >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")