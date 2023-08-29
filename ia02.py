nume1 = (input("Digite um número: ")) # retorna uma string digutada pelo user

antecessor = 0
sucessor = 0

try:
    sucessor = 1 + int(nume1)
    antecessor = int(nume1) - 1
except ValueError:
    raise ValueError("Digite um valor valido")
    print("Digite um numero valido")
        
print(f"O antecessor do número {nume1} é {antecessor} e o sucessor é {sucessor}")

print(type(nume1))
print(type(antecessor))
print(type(sucessor))