# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex4.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))

자동차 = 100
차_안_공간 = 4.0
운전사 = 30

승객 = 90
운행_안하는_차 = 자동차 - 운전사
운행하는_차 = 운전사
총_정원 = 운행하는_차 * 차_안_공간
차당_평균_승객 = 승객 / 운행하는_차
