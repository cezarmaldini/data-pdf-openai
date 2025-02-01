# 📄 Extração de Preços Unitários de Insumos da Construção Civil

Este projeto utiliza **Python**, a biblioteca **PyPDF2** para extração de texto de arquivos PDF e a API da **OpenAI** para processar e estruturar os dados extraídos. O objetivo é identificar insumos da construção civil e seus respectivos preços unitários.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12+
- [Poetry](https://python-poetry.org/) (gerenciamento de dependências)
- PyPDF2 (extração de texto de PDFs)
- OpenAI API (GPT-3.5 Turbo para processamento de texto)
- Dotenv (gerenciamento de variáveis de ambiente)

---

## 📌 Pré-requisitos

Antes de começar, certifique-se de ter o **Poetry** instalado:

```sh
pip install poetry
```

Além disso, você precisará de uma **chave da API OpenAI**. Caso ainda não tenha, crie uma conta em [OpenAI](https://platform.openai.com/) e gere uma chave de API.

---

## 🔧 Instalação

1. **Clone o repositório**
   ```sh
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Instale as dependências com Poetry**
   ```sh
   poetry install
   ```

3. **Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:**
   ```env
   KEY_API_OPENAI="sua-chave-aqui"
   ```

4. **Execute o script**
   ```sh
   poetry run python app.py
   ```

---

## 📜 Funcionamento do Código

1. O script lê um arquivo PDF e extrai o texto utilizando **PyPDF2**.
2. O texto extraído é enviado para a API da OpenAI com um prompt que solicita a identificação dos insumos e preços unitários.
3. A resposta da OpenAI é formatada em JSON e exibida no terminal.

---

## 📂 Estrutura do Projeto
```
📁 nome-do-repositorio
│── 📄 app.py              # Código principal
│── 📄 pyproject.toml      # Configuração do Poetry
│── 📄 README.md           # Documentação do projeto
│── 📄 .env                # Exemplo do arquivo de variáveis de ambiente
```

---

## 📌 Melhorias Futuras
- Criar uma interface gráfica para upload de arquivos PDF.
- Melhorar o tratamento de erros e logs.
- Suporte a múltiplos PDFs simultaneamente.

---

## 🤝 Contribuição
Sinta-se à vontade para contribuir! Faça um **fork** do repositório, crie um **branch**, implemente as melhorias e envie um **pull request**.

---

🚀 Desenvolvido por **Cezar Maldini** 🎯