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
            # 🥇 FASE 1 — GARANTIR PONTOS (Prioridade ⭐⭐⭐⭐⭐)
            ('Fase 1', 'Português', 'Interpretação: Tema, Ideias principal e secundárias', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Info. explícitas/implícitas e Inferência', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Fato vs Opinião e Finalidade do texto', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Argumentação, Tese e Conclusão', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Sentido no contexto e Linguagem verbal/não verbal', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Fonemas, Encontros vocálicos/consonantais e Dígrafos', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Divisão silábica, Ortografia e Acentuação', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Substantivo, Adjetivo, Artigo e Pronome', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Verbo, Advérbio, Preposição e Conjunção', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Numeral e Interjeição', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Sujeito, Predicado e Complementos', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Período simples e composto (Orações)', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Concordância verbal e nominal', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Regência verbal e nominal', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Colocação pronominal e Pontuação', 5, 'A Estudar'),
            ('Fase 1', 'Português', 'Linguagem: Figuras de linguagem e Vícios', 3, 'A Estudar'),

            ('Fase 1', 'Matemática', 'Básica: Operações, Frações e Decimais', 5, 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: Razão, Proporção e Porcentagem', 5, 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: Regra de três simples e composta', 5, 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: MMC e MDC', 5, 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Expressões, Produtos notáveis e Fatoração', 5, 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Equação do 1º e 2º grau', 5, 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Sistemas de equações e Polinômios', 5, 'A Estudar'),

            # 🥈 FASE 2 — SUBIR A NOTA (Prioridade ⭐⭐⭐)
            ('Fase 2', 'Matemática', 'Funções: Conceito, Função do 1º e 2º grau', 3, 'A Estudar'),
            ('Fase 2', 'Matemática', 'Funções: Gráficos, Raízes e Vértice da parábola', 3, 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Geometria Plana e Analítica', 3, 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Análise Combinatória e Probabilidade', 3, 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Trigonometria e Equações exponenciais', 3, 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Conjuntos, Sequências e Matrizes', 3, 'A Estudar'),

            # 🥉 FASE 3 — CONHECIMENTOS GERAIS (Prioridade ⭐ a ⭐⭐⭐)
            ('Fase 3', 'História', 'Brasil: Colônia, Independência, Reinado, República e Vargas', 3, 'A Estudar'),
            ('Fase 3', 'História', 'Brasil: Ditadura Militar e Redemocratização', 3, 'A Estudar'),
            ('Fase 3', 'História', 'Geral: Rev. Industrial, I/II Guerra e Guerra Fria', 3, 'A Estudar'),
            ('Fase 3', 'Geografia', 'População, Migrações, Urbanização e Industrialização', 3, 'A Estudar'),
            ('Fase 3', 'Geografia', 'Globalização, Economia BR, Meio Ambiente e Geopolítica', 3, 'A Estudar'),
            ('Fase 3', 'Biologia', 'Célula, Genética, Evolução e Ecologia', 3, 'A Estudar'),
            ('Fase 3', 'Biologia', 'Corpo Humano, Sistemas, Reprodução e Saúde', 3, 'A Estudar'),
            ('Fase 3', 'Química', 'Matéria, Átomo, Tabela Periódica e Ligações', 1, 'A Estudar'),
            ('Fase 3', 'Química', 'Reações, Soluções, Concentração e pH', 1, 'A Estudar'),
            ('Fase 3', 'Física', 'Movimento, Leis de Newton, Força e Energia', 1, 'A Estudar'),
            ('Fase 3', 'Física', 'Calor, Temperatura, Pressão e Eletricidade', 1, 'A Estudar'),
            ('Fase 3', 'Atualidades', 'Acontecimentos Globais, Ciência, Tecnologia e Sociedade', 1, 'A Estudar'),

            # ✍️ ROTINA DIÁRIA — REDAÇÃO (100 Pontos ⭐⭐⭐⭐⭐)
            ('Diário', 'Redação', 'Estrutura: Introdução, Desenvolvimento e Conclusão', 5, 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Tecnologia / Inteligência Artificial', 5, 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Educação / Saúde / Juventude', 5, 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Meio Ambiente / Violência / Redes Sociais', 5, 'A Estudar')
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
