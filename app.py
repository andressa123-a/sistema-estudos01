import os
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Alterado para v3 para forçar o carregamento de todos os novos tópicos
DB_NAME = 'database_v3.db'

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
            ('Fase 1', 'Português', 'Interpretação: Tema do texto', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Ideia principal e secundárias', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Informações explícitas e implícitas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Inferência e Fato × opinião', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Finalidade, Argumentação e Tese', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Interpretação: Sentido no contexto e Linguagem verbal/não verbal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Fonemas, Encontros vocálicos/consonantais e Dígrafos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Divisão silábica, Ortografia e Acentuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Classes gramaticais e Formação de palavras', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Substantivo, Adjetivo, Artigo, Pronome e Verbo', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Gramática: Advérbio, Preposição, Conjunção, Numeral e Interjeição', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Sujeito, Predicado e Complementos', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Período simples e composto (Coordenadas/Subordinadas)', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Concordância verbal e nominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Regência verbal e nominal', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Sintaxe: Colocação pronominal e Pontuação', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Linguagem: Metáfora, Metonímia, Comparação, Ironia e Hipérbole', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Português', 'Linguagem: Antítese, Eufemismo, Personificação e Vícios', '⭐⭐⭐⭐⭐', 'A Estudar'),

            # 🔵 MATEMÁTICA ⭐⭐⭐⭐⭐ (FASE 1 e FASE 2)
            ('Fase 1', 'Matemática', 'Básica: Operações básicas, Frações e Decimais', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: Razão, Proporção e Porcentagem', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: Regra de três simples e composta', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Básica: MMC e MDC', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Expressões, Produtos notáveis e Fatoração', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Polinômios, Equação do 1º e 2º grau', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 1', 'Matemática', 'Álgebra: Sistemas de equações e Equações algébricas', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Funções: Conceito, Função do 1º e 2º grau', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Funções: Gráficos, Raízes, Crescimento e Vértice da parábola', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Conjuntos, Sequências, Matrizes e Determinantes', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Sistemas lineares, Análise combinatória e Probabilidade', '⭐⭐⭐', 'A Estudar'),
            ('Fase 2', 'Matemática', 'Outros: Trigonometria, Geometria plana e analítica, Exponenciais', '⭐⭐⭐', 'A Estudar'),

            # 🥉 HISTÓRIA (FASE 3)
            ('Fase 3', 'História', 'Brasil: Colônia, Independência, 1º/2º Reinado e República', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', 'Brasil: Era Vargas, Ditadura Militar e Redemocratização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'História', 'Geral: Rev. Industrial, I/II Guerra Mundial, Guerra Fria e Contemporânea', '⭐⭐⭐', 'A Estudar'),

            # 🌎 GEOGRAFIA (FASE 3)
            ('Fase 3', 'Geografia', 'População, Migrações, Urbanização e Industrialização', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', 'Globalização, Economia BR, Agricultura e Recursos Naturais', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Geografia', 'Meio Ambiente, Mudanças Climáticas, Geopolítica e Conflitos', '⭐⭐⭐', 'A Estudar'),

            # 🧬 BIOLOGIA (FASE 3)
            ('Fase 3', 'Biologia', 'Célula, Genética, Evolução e Ecologia', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', 'Cadeias alimentares, Relações ecológicas e Ciclos biogeoquímicos', '⭐⭐⭐', 'A Estudar'),
            ('Fase 3', 'Biologia', 'Corpo humano, Sistemas, Reprodução e Saúde/Doenças', '⭐⭐⭐', 'A Estudar'),

            # ⚗️ QUÍMICA (FASE 3)
            ('Fase 3', 'Química', 'Matéria, Átomo, Tabela periódica e Ligações', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', 'Funções, Reações, Balanceamento, Soluções, Concentração e pH', '⭐', 'A Estudar'),
            ('Fase 3', 'Química', 'Química Ambiental', '⭐', 'A Estudar'),

            # ⚡ FÍSICA (FASE 3)
            ('Fase 3', 'Física', 'Movimento, Velocidade, Aceleração e Leis de Newton', '⭐', 'A Estudar'),
            ('Fase 3', 'Física', 'Força, Trabalho, Energia, Potência, Calor, Temperatura, Pressão e Eletricidade', '⭐', 'A Estudar'),

            # 📰 ATUALIDADES (FASE 3)
            ('Fase 3', 'Atualidades', 'Brasil, Política internacional, Economia e Meio Ambiente', '⭐', 'A Estudar'),
            ('Fase 3', 'Atualidades', 'Ciência, Tecnologia, Saúde, Questões sociais e Acontecimentos de 2026', '⭐', 'A Estudar'),

            # 🔴 REDAÇÃO ⭐⭐⭐⭐⭐ (DIÁRIO)
            ('Diário', 'Redação', 'Estrutura: Introdução, Desenvolvimento, Conclusão, Coerência e Coesão', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', 'Língua Portuguesa: Ortografia, Pontuação, Concordância e Vocabulário', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Educação / Saúde / Tecnologia / IA', '⭐⭐⭐⭐⭐', 'A Estudar'),
            ('Diário', 'Redação', 'Treino: Redação sobre Meio Ambiente / Desigualdade / Juventude / Violência', '⭐⭐⭐⭐⭐', 'A Estudar')
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
