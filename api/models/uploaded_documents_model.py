
from .database import get_db_connection

def insert_uploaded_document(stock_id, file_name, openai_file_id, uploaded_at):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO uploaded_documents (stock_id, file_name, openai_file_id, uploaded_at) VALUES (?, ?, ?, ?)",
        (stock_id, file_name, openai_file_id, uploaded_at)
    )
    conn.commit()
    conn.close()

def delete_uploaded_document(document_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM uploaded_documents WHERE id = ?", (document_id,))
    conn.commit()
    conn.close()