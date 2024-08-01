import sqlite3

def setup_database():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_nome TEXT(50) NOT NULL,
            endereco TEXT(100) NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()