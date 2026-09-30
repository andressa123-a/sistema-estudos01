import os
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fase TEXT NOT NULL,
            materia TEXT NOT NULL,
            nome TEXT NOT NULL,
            prioridade INTEGER NOT NULL,
            status TEXT DEFAULT 'A Estudar'
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM topicos')
    if cursor.fetchone()[0] == 0:
        dados_iniciais = [
            ('Fase 1', 'Português', 'Interpretação de Texto', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática Básica & Classes Gramaticais', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe, Regência e Concordância', 5, 'A Estudar'),
            ('Fase 1', 'Matemática', 'Matemática Básica & Razão/Proporção', 5, 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra e Equações do 1º/2º grau', 5, 'A Estudar'),
            ('Fase 2', 'Matemática', 'Funções e Gráficos', 3, 'A Estudar'),
            ('Fase 2', 'Matemática', 'Geometria Plana e Analítica', 3, 'A Estudar'),
            ('Fase 2', 'Matemática', 'Análise Combinatória e Probabilidade', 3, 'A Estudar'),
            ('Fase 3', 'História', 'História do Brasil e Conflitos Mundiais', 1, 'A Estudar'),
            ('Fase 3', 'Geografia', 'Geografia Humana e Meio Ambiente', 1, 'A Estudar'),
            ('Fase 3', 'Biologia', 'Ecologia, Genética e Saúde', 1, 'A Estudar'),
            ('Fase 3', 'Química/Física', 'Conceitos Fundamentais e Fórmulas', 1, 'A Estudar'),
            ('Diário', 'Redação', 'Treino Diário (20-30 min) / Esqueleto', 5, 'A Estudar')
        ]
        cursor.executemany('INSERT INTO topicos (fase, materia, nome, prioridade, status) VALUES (?, ?, ?, ?, ?)', dados_iniciais)
        conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/topicos', methods=['GET'])
def get_topicos():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, fase, materia, nome, prioridade, status FROM topicos')
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'id': r[0], 'fase': r[1], 'materia': r[2], 'nome': r[3], 'prioridade': r[4], 'status': r[5]} for r in rows])

@app.route('/api/topicos/atualizar', methods=['POST'])
def atualizar_status():
    data = request.json
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE topicos SET status = ? WHERE id = ?', (data['status'], data['id']))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
