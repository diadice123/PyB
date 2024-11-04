## 1. 개발환경 구축

### 1-1. 다운로드
- anaconda
- vscode

### 1-2. 아나콘다 환경세팅
- *실행하면 (base) 가상환경 자동 접속 됨
- conda env list                    (가상환경 목록 확인)
- conda create -n dev python=3.11   (가상환경 생성)
- conda activate dev                (가상환경 접속)
- pip list                          (설치 된 라이브러리 목록 확인)
- pip install [라이브러리]           (설치 된 라이브러리 목록 확인)
- cls

### 1-3. VSCODE 세팅
1. extensions 설치
    - python
    - prettier
    - python extension pack
    - Atom Material Icons
    - Atom Material Theme
2. Settings
    - [Mouse Wheel Zoom] 켜기
    - 
### 1-4. 명령어 단축키
- [ctrl] + [`] : 터미널 켜기
- [ctrl] + [,] : Settings 켜기
- [ctrl] + [/] : 주석 ( 1 Line ) 토글, 블록 (+ 여러줄 가능 )
- [ctrl] + [F11] : 파이썬 코드 실행 ( 터미널 )

1. 기본 터미널 세팅
2. 터미널 폰트 사이즈 수정
3. python run 단축키 설정

## 2. 데이터 베이스
    - 데이터를 효율적으로 저장하고 관리할 수 있는 프로그램(DBMS)
### 2-1. DBMS(데이터베이스 관리 시스템)
    - 관계형 데이터베이스(RDB): 표 형태, 보안이 중요하거나, 영속성 데이터
    (개인정보, 금융정보,)
        → MariaDB, Oracle, MySQL, PostgreSQL
    - NoSQL: 자유 형태, 대용량 수집 데이터
        → MongoDB

## 99. 전체 시스템 구조(학습용) - WEB/APP
#  - Client - Sever
#  *Client(고객: 웹 브라우저)
#  *Server(회사: 서비스를 동작하는 컴퓨터)
# Client(naver.com) -> Server(naver) -> Client(소스코드, 이미지, 정보 전달) -> Client(랜더링)

# 구조
# Client -> 네트워크 -> 클라우드 컴퓨팅(ex: AWS)
#                           ㄴ[Server(Linux : 운영체제)]
#                               ㄴ 도커 컨테이너
#                                   ㄴ 데이터 베이스(RDB, NoSQL) + SQL
#                                   ㄴ 프론트엔드(HTML, CSS, JS, React.js, Vue.js)
#                                   ㄴ 백엔드(Spring, FastAPI, Django, Express)
#                                   ㄴ NginX
# + 프로그래밍 언어
# + 디자인 패턴
# + 자료 구조
# + Github(버전 관리 도구)


#                      Server(Linux : 운영체제)
#                         +
#                      Database(데이터 베이스)
#