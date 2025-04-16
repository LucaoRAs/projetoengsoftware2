from app.extensions import mysql
import logging

logger = logging.getLogger('conexao_banco')

class Exame:
    @staticmethod
    def listar_exames():
        try:
            cursor = mysql.connection.cursor()
            logger.info("Conexão com o banco de dados efetuada com sucesso ou reutilizada")
            cursor.execute('SELECT * FROM exames')
            return cursor.fetchall()
        except Exception as e:
            logger.error(f"Erro ao listar exames: {e}", exc_info=True)
            print(f"Erro ao listar exames: {e}")
            return []
        finally:
            cursor.close()
            logger.info("Cursor fechado (fim da interação com banco)")

    @staticmethod
    def criar_exame(nome_paciente, nome, descricao, data_hora, status, preco):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('''
                INSERT INTO exames (nome_paciente, nome, descricao, data_hora, status, preco)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (nome_paciente, nome, descricao, data_hora, status, preco))
            mysql.connection.commit()
        except Exception as e:
            print(f"Erro ao criar exame: {e}")
            mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def editar_exame(id, nome_paciente, nome, descricao, data_hora, status, preco):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('''
                UPDATE exames
                SET nome_paciente=%s, nome=%s, descricao=%s, data_hora=%s, status=%s, preco=%s
                WHERE id=%s
            ''', (nome_paciente, nome, descricao, data_hora, status, preco, id))
            mysql.connection.commit()
        except Exception as e:
            print(f"Erro ao editar exame: {e}")
            mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def deletar_exame(id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('DELETE FROM exames WHERE id = %s', (id,))
            mysql.connection.commit()
        except Exception as e:
            print(f"Erro ao deletar exame: {e}")
            mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def buscar_exame_por_id(id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM exames WHERE id = %s', (id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar exame por ID: {e}")
            return None
        finally:
            cursor.close()

    @staticmethod
    def buscar_por_nome_paciente(nome_paciente):
        try:
            cursor = mysql.connection.cursor()
            like = f"%{nome_paciente}%"
            cursor.execute('SELECT * FROM exames WHERE nome_paciente LIKE %s', (like,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar por nome do paciente: {e}")
            return []
        finally:
            cursor.close()
