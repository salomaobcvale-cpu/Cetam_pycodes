salário = float(input("Qual seu salário?"))
percentual = float(input("Qual o percentual de reajuste?"))
reajuste = salário/percentual*100
NewSal = salário+reajuste
mensagem = F"Parabens, seu novo salário é {NewSal} São {reajuste} reais a mais pra você comer pastel com os amigos!"
print(mensagem)