# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

adicao = numero1 + numero2
subtracao = numero1 - numero2
divisao = numero1 / numero2
multiplicao = numero1 * numero2

print(f"Os valores digitados foram: {numero1} e {numero2}")

print(f"Somando os dos dois valores obtemos: {adicao}")
print(f"Subtraindo o primeiro valor do segundo obtemos: {subtracao}")
print(f"Dividindo o primeiro valor do segundo obtemos: {divisao}")
print(f"Multiplicando os dois valores obtemos: {multiplicacao}")

print("Volte sempre!")
