import json
from deep_translator import GoogleTranslator


class ColetarDados:

    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.dados = []

    def coletar(self):
        try:
            with open(self.nome_arquivo, "r", encoding="utf-8") as dados:
                linhas = dados.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo {self.nome_arquivo} não foi encontrado.")
        except Exception as e:
            raise RuntimeError(f"Ocorreu um erro ao ler o arquivo: {e}")

        if not linhas:
            raise ValueError(f"O arquivo {self.nome_arquivo} está vazio.")

        self.dados = [linha.strip() for linha in linhas]
        return self.dados


class Tradutor:
    def __init__(self, source, target):
        try:
            self.translator = GoogleTranslator(source=source, target=target)
        except Exception as e:
            raise RuntimeError(f"Erro ao inicializar o tradutor: {e}")

    def traduzir(self, texto):
        try:
            return self.translator.translate(texto)
        except Exception as e:
            raise RuntimeError(f"Erro ao traduzir o texto '{texto}': {e}")


class TratarDados:

    def __init__(self, dados):
        if not isinstance(dados, list):
            raise ValueError("A entrada deve ser uma lista de textos.")
        self.dados = dados

    def formatar_dados(self):
        resultado = {}

        for i, texto in enumerate(self.dados):
            if not isinstance(texto, str) or not texto.strip():
                raise ValueError(f"Texto inválido encontrado na entrada: {texto}")

            inicio = f"{' '.join(texto.split()[:3])}"

            traduzir_ingles = Tradutor("pt", "en")
            traduzir_espanhol = Tradutor("pt", "es")

            try:
                traduzido_en = traduzir_ingles.traduzir(texto)
                traduzido_es = traduzir_espanhol.traduzir(texto)
            except RuntimeError as e:
                print(f"Erro durante a tradução do texto '{texto}': {e}")
                traduzido_en = traduzido_es = "Erro na tradução"

            resultado[inicio] = {
                "pt": texto,
                "es": traduzido_es,
                "en": traduzido_en
            }

        return resultado

    def exportar(self, arquivo_exportar):
        dados_formatados = self.formatar_dados()

        try:
            with open(arquivo_exportar, "w", encoding="utf-8") as arquivo:
                json.dump(dados_formatados, arquivo, ensure_ascii=False, indent=4)
            print(f"Dados exportados com sucesso para o arquivo {arquivo_exportar}!")
        except Exception as e:
            raise RuntimeError(f"Erro ao exportar os dados para o arquivo: {e}")


def Main():
    try:
        coleta = ColetarDados(nome_arquivo="dados.txt")
        dados_portugues = coleta.coletar()

        formatar = TratarDados(dados_portugues)
        formatar.exportar("dados_traduzidos.json")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    Main()
