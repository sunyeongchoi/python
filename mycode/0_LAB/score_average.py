# 2차원 배열
# 학생별 과목의 평균을 계산
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

# 학생별 과목의 합계를 저장할 리스트
# 중첩된 for 루프 안에서 학생별 과목 점수 합계를 저장한다.
student_score = [0, 0, 0, 0, 0]

# 학생을 구분하기 위한 인덱스
idx = 0 # 이부분 중요!!!
for subject in midterm_score:
    for student in subject:
        print(student)
        student_score[idx] += student
        idx += 1 # 이부분 중요!!!
    print('-------')
    idx = 0 # 이부분 중요!!!
else :
    print(student_score)
    # 학생별 점수를 unpacking
    a, b, c, d, e, = student_score
    student_average = [int(a/3), int(b/3), int(c/3), int(d/3), int(e/3)]
    print(student_average)





