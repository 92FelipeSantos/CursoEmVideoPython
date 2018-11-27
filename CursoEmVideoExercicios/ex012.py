# Ler o preço de um produto e exibir um novo valor com 5% de desconto

p = float(input('Digite o preço do produto: '))
d = p - (p * (5/100))
print('O preço original era de R$ {:.2f} e com um desconto de 5% passou a custar R$ {:.2f}'.format(p, d))
