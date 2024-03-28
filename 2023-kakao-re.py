
    # 1. today는 2022.05.19이다 이때 . 을 기준으로 다 나누고 모두 숫자형태 리스트로 저장[2022,5,19]
    # 2. 약관은 ABC형태로 키를 가지고 그에 맞는 값을 대입한다 (A는 6 B는 12 C는 3) : 딕셔너리 이용
    # 3. 개인정보를 처리 하기 위해 띄어 쓰기 기준으로 분리 한다 "2021.05.02 A" 여기서 날짜와 키를 분리하여 리스트로 저장한다 
    # 4. 그다음 각 조건에 맞게 키에 따라 더한다 여기서 B는 12개월 이므로 년도에 1을 더한다 
    # 5. 그리고 마지막으로 today년,월,일 을  비교하여 연도가 오느날보다 크거나 월과 일이 클경우 반환리스트에 저장한다. 
    # 6. 
def solution(today,terms,prvaces):
    terms = list(map(lambda x:x.split(" "), terms))
    for priv in prvaces:
        p_date,p_type = priv
        y,m,d =p_date.split(".")