# Entre com a quantidade de Km percorridos por um carro alugado e a quantidade de dias de aluguel. Calcule o preço a pagar. Utilize: R$ 60 a diária e R$ 0.15 por km.

km = float(input('Digite a quantidade de quilômetros rodados: '))
diaria = int(input('Digite a quantidade de diárias utilizadas: '))

valor = km * 0.15 + diaria * 60

print("O preço total do aluguel por {} diárias e {:.2f}km rodados é igual a R$ {:.2f}".format(diaria, km, valor))
