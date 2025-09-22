def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 17 and idade > 15 or idade >= 65:
        print(f"Sua Idade é de {idade} anos e o voto é:  OPCIONAL")
    elif idade < 16:
        print(f"Sua Idade é de {idade} anos e o você NÃO VOTA!!")
    else:
        print(f"Sua Idade é de {idade} anos e o voto é:  OBRIGATÓRIO")




voto(int(input("Que ano você nasceu? ")))