from PyPDF2 import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os
import pandas as pd
import json

# Carregar variáveis do arquivo .env
load_dotenv()

nome_arquivo = input("Digite o nome do arquivo:")

# Configurar a chave da API do Gemini
api_key = os.getenv("KEY_API_GEMINI")
genai.configure(api_key=api_key)

def extrair_texto_pdf(path_pdf):
    """ Extrai o texto de um arquivo PDF. """
    reader = PdfReader(path_pdf)
    texto = "".join([pagina.extract_text() for pagina in reader.pages if pagina.extract_text()])
    return texto

path = "proposta_07.pdf"
texto_extraido = extrair_texto_pdf(path)

def extrair_precos_unitarios(texto):
    """ Envia o texto para o Gemini e extrai os preços unitários. """
    prompt = f"""No texto abaixo, identifique os insumos da construção civil e seus respectivos preços unitários.
                Leve em consideração que os insumos podem ter informações técnicas, como diâmetro, comprimento e outras características. Portanto, busque as descrições dos insumos com o máximo de detalhes possível.
                 Retorne os dados em formato JSON, com os campos:
                 - "Insumo"
                 - "Unidade"
                 - "Preço Unitário"

                 Certifique-se de que a saída seja **apenas um JSON puro**, sem explicações ou comentários adicionais.
                 
                 Texto: {texto}"""

    modelo = genai.GenerativeModel("gemini-pro")  
    resposta = modelo.generate_content(prompt)  

    # Exibir resposta para depuração
    print("🔹 Resposta bruta do Gemini:")
    print(resposta.text)

    return resposta.text  

# Extrair dados
dados_processados = extrair_precos_unitarios(texto_extraido)

# Remover possíveis marcadores ```json ... ```
dados_processados = dados_processados.strip("```json").strip("```")

# Tentar converter para JSON
try:
    dados_json = json.loads(dados_processados)
except json.JSONDecodeError:
    print("❌ Erro ao converter a resposta em JSON. Salvando resposta bruta para análise...")
    with open("resposta_bruta.txt", "w", encoding="utf-8") as f:
        f.write(dados_processados)
    exit()

# Criar DataFrame Pandas
df = pd.DataFrame(dados_json)

# Corrigir possíveis problemas de codificação
df.columns = ["Insumo", "Unidade", "Preço Unitário"]
df["Preço Unitário"] = (
    df["Preço Unitário"]
    .astype(str)
    .str.replace("R$", "", regex=True)  # Remove o símbolo "R$"
    .str.replace(",", ".")  # Substitui vírgula por ponto
    .str.strip()  # Remove espaços extras
    .astype(float)  # Converte para float
)

# Salvar em CSV corretamente formatado
df.to_csv(nome_arquivo,index=False, encoding="utf-8-sig", sep=";")

print(f"✅ Arquivo CSV salvo em: {nome_arquivo}")