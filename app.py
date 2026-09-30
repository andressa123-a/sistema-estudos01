import os
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Nome do banco v12 para garantir que todos os dados novos entram limpos
DB_NAME = 'database_v12.db'

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
            # 🟣 PORTUGUÊS ⭐⭐⭐⭐⭐ (FASE 1)
            ('Fase 1', 'Português', '📖 Interpretação: Tema do texto, Ideia principal e secundárias', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Informações explícitas e implícitas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Inferência, Fato × opinião e Finalidade do texto', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Argumentação, Tese e Conclusão', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Sentido no contexto e Linguagem verbal/não verbal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Fonemas, Encontros vocálicos/consonantais e Dígrafos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Divisão silábica, Ortografia e Acentuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Classes gramaticais e Formação de palavras', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Substantivo, Adjetivo, Artigo, Pronome e Verbo', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Advérbio, Preposição, Conjunção, Numeral e Interjeição', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Sujeito, Predicado e Complementos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Período simples e composto (Orações Coordenadas/Subordinadas)', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Concordância verbal e nominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Regência verbal e nominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Colocação pronominal e Pontuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Metáfora, Metonímia, Comparação, Ironia e Hipérbole', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Antítese, Eufemismo, Personificação e Vícios de linguagem', '⭐⭐⭐⭐⭐', 'A Estudar'),

            # 🔵 MATEMÁTICA ⭐⭐⭐⭐⭐ (FASE 1 e FASE 2)
            ('Fase 1', 'Matemática', '🧮 Básica: Operações básicas, Frações e Decimais', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Razão, Proporção e Porcentagem', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Regra de três simples e composta', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: MMC e MDC', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Expressões algébricas, Produtos notáveis e Fatoração', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Polinômios, Equação do 1º e 2º grau', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Sistemas de equações e Equações algébricas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '📈 Funções: Conceito de função, Função do 1º e 2º grau', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '📈 Funções: Gráficos, Raízes, Crescimento e Vértice da parábola', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Conjuntos, Sequências, Matrizes e Determinantes', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Sistemas lineares, Análise combinatória e Probabilidade', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Trigonometria, Geometria plana e analítica, Exponenciais', '⭐⭐⭐', 'A Estudar'),

            # 📜 HISTÓRIA ⭐⭐⭐ (FASE 3)
            ('Fase 3', 'História', '📜 Brasil: Colônia, Independência, Primeiro e Segundo Reinado', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Brasil: República, Era Vargas, Ditadura Militar e Redemocratização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Geral: Rev. Industrial, I/II Guerra Mundial e Guerra Fria', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Geral: Principais acontecimentos do mundo contemporâneo', '⭐⭐⭐', 'A Estudar'),

            # 🌎 GEOGRAFIA ⭐⭐⭐ (FASE 3)
            ('Fase 3', 'Geografia', '🌎 População, Migrações, Urbanização e Industrialização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Globalização, Economia brasileira, Agricultura e Recursos naturais', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Meio ambiente, Mudanças climáticas, Geopolítica e Conflitos', '⭐⭐⭐', 'A Estudar'),

            # 🧬 BIOLOGIA ⭐⭐⭐ (FASE 3)
            ('Fase 3', 'Biologia', '🧬 Célula, Genética, Evolução e Ecologia', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Cadeias alimentares, Relações ecológicas e Ciclos biogeoquímicos', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Corpo humano, Sistemas do corpo, Reprodução, Saúde e doenças', '⭐⭐⭐', 'A Estudar'),

            # ⚗️ QUÍMICA ⭐ (FASE 3)
            ('Fase 3', 'Química', '⚗️ Matéria, Átomo, Tabela periódica e Ligações químicas', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Funções químicas, Reações químicas, Balanceamento e Soluções', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Concentração, pH e Química ambiental', '⭐', 'A Estudar'),

            # ⚡ FÍSICA ⭐ (FASE 3)
            ('Fase 3', 'Física', '⚡ Movimento, Velocidade, Aceleração e Leis de Newton', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', '⚡ Força, Trabalho, Energia, Potência, Calor e Temperatura', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', '⚡ Pressão e Eletricidade', '⭐', 'A Estudar'),

            # 📰 ATUALIDADES ⭐ (FASE 3)
            ('Fase 3', 'Atualidades', '📰 Brasil, Política internacional, Economia e Meio ambiente', '⭐', 'A Estudar'),
            ('Fase 3', 'Atualidades', '📰 Ciência, Tecnologia, Saúde, Questões sociais e Acontecimentos de 2026', '⭐', 'A Estudar'),

            # 🔴 REDAÇÃO ⭐⭐⭐⭐⭐ (DIÁRIO)
            ('Diário', 'Redação', '✍️ Estrutura: Introdução, Desenvolvimento, Conclusão, Coerência e Coesão', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Língua Portuguesa: Ortografia, Acentuação, Pontuação, Concordância e Regência', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Treino: Redação sobre Educação / Saúde / Tecnologia / Inteligência Artificial', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Treino: Redação sobre Meio Ambiente / Desigualdade / Juventude / Violência / Redes Sociais', '⭐⭐⭐⭐⭐', 'A Estudar')
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
