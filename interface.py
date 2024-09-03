from data_music import DataMusic

def menu():
    """ Exibe o menu de opções """
    print("\nMenu:")
    print("1. Criar música")
    print("2. Ler música")
    print("3. Atualizar música")
    print("4. Deletar música")
    print("5. Listar músicas")
    print("6. Encerrar programa")

def main():
    data_music = DataMusic()  # Instancia a classe DataMusic

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            id_musica = input("Digite o ID da música: ")
            nome = input("Digite o nome da música: ")
            banda = input("Digite o nome da banda/cantor: ")
            print(data_music.create(id_musica, nome, banda))
        
        elif opcao == '2':
            id_musica = input("Digite o ID da música para ler: ")
            print(data_music.read(id_musica))
        
        elif opcao == '3':
            id_musica = input("Digite o ID da música para atualizar: ")
            nome = input("Digite o novo nome da música ou deixe em branco para não alterar: ")
            banda = input("Digite o novo nome da banda/cantor ou deixe em branco para não alterar: ")
            print(data_music.update(id_musica, nome if nome else None, banda if banda else None))
        
        elif opcao == '4':
            id_musica = input("Digite o ID da música para deletar: ")
            print(data_music.delete(id_musica))
        
        elif opcao == '5':
            musicas = data_music.list_musicas()
            if isinstance(musicas, str):
                print(musicas)
            else:
                for id_musica, dados in musicas.items():
                    print(f"ID: {id_musica}, Nome: {dados['nome']}, Banda: {dados['banda']}")
        
        elif opcao == '6':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, por favor escolha uma opção entre 1 e 6.")

if __name__ == "__main__":
    main()
