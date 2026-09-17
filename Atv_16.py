preço_do_produto = float(input("Qual o preço do produto?"))
desconto = preço_do_produto/10
novo_valor = preço_do_produto-desconto
mensagem = f"Parabéns! Você ganhou 10% de desconto. Agora custará somente {novo_valor}"
print(mensagem)