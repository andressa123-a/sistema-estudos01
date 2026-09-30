import os
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Nome do banco v15 para carregar a lista completa de subtópicos
DB_NAME = 'database_v15.db'

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
            # 🟣 PORTUGUÊS ⭐⭐⭐⭐⭐
            ('Fase 1', 'Português', '📖 Interpretação: Tema do texto', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Ideia principal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Ideias secundárias', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Informações explícitas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Informações implícitas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Inferência', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Fato × opinião', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Finalidade do texto', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Argumentação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Tese', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Conclusão', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Sentido de palavras no contexto', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Linguagem verbal e não verbal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '📖 Interpretação: Relação entre partes do texto', '⭐⭐⭐⭐⭐', 'A Estudar'),

            ('Fase 1', 'Português', '✏️ Gramática: Fonemas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Encontros vocálicos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Encontros consonantais', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Dígrafos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Divisão silábica', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Ortografia', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Acentuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Classes gramaticais', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Formação de palavras', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Substantivo', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Adjetivo', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️️ Gramática: Artigo', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Pronome', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Verbo', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️️ Gramática: Advérbio', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Preposição', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Conjunção', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Numeral', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '✏️ Gramática: Interjeição', '⭐⭐⭐⭐⭐', 'A Estudar'),

            ('Fase 1', 'Português', '🔤 Sintaxe: Sujeito', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Predicado', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Complementos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Período simples', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Período composto', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Orações coordenadas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Orações subordinadas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Concordância verbal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Concordância nominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Regência verbal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Regência nominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Colocação pronominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🔤 Sintaxe: Pontuação', '⭐⭐⭐⭐⭐', 'A Estudar'),

            ('Fase 1', 'Português', '🎭 Linguagem: Metáfora', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Metonímia', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Comparação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Ironia', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Hipérbole', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Antítese', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Eufemismo', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Personificação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', '🎭 Linguagem: Vícios de linguagem', '⭐⭐⭐⭐⭐', 'A Estudar'),

            # 🔵 MATEMÁTICA ⭐⭐⭐⭐⭐
            ('Fase 1', 'Matemática', '🧮 Básica: Operações básicas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Frações', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Números decimais', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Razão', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Proporção', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Regra de três simples', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Regra de três composta', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: Porcentagem', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: MMC', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '🧮 Básica: MDC', '⭐⭐⭐⭐⭐', 'A Estudar'),

            ('Fase 1', 'Matemática', '📐 Álgebra: Expressões algébricas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Produtos notáveis', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Fatoração', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Polinômios', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Equação do 1º grau', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Equação do 2º grau', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Sistemas de equações', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', '📐 Álgebra: Equações algébricas', '⭐⭐⭐⭐⭐', 'A Estudar'),

            ('Fase 2', 'Matemática', '📈 Funções: Conceito de função', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '📈 Funções: Função do 1º grau', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '📈 Funções: Função do 2º grau', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '📈 Funções: Gráficos', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '📈 Funções: Raízes', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '📈 Funções: Crescimento e decrescimento', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '📈 Funções: Vértice da parábola', '⭐⭐⭐', 'A Estudar'),

            ('Fase 2', 'Matemática', '🎲 Outros: Conjuntos', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Sequências', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Matrizes', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Determinantes', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Sistemas lineares', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Análise combinatória', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Probabilidade', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Trigonometria', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Geometria plana', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Geometria analítica', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', '🎲 Outros: Equações exponenciais', '⭐⭐⭐', 'A Estudar'),

            # 📜 HISTÓRIA ⭐⭐⭐
            ('Fase 3', 'História', '📜 Brasil Colônia', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Independência do Brasil', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Primeiro e Segundo Reinado', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 República', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Era Vargas', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Ditadura Militar', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Redemocratização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Revolução Industrial', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Primeira Guerra Mundial', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Segunda Guerra Mundial', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Guerra Fria', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', '📜 Acontecimentos do mundo contemporâneo', '⭐⭐⭐', 'A Estudar'),

            # 🌎 GEOGRAFIA ⭐⭐⭐
            ('Fase 3', 'Geografia', '🌎 População', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Migrações', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Urbanização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Industrialização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Globalização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Economia brasileira', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Agricultura', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Recursos naturais', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Meio ambiente', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Mudanças climáticas', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Geopolítica', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', '🌎 Conflitos internacionais', '⭐⭐⭐', 'A Estudar'),

            # 🧬 BIOLOGIA ⭐⭐⭐
            ('Fase 3', 'Biologia', '🧬 Célula', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Genética', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Evolução', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Ecologia', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Cadeias alimentares', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Relações ecológicas', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Ciclos biogeoquímicos', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Corpo humano e Sistemas', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Reprodução', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', '🧬 Saúde e doenças', '⭐⭐⭐', 'A Estudar'),

            # ⚗️ QUÍMICA ⭐
            ('Fase 3', 'Química', '⚗️ Matéria', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Átomo', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Tabela periódica', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Ligações químicas', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Funções químicas', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Reações químicas', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Balanceamento', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Soluções e Concentração', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ pH', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', '⚗️ Química ambiental', '⭐', 'A Estudar'),

            # ⚡ FÍSICA ⭐
            ('Fase 3', 'Física', '⚡ Movimento, Velocidade e Aceleração', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', '⚡ Leis de Newton e Força', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', '⚡ Trabalho, Energia e Potência', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', '⚡ Calor e Temperatura', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', '⚡ Pressão', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', '⚡ Eletricidade', '⭐', 'A Estudar'),

            # 📰 ATUALIDADES ⭐
            ('Fase 3', 'Atualidades', '📰 Brasil e Política internacional', '⭐', 'A Estudar'),
            ('Fase 3', 'Atualidades', '📰 Economia e Meio ambiente', '⭐', 'A Estudar'),
            ('Fase 3', 'Atualidades', '📰 Ciência e Tecnologia', '⭐', 'A Estudar'),
            ('Fase 3', 'Atualidades', '📰 Saúde e Questões sociais', '⭐', 'A Estudar'),
            ('Fase 3', 'Atualidades', '📰 Conflitos internacionais', '⭐', 'A Estudar'),
            ('Fase 3', 'Atualidades', '📰 Principais acontecimentos de 2026', '⭐', 'A Estudar'),

            # 🔴 REDAÇÃO ⭐⭐⭐⭐⭐
            ('Diário', 'Redação', '✍️ Estrutura: Introdução, Desenvolvimento e Conclusão', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Estrutura: Organização, Coerência, Coesão e Clareza', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️️ Estrutura: Argumentação e Adequação ao tema', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Gramática: Ortografia, Acentuação e Pontuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Gramática: Concordância, Regência e Vocabulário', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Treino: Redação sobre Educação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Treino: Redação sobre Tecnologia / IA', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Treino: Redação sobre Saúde', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Treino: Redação sobre Meio Ambiente', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', '✍️ Treino: Redação sobre Desigualdade / Violência / Redes Sociais', '⭐⭐⭐⭐⭐', 'A Estudar')
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
