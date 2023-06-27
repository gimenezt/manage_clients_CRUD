import psycopg2
import yaml


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def select():
    print('---------- VISUALIZAR INFORMAÇÕES ----------')
    
    cur.execute("SELECT * FROM user_;")

    list = cur.fetchall()

    print('\n\nNOME \t CELULAR \t ENDEREÇO \n----------------------------------')

    for x in list:
        print('{} \t {} \t {}'.format(x[1], x[2], x[3]))

def insert():
    print('---------- ADICIONAR NOVO USUÁRIO ----------')

    nome =           input("Digite o nome: ")
    celular =        input("Digite o celular: ")
    endereco =       input("Digite o endereço: ")

    query = """INSERT INTO user_ (name, celular, endereço) VALUES (%s, %s, %s)"""
    values = (nome, celular, endereco)
    cur.execute(query, values)
    conn.commit()

    select()

def update():
    print('---------- ATUALIZAR INFORMAÇÕES ----------\n')
    nome = input("Digite o nome do usuário cujo deseja atualizar as informações: ")
    
    cur.execute("SELECT name FROM user_;")
    nomes_tupla = cur.fetchall()
    nomes_lista = []

    for i in range(len(nomes_tupla)):
        nomes_lista.append(nomes_tupla[i][0])

    if nome in nomes_lista:
        cur.execute         ("SELECT * FROM user_ where name = {}".format("'"+nome+"'"))
        actual_info =       cur.fetchall()
        id =                actual_info[0][0]
        edit_option =       int(input("\n\nQual informação deseja atualizar referente ao usuário {}?\n\n1 - Nome\n2 - Celular\n3 - Endereço\n\n".format(nome)))

        match edit_option:
            case 1:
                column =    'name'
                value =     "'"+input("\nDigite o novo nome: ")+"'"
            case 2:
                column =    'celular'
                value =     "'"+input("\nDigite o novo celular: ")+"'"
            case 3:
                column =    'endereço'
                value =     "'"+input("\nDigite o novo endereço: ")+"'"
        
        query = """UPDATE user_ SET {} = {} where id = {}""".format(column, value, id)
        cur.execute(query)
        conn.commit()

        print("\n\n>>>>>>>>> Informações atualizadas com sucesso.\n\n")
        select()
    
    else:
        print("\nNome de usuário inválido. Verifique novamente.")

def delete():
    print('\n---------- DELETAR INFORMAÇÕES ----------')
    nome = input("Digite o nome do usuário cujo deseja deletar as informações: ")
    
    try:
        cur.execute("DELETE FROM user_ WHERE name = {}\n\n".format("'"+nome+"'"))
        conn.commit()
        print('\nInformações deletadas com sucesso.')
    except:
        print("\nNome de usuário inválido. Verifique novamente.")

    select()


config = read_yaml('login_info.yml')

database, user, password, host = config['db_name'], config['user'], config['pass'], config['host']

conn = psycopg2.connect(database=database,
user=user,
password=password,
host=host
)

cur = conn.cursor()
