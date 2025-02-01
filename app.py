from PyPDF2 import PdfReader
import openai
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Criar um cliente OpenAI
api_key = os.getenv("KEY_API_OPENAI")

client = openai.OpenAI(api_key=api_key)

def extrair_texto_pdf(path_pdf):
    reader = PdfReader(path_pdf)

    texto = ""
    
    for pagina in reader.pages:
        texto += pagina.extract_text()
    return texto

path = "proposta_01.pdf"
texto_extraido = extrair_texto_pdf(path)

def extrair_precos_unitarios(texto):
    prompt = f"""No texto abaixo, identifique os insumos da construção civil e seus respectivos preços unitários. Retorne os dados em formato JSON com os campos "Insumo", "Unidade" e "Preço Unitário".
                 
                 Texto: {texto}"""

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Ou gpt-4, se preferir
        messages=[{"role": "system", "content": "Você é um assistente especializado em extração de dados de texto."},
                  {"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.3
    )

    return resposta.choices[0].message.content.strip()

dados_processados = extrair_precos_unitarios(texto_extraido)

print(dados_processados)