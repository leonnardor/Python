from flask import Flask
import boto3
from credentials import aws_access_key_id, aws_secret_access_key

dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-east-1')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'


@app.route('/jogos')
def obter_jogos():
    table = dynamodb.Table('jogos')
    response = table.scan()
    return response['Items']

@app.route('/jogos/<int:id>')
def obter_jogo(id):
    table = dynamodb.Table('jogos')
    response = table.get_item(Key={'id': id})
    return response['Item']

@app.route('/jogos', methods=['POST'])
def adicionar_jogo():
    table = dynamodb.Table('jogos')
    dados = request.get_json()
    id = dados['id']
    nome = dados['nome']
    categoria = dados['categoria']
    response = table.put_item(
        Item={
            'id': id,
            'nome': nome,
            'categoria': categoria
        }
    )
    return response

@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    table = dynamodb.Table('jogos')
    dados = request.get_json()
    nome = dados['nome']
    categoria = dados['categoria']
    response = table.update_item(
        Key={
            'id': id
        },
        UpdateExpression='SET nome = :nome, categoria = :categoria',
        ExpressionAttributeValues={
            ':nome': nome,
            ':categoria': categoria
        }
    )
    return response

@app.route('/jogos/<int:id>', methods=['DELETE'])
def remover_jogo(id):
    table = dynamodb.Table('jogos')
    response = table.delete_item(
        Key={
            'id': id
        }
    )
    return response

    


if __name__ == '__main__':
    app.run()
