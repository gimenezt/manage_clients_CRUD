from Functions import select, insert, update, delete

def main():
    var = int(input('\nBem-vindo(a)! \n\nO que deseja fazer?\n\n1 - Visualizar informações\n2 - Adicionar\n3 - Editar\n4 - Deletar\n'))

    match var:
        case 1:
            select()
        case 2:
            insert()
        case 3:
            update()
        case 4:
            delete()
    
    option = int(input('\nRetornar para o menu inicial?\n1 - Sim\n2 - Não\n'))
    
    if option == 1:
        main()
    else:
        print('\nAté mais!')
        exit()
main()
