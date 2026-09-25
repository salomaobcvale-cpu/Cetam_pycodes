def calcular_media(a, b, c):
    resultado = (a+b+c)/3
    return resultado
nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_3 = float(input("Digite sua terceira nota: "))
media = calcular_media(nota_1,nota_2,nota_3)
print(media)