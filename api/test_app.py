import unittest
from app import app
from flask import jsonify

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_obter_jogos(self):
        response = self.app.get('/jogos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [
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
        ])

    def test_obter_jogo(self):
        response = self.app.get('/jogos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'id': 1,
            'nome': 'Super Mario World',
            'categoria': 'Plataforma'
        })

    def test_obter_jogo_inexistente(self):
        response = self.app.get('/jogos/6')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'mensagem': 'Jogo não encontrado'})

    def test_adicionar_jogo(self):
        response = self.app.post('/jogos', json={
            'nome': 'Teste',
            'categoria': 'Teste'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'id': 6,
            'nome': 'Teste',
            'categoria': 'Teste'
        })

    def test_adicionar_jogo_sem_nome(self):
        response = self.app.post('/jogos', json={
            'categoria': 'Teste'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'mensagem': 'O campo nome é obrigatório'})

    def test_adicionar_jogo_sem_categoria(self):
        response = self.app.post('/jogos', json={
            'nome': 'Teste'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'mensagem': 'O campo categoria é obrigatório'})

    def test_adicionar_jogo_sem_nome_e_categoria(self):
        response = self.app.post('/jogos', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {
            'mensagem': 'O campo nome é obrigatório',
            'mensagem': 'O campo categoria é obrigatório'
        })

    def test_remover_jogo(self):
        response = self.app.delete('/jogos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'mensagem': 'Jogo removido com sucesso'})

    def test_remover_jogo_inexistente(self):
        response = self.app.delete('/jogos/6')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'mensagem': 'Jogo não encontrado'})

    def test_atualizar_jogo(self):
        response = self.app.put('/jogos/1', json={
            'nome': 'Teste',
            'categoria': 'Teste'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'id': 1,
            'nome': 'Teste',
            'categoria': 'Teste'
        })
        
    def test_atualizar_jogo_inexistente(self):
        response = self.app.put('/jogos/6', json={
            'nome': 'Teste',
            'categoria': 'Teste'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'mensagem': 'Jogo não encontrado'})

    def test_atualizar_jogo_sem_nome(self):
        response = self.app.put('/jogos/1', json={
            'categoria': 'Teste'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'mensagem': 'O campo nome é obrigatório'})

    def test_atualizar_jogo_sem_categoria(self):
        response = self.app.put('/jogos/1', json={
            'nome': 'Teste'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'mensagem': 'O campo categoria é obrigatório'})

    def test_atualizar_jogo_sem_nome_e_categoria(self):
        response = self.app.put('/jogos/1', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {
            'mensagem': 'O campo nome é obrigatório',
            'mensagem': 'O campo categoria é obrigatório'
        })

        

if __name__ == '__main__':
    unittest.main()
