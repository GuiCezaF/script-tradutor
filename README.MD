# Script de Tradução Automática

Este script automatiza a tradução de textos de um sistema, gerando um arquivo JSON estruturado com traduções para vários idiomas (português, espanhol e inglês).

## Como Funciona?

O script lê um arquivo de entrada (`dados.txt`), traduz cada linha e gera um arquivo de saída (`dados_traduzidos.json`) com as traduções organizadas por idioma.

### Estrutura do Resultado

O arquivo de saída será gerado com a seguinte estrutura:

```json
{
    "TEXTO_ORIGINAL": {
        "pt": "TRADUÇÃO_EM_PORTUGUÊS",
        "es": "TRADUÇÃO_EM_ESPANHOL",
        "en": "TRADUÇÃO_EM_INGLÊS"
    }
}
```

### Pré-requisitos

- Python 3.12
- pipenv para gerenciamento de dependências

### Dependências

As dependências são gerenciadas pelo pipenv e estão listadas no arquivo Pipfile. O script utiliza a biblioteca deep-translator para realizar as traduções.

### Instalando as Dependências

Execute o seguinte comando para instalar as dependências:

```bash
  pipenv install
```

### Como Usar
1. Preparar o Arquivo de Entrada:

    - Crie ou edite o arquivo dados.txt.
    - Insira cada texto a ser traduzido em uma nova linha. Exemplo:
    ```txt
      CAMPANHAS
      INÍCIO
      BRINDES
    ```

2. Executar o Script:

    - Ative o ambiente virtual criado pelo pipenv:
      ```bash
        pipenv shell
      ```
    - Execute o script:
    ```bash
        python index.py
    ```

3. Resultado:
    - O arquivo dados_traduzidos.json será gerado ou atualizado com as traduções correspondentes.

### Personalização
Você pode alterar os idiomas de destino modificando o código no script. Atualmente, o script traduz para português (pt), espanhol (es) e inglês (en)

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e sugestões.
