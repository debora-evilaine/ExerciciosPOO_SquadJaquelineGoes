from datetime import datetime

lista_produtos = []
dados_transacoes = []


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
    
    @property
    def get_nome(self):
        return self.nome
        
    @property
    def get_telefone(self):
        return self.telefone
        
    @property
    def get_endereco(self):
        return self.endereco
        
    
    def comprar_produto(self, produto, quantidade):
        nome_produto = produto.nome.lower()
        print(nome_produto)
        
        for produto in lista_produtos:
            if produto["Nome"] == nome_produto:
                if produto["Quantidade disponivel"] >= quantidade:
                    produto["Quantidade disponivel"] -= quantidade
                    dados_transacoes.append({"Data da compra": datetime.now(), "Produto comprado": nome_produto, "Quantidade comprada": quantidade, "Comprador": self.nome})
                    print("Produto comprado!")
                else:
                    print(f"Estamos sem estoque do produto {nome_produto}!")
                    return
                
               
class Produto():
    def __init__(self, nome, quantidade_disponivel):
        self.nome = nome
        self.categorias = []
        self.fornecedores = []
        self.quantidade_disponivel = quantidade_disponivel
        
    def cadastrar_categorias(self, categoria):
        self.categorias.append(categoria)
        
    def cadastrar_fornecedores(self, fornecedor):
        self.fornecedores.append(fornecedor)
        
    def adicionar_a_lista(self, produto):
        lista_produtos.append({"Nome": produto.nome.lower(), "Quantidade disponivel": produto.quantidade_disponivel})
        
    def apresentar_produto(self, produto):
        print(vars(produto))
        
    @property
    def get_nome_produto(self):
        return self.nome
    
    @property
    def get_quantidade_produto(self):
        return self.quantidade_disponivel
        

class Mercado():
    def __init__(self):
        self.__clientes = []
        
    def cadastrar_cliente(self, cliente):
        nome_cliente = cliente.nome.lower()
        if nome_cliente not in (cliente["Nome do cliente"] for cliente in self.__clientes):
            self.__clientes.append({"Nome do cliente": cliente.get_nome, "Telefone": cliente.get_telefone, "Endereço": cliente.get_endereco})
            print("Cliente cadastrado com sucesso!")
        else:
            print("\nEste cliente já está cadastrado!\n")
            return
        
    def get_lista_clientes(self):
        return self.__clientes



#EXEMPLOS DE TESTES  
    
produto1 = Produto("Sabonete", 5)
produto1.cadastrar_categorias("limpeza")
produto1.cadastrar_categorias("banho")
produto1.apresentar_produto(produto1)
print(lista_produtos)

produto1.adicionar_a_lista(produto1)
print(lista_produtos)


print()
print()

print("Entrando no objeto cliente")

cliente1 = Cliente("debora", "1199999", "Rua 123")
cliente1.comprar_produto(produto1, 2)
print(dados_transacoes)
print()

print("Print da lista de produtos:")
print(lista_produtos)
    
print()

print("Entrando no objeto Mercado")

mercado1 = Mercado()
mercado1.cadastrar_cliente(cliente1)
mercado1.cadastrar_cliente(cliente1)
lista_clientes = mercado1.get_lista_clientes()
print(lista_clientes)