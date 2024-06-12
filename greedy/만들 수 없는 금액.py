'''
	1회 20240612
	2회
	3회

	아이디어
	1. 조합을 이용해 모든 경우의 수를 만든다. > 시간 복잡도 초과 O(n!)
	2. 정렬을 이용한 그리디, 핵심: "현재 상태는 항상 1부터 target-1을 만들 수 있는 상태"
		1. 화폐 단위 기준 오름차순 정렬한다.
		2. 1부터 차례로 특정 금액(target)을 만들 수 있는 지 확인한다.
			1. 현재 상태에서 확인하는 동전을 이용해 target을 만들 수 있는 지 확인한다.
			2. 현재 상태는 항상 1부터 target-1을 만들 수 있는 상태이다.
			3. Ex) target이 8이고, data가 [1, 1, 2, 3, 9]일 때,
				1, 2, 3, 4, 5, 6, 7 까지는 [1, 1, 2, 3]의 조합으로 만들 수 있는 상태임이 자명하다.
				이 때, 새로운 동전의 값이 i일 때, i + (1, 2, 3, 4, 5, 6, 7)을 만들 수 있음은 자명하다.
				따라서 target < i라면, (target + i - 1) 까지의 모든 수를 만들 수 있음을 증명할 수 있다.
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for i in data:
	if target < i:
		print(target)
		break
	target += i
