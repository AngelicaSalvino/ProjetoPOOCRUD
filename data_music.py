class DataMusic:
    def __init__(self, arquivo='musicas.txt'):
        self.arquivo = arquivo
    
    def _ler_dados(self):
        """ Lê os dados do arquivo e retorna um dicionário """
        musicas = {}
        try:
            with open(self.arquivo, 'r') as file:
                for linha in file:
                    id_musica, nome, banda = linha.strip().split(',')
                    musicas[id_musica] = {"nome": nome, "banda": banda}
        except FileNotFoundError:
            pass
        return musicas
    
    def _escrever_dados(self, musicas):
        """ Escreve os dados no arquivo """
        with open(self.arquivo, 'w') as file:
            for id_musica, dados in musicas.items():
                file.write(f"{id_musica},{dados['nome']},{dados['banda']}\n")
    
    def create(self, id_musica, nome, banda):
        """ Adiciona uma nova música ao arquivo, se o ID não existir """
        musicas = self._ler_dados()
        if id_musica in musicas:
            return "ID já existe. Use um ID diferente ou faça uma atualização."
        musicas[id_musica] = {"nome": nome, "banda": banda}
        self._escrever_dados(musicas)
        return "Música adicionada com sucesso."
    
    def read(self, id_musica):
        """ Retorna os detalhes da música com o ID fornecido """
        musicas = self._ler_dados()
        musica = musicas.get(id_musica)
        if musica:
            return musica
        return "Música não encontrada."
    
    def update(self, id_musica, nome=None, banda=None):
        """ Atualiza os detalhes da música com o ID fornecido """
        musicas = self._ler_dados()
        musica = musicas.get(id_musica)
        if not musica:
            return "Música não encontrada."
        if nome:
            musica["nome"] = nome
        if banda:
            musica["banda"] = banda
        self._escrever_dados(musicas)
        return "Música atualizada com sucesso."
    
    def delete(self, id_musica):
        """ Remove a música com o ID fornecido """
        musicas = self._ler_dados()
        if id_musica in musicas:
            del musicas[id_musica]
            self._escrever_dados(musicas)
            return "Música removida com sucesso."
        return "Música não encontrada."
    
    def list_musicas(self):
        """ Lista todas as músicas armazenadas """
        musicas = self._ler_dados()
        if not musicas:
            return "Nenhuma música cadastrada."
        return musicas

        