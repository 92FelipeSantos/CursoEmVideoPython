# Ler uma quantia em reais e convertê-la para dólares
# US$ 1 = R$ 4.15

r = float(input('Digite o valor em Reais: R$ '))
d = r/4.15

print('Com R$ {:.2f} é possível comprar US$ {:.2f}'.format(r, d))