import os
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

DB_NAME = 'database_v10.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fase TEXT NOT NULL,
            materia TEXT NOT NULL,
            nome TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            status TEXT DEFAULT 'A Estudar'
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM topicos')
    if cursor.fetchone()[0] == 0:
        dados = [
            # Português
            ('Fase 1', 'Português', 'Interpretação: Tema, Ideias principais/secundárias', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Informações explícitas e implícitas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Fonemas, Ortografia e Acentuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Classes gramaticais e Verbos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Concordância, Regência e Pontuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Linguagem: Figuras e Vícios de linguagem', '⭐⭐⭐⭐⭐', 'A Estudar'),
            # Matemática
            ('Fase 1', 'Matemática', 'Básica: Operações, Frações, Decimais, Porcentagem', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: Razão, Proporção, Regra de três, MMC/MDC', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Produtos Notáveis, Fatoração, Equações 1º/2º grau', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Funções: Conceito, Gráficos e Parábola', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Geometria, Análise Combinatória e Probabilidade', '⭐⭐⭐', 'A Estudar'),
            # Conhecimentos Gerais
            ('Fase 3', 'História', 'Brasil: Colônia, Império, República, Vargas e Ditadura', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', 'População, Urbanização, Meio Ambiente e Geopolítica', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', 'Célula, Genética, Evolução, Ecologia e Corpo Humano', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Química', 'Matéria, Átomo, Tabela Periódica, Reações e pH', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', 'Movimento, Leis de Newton, Energia e Eletricidade', '⭐', 'A Estudar'),
            ('Fase 3', 'Atualidades', 'Acontecimentos Globais, Ciência e Sociedade (2026)', '⭐', 'A Estudar'),
            # Redação
            ('Diário', 'Redação', 'Estrutura: Introdução, Desenvolvimento e Conclusão', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Tecnologia / Inteligência Artificial', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Saúde / Educação / Meio Ambiente', '⭐⭐⭐⭐⭐', 'A Estudar')
        ]
        cursor.executemany('INSERT INTO topicos (fase, materia, nome, prioridade, status) VALUES (?, ?, ?, ?, ?)', dados)
        conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/topicos', methods=['GET'])
def get_topicos():
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, fase, materia, nome, prioridade, status FROM topicos')
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'id': r[0], 'fase': r[1], 'materia': r[2], 'nome': r[3], 'prioridade': r[4], 'status': r[5]} for r in rows])

@app.route('/api/topicos/atualizar', methods=['POST'])
def atualizar_status():
    data = request.json
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE topicos SET status = ? WHERE id = ?', (data['status'], data['id']))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
