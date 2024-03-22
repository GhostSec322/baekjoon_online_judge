#교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
student =[i+1 for i in range(30)]

submit_student=[]
#입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다
for i in range(28):
    submit_student.append(int(input()))
# 중복되지 않는 출석번호 찾기
unique_students =sorted(list(set(student) - set(submit_student)))
print("\n".join(map(str,unique_students)))