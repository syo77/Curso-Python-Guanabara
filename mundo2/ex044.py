"""
Elabore um programa em Python que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/pix: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
"""
valor_produto = float(input("Insira o preço do produto: "))
escolha = int(input("""Qual sua forma de pagamento?
[ 1 ] À vista dinheiro/pix
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão
Digite: """))
if escolha == 1:
    total = valor_produto * (1 - 10/100)
elif escolha == 2:
    total = valor_produto * (1 - 5/100)
elif escolha == 3:
    total = valor_produto
    cartao2x = valor_produto/2
    print(f"Dividindo em 2x no cartão cada parcela irá custar {cartao2x:.2f}")
elif escolha == 4:
    total = valor_produto * (1 + 20/100)
    qtd_parcelas = int(input("Digite a quantidade de parcelas: "))
    cartao3xmais = valor_produto/qtd_parcelas
    print(f"Dividindo em {qtd_parcelas}x no cartão cada parcela irá custar {cartao3xmais:.2f} COM JUROS")
else:
    total = valor_produto
    print("Digite uma escolha válida")
print(f"O produto de {valor_produto:.2f} custará {total:.2f}")










