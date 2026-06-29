import os
import pg8000
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection = pg8000.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            port=int(os.environ.get('DB_PORT'))
        )
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def execute_query(sql, params=None, fetch=False):
    connection = get_db_connection()
    if connection is None:
        return None

    response = None

    try:
        cursor = connection.cursor()
        cursor.execute(sql, params) if params else cursor.execute(sql)

        if fetch:
            results = cursor.fetchall()
            colunas = [col[0] for col in cursor.description]
            response = [dict(zip(colunas, row)) for row in results]
        else:
            connection.commit()
            response = True

        cursor.close()

    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        connection.rollback()
        return None

    finally:
        connection.close()

    return response