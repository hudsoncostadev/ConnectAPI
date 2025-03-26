from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Configuração de conexão com o banco
DB_CONFIG = {
    'dbname': 'testedenivelamento',
    'user': 'postgres',
    'password': 'hudson3254',
    'host': 'localhost',
    'port': '5432'
}
@app.route('/api/operadoras', methods=['GET'])
def get_operadoras():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT nome_fantasia, cnpj, razao_social FROM operadoras_ativas LIMIT 10;")
        resultados = cursor.fetchall()
        operadoras = [{'nome_fantasia': row[0], 'cnpj': row[1], 'razao_social': row[2]} for row in resultados]
        cursor.close()
        conn.close()
        return jsonify(operadoras)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)