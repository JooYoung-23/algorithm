'''
	카카오 기출
	1회 20240614
	2회
	3회

	아이디어
		1. 완전 탐색
		2. 반복되는 문자열 s가 있을 때, (s * n)으로 표현되는 문자를 ns로 표현한다. 이 때, 1은 생략한다.
    3. 투포인터로 문자열이 반복되는지 확인한다.
'''

def solution(s):
	answer = len(s)

	length = len(s)
	for step in range(1, length // 2 + 1):
		compressed = ""
		prev = s[0:step]
		count = 1
		for j in range(step, length, step):
			if prev == s[j:j + step]:
				count += 1
			else:
				compressed += str(count) + prev if count > 1 else prev
				prev = s[j:j + step]
				count = 1
		compressed += str(count) + prev if count > 1 else prev
		answer = min(answer, len(compressed))
	return answer

s = "ababbcbc"
print(solution(s))
