nome = 'Paula Martins.'
valor = 500.00
desconto = 10
cupom = True

format_1 = f"O nome da pessoa é {nome}, o desconto dela é {desconto}"
format_2 = "O nome da pessoa é {}, o desconto dela é {}".format(nome, desconto)
format_3 = "O nome da pessoa é {a}, o desconto dela é {b}".format(a=nome, b=desconto)

tipo_nome = type(nome)
tipo_valor = type(valor)
tipo_desconto = type(desconto)
tipo_cupom = type(cupom)

print(tipo_nome)
print (tipo_valor)
print(tipo_desconto)
print (tipo_cupom)