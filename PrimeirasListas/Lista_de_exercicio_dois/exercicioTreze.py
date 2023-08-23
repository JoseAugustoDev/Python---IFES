haste_aco = int(input("Digite a quantidade de hastes de aço que deseja comprar: "))
haste_cobre = int(input("Digite a quantidade de hastes de cobre que deseja comprar: "))
haste_aluminio = int(input("Digite a quantidade de hastes de alumínio que deseja comprar: "))

preco_unitario_aco = 2.5
preco_unitario_cobre = 4.0
preco_unitario_aluminio = 5.0

quantidade_total = haste_aco + haste_cobre + haste_aluminio

preco_pedido_aco = preco_unitario_aco * haste_aco
preco_pedido_cobre = preco_unitario_cobre * haste_cobre
preco_pedido_aluminio = preco_unitario_aluminio * haste_aluminio

preco_sem_desconto = preco_pedido_aco + preco_pedido_cobre + preco_pedido_aluminio

preco_final = 0

if quantidade_total <= 6:
    preco_final = preco_sem_desconto
elif quantidade_total >= 7 and quantidade_total <= 15:
    preco_final = preco_sem_desconto - (preco_sem_desconto * 0.1)
elif quantidade_total >= 16 and quantidade_total <= 20:
    preco_final = preco_sem_desconto - (preco_sem_desconto * 0.15)
elif quantidade_total > 20:
    preco_final = preco_sem_desconto - (preco_sem_desconto * 0.20)
else:
    print("Erro!")

print(f"Preço final é de: {preco_final} ")