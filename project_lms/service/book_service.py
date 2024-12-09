# 프론트엔드 - Contorller - Service - DAO - DB
# Streamlit - main.py - service - DB

# 서비스층 : 실제 비지니스로직의 기능을 담당 

# MVC, MVT 패턴
#   → 시스템 개발시 사용하는 패턴

# 웹 브라우저 요청(request) : https://naver.com + 글쓰기
#           ↓
# 웹 서버(네이버 서버)
#   1. Controller : 요청을 받아서 해당 로직을 처리할 수 있는 Service로 전달하는 역할
#      → Cafe 관련 Service로 전달
#   2. Service : 실제 비즈니스 로직을 처리하는 곳
#      → Cafe 글쓰기 관련 함수로 처리 ex(def cafe_insert())
#      → def cafe_insert() 처리하는 도중에 DB가 필요한 경우 DAO로 전달
#   3. DAO(Data Access Object) : DB관련 로직을 처리
#      → CafeDAO를 사용해서 SQL(ex: INSERT INTO ~) 실행
#      → DB로부터 처리받은 결과를 Service로 전달
#   4. Service 
#      → DAO로부터 처리받은 결과를 Controller로 전달
#   5. Controller
#      → Service로부터 처리받은 결과를 웹 브라우저에게 전달(Response)

# 겨울방학 때 추천 코스
#   1. SQLD 자격증 취득
#     → 요즘은 ORM으로 개발하는데 SQL 필요한가?
#     → ORM을 할려고 해도 SQL을 이해하고 있어야 훨씬 좋음
#     → 복잡한 SQL구조는 ORM으로 구현 불가능(그떄는 SQL 직접 사용)
#   2. 웹 개발 공부
#     → 웹 개발 → 모든 IT의 정수
#     → Python 웹 프레임워크 : Django, Flask(비추), FastAPI
#     ※ Python 웹 개발자 취업? 매우 어렵, 점유율↓
#        1등: SprintBoot(JAVA)
#        2등: Node.js(JavaScript)
#        3등: Django(Python)
#     ※ 나는 졸업 전에 취업하고 싶다. SpringBoot 공부 추천(취업 매우 잘됨)
#     ※ HTML, CSS, JavaScript(기본) → 1달이면 충분히 가능
#     ※ 토이프로젝트, 사이트프로젝트, 펫 프로젝트
#       → 개인 웹 사이트
#

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
        # 전체 결과 → Dict → 2차원 데이터
        rows = curs.fetchall()     # 실행결과(전체) 받기
        # 2차원 Dict 데이터 → 표 형태로 변환
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
def search_book(keyword: str):
    conn = connection()
    try:
        curs = conn.cursor()
        sql = """
            SELECT * FROM tbl_book
            WHERE book_name LIKE %(keyword)s
            OR book_writer LIKE %(keyword)s
            OR book_publisher LIKE %(keyword)s;
        """
        curs.execute(sql, {'keyword': "%" + keyword + "%"})
        rows = curs.fetchall()
        rows = pd.DataFrame(rows)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
    return rows

# 도서 등록
def insert_book(book: dict):
    conn = connection()
    try:
        curs = conn.cursor()
        sql = """
            INSERT INTO tbl_book(book_name, book_writer, book_publisher, book_price)
            VALUE(%(book_name)s, %(book_writer)s, %(book_publisher)s, %(book_price)s);
        """
        curs.execute(sql, book)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()

# ※ UPDATE, DELETE는 WHERE절 필수 ★★★★

# 도서 수정
def update_book(book: dict):
    conn = connection()
    try:
        curs = conn.cursor()
        sql = """
            UPDATE tbl_book
            SET book_name = %(book_name)s,
                book_writer = %(book_writer)s,
                book_publisher = %(book_publisher)s,
                book_price = %(book_price)s,
                register_at = %(register_at)s,
                useyn = %(useyn)s
            WHERE book_ISBN = %(book_ISBN)s;
        """
        curs.execute(sql, book)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()

# 도서 삭제
def delete_book(book_isbn: dict):
    pass