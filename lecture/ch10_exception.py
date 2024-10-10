# 예외(Exception)
#   - 프로그램을 개발하면서 예상하지 못한 상황
#     ex) 사용자 입력 오류 (숫자만 입력 → 문자 입력)
#   - 예외가 발생 하게되면 서비스 중인 어플리케이션이 종료
#    → "예외처리"를 하면 예외가 발생해도 종료되지 않음
#   - 예외처리는 강제성이 없음
#    → 파일 시스템, 데이터베이스 반드시 예외처리

#   - 사용자에게 입력 받는 부분에서 많이 발생 → 예외
#    → 유효성 체크 (사용자가 올바른 값을 입력하도록 도와주고 체크)

# ** 예외 종류
#  1. 예측 가능한 예외
#   - 발생 여부를 개발자가 사전에 인지 → 예외 처리
#   전화번호 : 01012341234
#   알림: (-없이) 입력해주세요. → 010-1234-5678
#                             → 010-1234-5678ㄷㄷㄷ

#  2. 예측이 불가능한 예외
#   - 쳔재지변과 같은 경우
#    ex) 화재로 인한 카카오톡 서버 종료 → 카카오톡 서비스 X

# 예외 기본 문법
"""
try:
    예외가 발생할 수 있는 코드
except 예외타입:
    예외처리
else:   ← 잘안씀
    예외가 발생하지 않은 경우 실행되는 코드
finally:
    무족건 실행되는 코드
    ex) 자원해제
    
    데이터 베이스 ( 데이터를 저장하는 프로그램)
        ㄴ 저장, 수정, 삭제, 조회, 검색, etc..
        ㄴ 1번에 접속해서 사용할 수 있는 인원 제한
"""
from urllib.request import urlopen, HTTPError
# 예외가 발생할 수 있는 상황 무궁무진하게 많음
#   except HTTPError → 예외 중 HTTP 관련된 예외만 처리
#   except HTTPError, ...
#   except : → 모든 예외상황을 처리하세요!


try:
    html = urlopen("https://www.naver.commmm")
except:
    print("올바른 URL을 입력해주세요")
else:
    print("No Error")
finally:
    print("자원해제")