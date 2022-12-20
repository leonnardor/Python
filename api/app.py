from flask import Flask, jsonify, request

app = Flask(__name__)

jogos = [
    {
        'id': 1,
        'nome': 'Super Mario World',
        'categoria': 'Plataforma'
    },
    {
        'id': 2,
        'nome': 'Super Mario Kart',
        'categoria': 'Corrida'
    },
    {
        'id': 3,
        'nome': 'Super Mario 64',
        'categoria': 'Plataforma'
    },
    {
        'id': 4,
        'nome': 'Battlefield 4',
        'categoria': 'FPS'
    },
    {
        'id': 5,
        'nome': 'Battlefield 1',
        'categoria': 'FPS'
    },
]

# Consultar(todos)
@app.route('/jogos', methods=['GET'])
def obter_jogos():
    return jsonify(jogos)

#consulta um jogo pelo id
@app.route('/jogos/<int:id>', methods=['GET'])
def obter_jogo(id):
    jogo = [jogo for jogo in jogos if jogo['id'] == id]
    if len(jogo) > 0:
        return jsonify(jogo[0])
    return jsonify({'mensagem': 'Jogo não encontrado'})

#inserir um jogo
@app.route('/jogos', methods=['POST'])
def adicionar_jogo():
    dados = request.get_json()
    id = len(jogos) + 1
    nome = dados['nome']
    categoria = dados['categoria']
    novo_jogo = {
        'id': id,
        'nome': nome,
        'categoria': categoria
    }
    jogos.append(novo_jogo)
    return jsonify(novo_jogo)

#alterar um jogo
@app.route('/jogos/<int:id>', methods=['PUT'])
def alterar_jogo(id):
    dados = request.get_json()
    jogo = [jogo for jogo in jogos if jogo['id'] == id]
    if len(jogo) > 0:
        jogo[0]['nome'] = dados['nome']
        jogo[0]['categoria'] = dados['categoria']
        return jsonify(jogo[0])
    return jsonify({'mensagem': 'Jogo não encontrado'})

#deletar um jogo
@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = [jogo for jogo in jogos if jogo['id'] == id]
    if len(jogo) > 0:
        jogos.remove(jogo[0])
        return jsonify({'mensagem': 'Jogo removido com sucesso'})
    return jsonify({'mensagem': 'Jogo não encontrado'})




app.run(port=5000, debug=True, host='localhost')