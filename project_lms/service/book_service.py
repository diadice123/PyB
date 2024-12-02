# 프론트엔드 - Contorller - Service - DAO - DB
# Streamlit - main.py - service - DB

# 서비스층 : 실제 비지니스로직의 기능을 담당 
from common.connection import connection
import pandas as pd

# 도서목록 조회(ALL)
def get_books():
    conn = connection()
    try:
        curs = conn.cursor()
        sql = """
            SELECT * FROM tbl_book;
        """
        curs.execute(sql)          # 실행문
        rows = curs.fetchall()     # 실행결과 받기
        rows = pd.DataFrame(rows)  # Python의 DataFrame형태로 변환
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close
    return rows
# 도서검색
def search_books(keyword: str):
    pass

# 도서 등록
def insert_book(book: dict):
    pass

# 도서 수정
def update_book(book: dict):
    pass

# 도서 삭제
def delete_book(book_isbn: dict):
    pass