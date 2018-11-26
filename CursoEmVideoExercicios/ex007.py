# Ler duas notas de um aluno e calcular a média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A média das notas {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))