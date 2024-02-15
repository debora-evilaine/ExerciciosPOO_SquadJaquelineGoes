from datetime import datetime
from typing import NamedTuple

class Produto:
    def __init__(self, nome: str, fornecedores: list, categorias: list, quantidade: int):
        self.nome = nome
        self.fornecedores = fornecedores
        self.categorias = categorias
        self.quantidade = quantidade

    def remover_estoque(self, quantidade_comprada: int):
        self.quantidade -= quantidade_comprada
    
class Cliente:
    def __init__(self, nome: str, telefone: str, endereco: str):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Compra:
    def __init__(self, cliente: object, produtos: dict):
        self.cliente = cliente
        self.produtos = produtos
        self.horario = datetime.now()
    
class Mercado:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.transacoes = []

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def cadastrar_produto(self, novo_produto: Produto):
        if (novo_produto.nome in self.produtos):
            print("Este produto já está cadastrado.")
        else:
            self.produtos.append(novo_produto)

    def exibir_nota(self, compra):
        print("=" * 40)
        print("** SUPERMERCADO **")
        print("=" * 40)

        print(f"Data: {compra.horario.strftime("%d/%m/%Y, %H:%M:%S")}")

        print("-" * 40)
        print(f"| {"Descrição":<20} |  {"Qtd":^3} |")
        print("-" * 40)
        for item in compra.produtos:
            nome = item[0].nome
            quantidade = item[1]
            print(f"| {nome:<20} | {quantidade:^4} |")
        print("-" * 40)

        print("-" * 40)
        print(f"OBRIGADO PELA SUA COMPRA, {compra.cliente.nome.upper()}!")
        print("Volte sempre!")
        print("=" * 40)

    def registrar_compra(self, compra: Compra):
        self.transacoes.append(compra)
        for item in compra.produtos:
            item[0].remover_estoque(item[1])
        self.exibir_nota(compra)
        

mercado = Mercado()

cliente01 = Cliente(nome="Lívia Nascimento", telefone="81994000000", endereco="Rua dos Bobos, nº 0")

mercado.cadastrar_cliente(cliente=cliente01)

produto01 = Produto(nome="Molho de tomate", fornecedores=["fornecedor A", "fornecedor B"], categorias=["molhos", "comida"], quantidade=500)
produto02 = Produto(nome="Sabão em pó", fornecedores=["fornecedor C"], categorias=["lava roupas", "limpeza"], quantidade=150)
produto03 = Produto(nome="Macarrão", fornecedores=["fornecedor A", "fornecedor B"], categorias=["massas", "comida"], quantidade=300)
produto04 = Produto(nome="Goiabada", fornecedores=["fornecedor A", "fornecedor B"], categorias=["doces", "comida"], quantidade=800)

mercado.cadastrar_produto(novo_produto=produto01)
mercado.cadastrar_produto(novo_produto=produto02)
mercado.cadastrar_produto(novo_produto=produto03)
mercado.cadastrar_produto(novo_produto=produto04)

compra01 = Compra(cliente=cliente01, produtos=[[produto01, 2], [produto03, 5]])

mercado.registrar_compra(compra=compra01)


