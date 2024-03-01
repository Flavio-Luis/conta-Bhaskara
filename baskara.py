import math

delta = float

condicao = True

while condicao:

    try:
        a = float(input("Coeficiente 'A': "))
        if a == 0:
            print("A variavel A, não pode receber o valor igual a zero")
            a = float(input("Coeficiente 'A': "))
        b = float(input("Coeficiente 'B': "))
        c = float(input("Coeficiente 'C': "))
    except:
        print("Digite somente números!\n")
        continue

    delta = (b * b) - (4 * a * c)

    if delta > 0:

        x1 = (-b + math.sqrt(delta)) / (2 * a)

        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print(f"\nX1= {x1:.4f}")
        print(f"X2= {x2:.4f}\n")

        resposta = input("\nDeseja recomeçar:")
        resposta_trat = resposta.lower().startswith("s")

        if resposta_trat:
            print()
            continue
        else:
            print("Até mais!😊\n")
            break
    
    if delta < 0:
        print("Esses valores determinou em Raízes Complexas!")

        resposta = input("\nDeseja recomeçar:")
        resposta_trat = resposta.lower().startswith("s")
        if resposta_trat:
            print()
            continue
        else:
            print("Até mais!😊\n")
            break

    else:
        print("Esta equação nao possui raízes reais")
        resposta = input("\nDeseja recomeçar:")
        resposta_trat = resposta.lower().startswith("s")
        if resposta_trat:
            print()
            continue
        else:
            print("Até mais!😊\n")
            break