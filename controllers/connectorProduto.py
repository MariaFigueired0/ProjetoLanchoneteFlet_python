import mysql.connector
from Produto import Produto

user="root"
senha=""
host="localhost"
database="lanchonete"

#retorna a conexão estabelecida ou None caso dê errado
def conectar():
    conexao=None
    try:
        conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=senha,
            database=database
        )
    except mysql.connector.Error as e:
        print(f"Erro ao conectar com BD:{e}")

    return conexao

#finalizar a conexão o fim das operações
def fechar_conexao(conexao):
    if conexao.is_connected():
        conexao.close()
        print("Conexão terminada!")

#CREATE
def create(conexao, Produto):
    try:
        cursor = conexao.cursor()
        #usar o %s para evitar o SQL injector
        query = "INSERT into PRODUTOS(descricao, preco, qtd) VALUES(%s, %s, %s)"
        cursor.execute(query, (Produto.descricao, Produto.preco, Produto.qtd))
        cursor.commit()

    except mysql.connector.Error as e:
        print(f"Erro ao inserir produto: {e}")
    finally:
        cursor.close()

# def create(conexao, descricao, preco, quantidade):
#     try:
#         cursor = conexao.cursor()
#         #usar o $s para evitar o SQL injector
#         query = "INSERT into PRODUTOS(descricao, preco, quantidade) VALUES (%s, %s, %s)"
#         cursor.execute(query, (descricao, preco, quantidade))
#         conexao.commit()
#         print(f"{descricao} Registrado com sucesso!")

#     except mysql.connector.Error as e:
#         print(f"Erro ao inserir produto:{e}")
#     finally:
#         cursor.close()

#READ
def read(conexao):
    listaProdutos = []
    try:
        cursor = conexao.cursor()
        query = "Select * from produtos"
        cursor.execute(query)
        registros = cursor.fetchall()

        for produtos in registros:
            objeto = Produto(*produtos) #Produto(registro[0], registro[1],...)
            listaProdutos.append(objeto)

    except mysql.connector.Error as e:
        print(f"Erro ao listar produtos: {e}")
    finally:
        cursor.close()
    return listaProdutos

#UPDATE
def update(conexao, preco, quantidade, codigo):
    try:
        cursor = conexao.cursor()
        query = "UPDATE produtos SET preco=%s, quantidade=%s WHERE codigo=%s"
        cursor.execute(query, (preco, quantidade, codigo))
        conexao.commit()
        print(f"{codigo} registrado com sucesso!")

    except mysql.connector.Error as e:
        print (f"Erro ao atualizar produto: {e}")
    finally:
        cursor.close()

#DELETE
def delete(conexao, codigo):
    try:
        cursor = conexao.cursor()
        query = "DELETE from PRODUTOS WHERE codigo = %s"
        cursor.execute(query,tuple([codigo,]))
        conexao.commit()
        print(f"{codigo} excluído!")

    except mysql.connector.Error as e:
        print(f"Erro ao deletar o produto!")
    finally:
        cursor.close()

#BUSCAR
def buscar(conexao, busca):
    listaProdutos=[]
    try:
        cursor = conexao.cursor()
        query = "SELECT * from PRODUTOS where DESCRICAO like %s"
        cursor.execute(query, ("%s"+busca+"%s",))
        registros = cursor.fetchall()

        for produtos in registros:
            objeto = Produto(*produto)
            listaProdutos.append(objeto)

    except mysql.connector.Error as e:
        print(f"Erro ao buscar produto: {e}")
    finally:
        cursor.close()
    return listaProdutos
        
#MAIN
conexao = conectar()
if conexao: #ou if conexao!=None
    print("Conectado com o banco de dados!")

    #novo_produto = Produto(None,"Achocolatado Nescau", 10, 10)
    #create(conexao, novo_produto)

    produtosR = read(conexao)
    for produto in produtosR:
        produto.listar()

    #update(conexao,2,5,10)

    #delete(conexao, 4)

    produtosB = buscar(conexao, "Coco")
    if produtosB!=[]:
        for produtos in produtosB:
            produto.listar()
    else:
        print("Nenhum produto encontrado!")

    fechar_conexao(conexao)