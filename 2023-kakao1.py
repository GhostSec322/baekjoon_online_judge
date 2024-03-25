def solution(today,terms, privacies):
    answer = []
    
    # 오늘 날짜 문자열
    today_str = today  # 주어진 문제에서 오늘 날짜로 고정
    
    # 오늘 날짜를 연, 월, 일로 분리
    today_year, today_month, today_day = map(int, today_str.split('.'))
    
    # 약관별 유효기간 딕셔너리 생성
    term_dict = {}
    for term in terms:
        name, duration = term.split()
        term_dict[name] = int(duration)
    
    # 개인정보 처리
    for idx, privacy in enumerate(privacies):
        date_str, term_name = privacy.split()
        info_year, info_month, info_day = map(int, date_str.split('.'))
        
        # 유효기간 계산
        expiration_year = info_year
        expiration_month = info_month + term_dict[term_name]
        if expiration_month > 12:
            expiration_year += 1
            expiration_month -= 12
        
        # 오늘보다 유효기간이 지난 경우 answer에 추가
        if today_year > expiration_year or \
           (today_year == expiration_year and today_month > expiration_month) or \
           (today_year == expiration_year and today_month == expiration_month and today_day > info_day):
            answer.append(idx + 1)
    
    return answer

# 예시 입력
print(solution('2022.05.19',["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
