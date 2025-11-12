# Importa bibliotecas necessárias
import boto3  # Biblioteca oficial da AWS para Python
import json   # Biblioteca para manipulação de JSON

# Função principal Lambda
def lambda_handler(event, context):
    """
    event: contém dados da requisição HTTP (como o prompt enviado pelo usuário)
    context: fornece informações sobre a execução da função Lambda
    """
    
    # Cria um cliente para interagir com o Amazon Bedrock
    # 'bedrock-runtime' é o serviço que permite invocar modelos gerativos
    client = boto3.client('bedrock-runtime', region_name='us-east-1')

    # Extrai o prompt enviado pelo usuário da requisição HTTP
    # Caso nenhum prompt seja enviado, usa um padrão
    prompt = event.get("prompt", "Explique o que é IA Generativa de forma simples.")

    # Monta o corpo da requisição para enviar ao modelo Titan
    # - inputText: texto que será processado pelo modelo
    # - textGenerationConfig: parâmetros que controlam o comportamento do modelo
    body = json.dumps({
        "inputText": prompt,        # O texto que será processado
        "textGenerationConfig": {
            "temperature": 0.7,    # Controla a criatividade das respostas (0 = conservador, 1 = criativo)
            "maxTokenCount": 256,  # Máximo de tokens (palavras/pedaços de palavras) na resposta
            "topP": 0.9            # Controle de probabilidade cumulativa para amostragem (nuclear sampling)
            # "stopSequences": []   # Opcional: lista de sequências que interrompem a geração
        }
    })

    # Envia a requisição para o modelo Amazon Titan Text Express
    response = client.invoke_model(
        modelId="amazon.titan-text-express-v1",  # Modelo da própria Amazon
        contentType="application/json",         # Tipo de conteúdo enviado
        accept="application/json",              # Tipo de resposta esperado
        body=body                               # Corpo da requisição (prompt e configurações)
    )

    # Lê a resposta do modelo
    # 'response['body']' é um objeto de stream, por isso usamos read()
    # Em seguida, convertemos de JSON para dicionário Python
    result = json.loads(response['body'].read())

    # Extrai o texto gerado pelo modelo
    # 'results' é uma lista de respostas (normalmente com apenas 1 item)
    answer = result['results'][0]['outputText']

    # Retorna a resposta em formato JSON para o usuário
    # statusCode 200 indica que a requisição foi bem-sucedida
    return {
        "statusCode": 200,
        "body": json.dumps({"response": answer})
    }
