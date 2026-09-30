import os
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Nome do banco atualizado para forçar o recarregamento completo dos tópicos
DB_NAME = 'database_v4.db'

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
        dados_iniciais = [
            # 🟣 PORTUGUÊS ⭐⭐⭐⭐⭐ (FASE 1)
            ('Fase 1', 'Português', 'Interpretação: Tema, Ideia principal e secundárias', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Info. explícitas/implícitas e Inferência', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Fato × opinião, Tese e Argumentação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Sentido no contexto e Linguagem verbal/não verbal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Fonemas, Encontros vocálicos/consonantais e Dígrafos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Divisão silábica, Ortografia e Acentuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Substantivo, Adjetivo, Artigo, Pronome e Verbo', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Advérbio, Preposição, Conjunção, Numeral e Interjeição', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Sujeito, Predicado e Complementos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Período simples e composto (Orações)', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Concordância verbal e nominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Regência verbal e nominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Colocação pronominal e Pontuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Linguagem: Figuras de linguagem e Vícios de linguagem', '⭐⭐⭐⭐⭐', 'A Estudar'),

            # 🔵 MATEMÁTICA ⭐⭐⭐⭐⭐ (FASE 1 e FASE 2)
            ('Fase 1', 'Matemática', 'Básica: Operações, Frações e Decimais', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: Razão, Proporção e Porcentagem', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: Regra de três simples e composta', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: MMC e MDC', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Expressões, Produtos notáveis e Fatoração', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Polinômios, Equação do 1º e 2º grau', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Sistemas de equações e Equações algébricas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Funções: Conceito, Função do 1º e 2º grau', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Funções: Gráficos, Raízes e Vértice da parábola', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Conjuntos, Sequências, Matrizes e Determinantes', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Análise combinatória, Probabilidade e Trigonometria', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Geometria Plana/Analítica e Equações Exponenciais', '⭐⭐⭐', 'A Estudar'),

            # 📜 HISTÓRIA (FASE 3)
            ('Fase 3', 'História', 'Brasil: Colônia, Independência, 1º/2º Reinado e República', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', 'Brasil: Era Vargas, Ditadura Militar e Redemocratização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', 'Geral: Rev. Industrial, I/II Guerra e Guerra Fria', '⭐⭐⭐', 'A Estudar'),

            # 🌎 GEOGRAFIA (FASE 3)
            ('Fase 3', 'Geografia', 'População, Migrações, Urbanização e Industrialização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', 'Globalização, Economia BR, Meio Ambiente e Geopolítica', '⭐⭐⭐', 'A Estudar'),

            # 🧬 BIOLOGIA (FASE 3)
            ('Fase 3', 'Biologia', 'Célula, Genética, Evolução e Ecologia', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', 'Corpo humano, Sistemas, Reprodução e Saúde', '⭐⭐⭐', 'A Estudar'),

            # ⚗️ QUÍMICA (FASE 3)
            ('Fase 3', 'Química', 'Matéria, Átomo, Tabela periódica e Ligações', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', 'Reações, Soluções, Concentração, pH e Química Ambiental', '⭐', 'A Estudar'),

            # ⚡ FÍSICA (FASE 3)
            ('Fase 3', 'Física', 'Movimento, Velocidade, Aceleração e Leis de Newton', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', 'Força, Energia, Calor, Pressão e Eletricidade', '⭐', 'A Estudar'),

            # 📰 ATUALIDADES (FASE 3)
            ('Fase 3', 'Atualidades', 'Política, Economia, Ciência, Tecnologia e Acontecimentos de 2026', '⭐', 'A Estudar'),

            # 🔴 REDAÇÃO ⭐⭐⭐⭐⭐ (DIÁRIO)
            ('Diário', 'Redação', 'Estrutura: Introdução, Desenvolvimento e Conclusão', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Educação / Saúde / Tecnologia / IA', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Meio Ambiente / Violência / Redes Sociais', '⭐⭐⭐⭐⭐', 'A Estudar')
        ]
        cursor.executemany('INSERT INTO topicos (fase, materia, nome, prioridade, status) VALUES (?, ?, ?, ?, ?)', dados_iniciais)
        conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/topicos', methods=['GET'])
def get_topicos():
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
