# Ler uma medida em metros e convertê-lo para centímetros e milímetros.

m = float(input('Digite a medida em metros: '))
cm = m * 100
mm = m * 1000

print('A medida {}m equivale a {:.0f}cm e {:.0f}mm.'.format(m, cm, mm))
