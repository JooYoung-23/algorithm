n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
	length = 0
	mid = (start + end) // 2
	for x in array:
		if x > mid:
			length += x - mid
	if length < m:
		end = mid - 1
	else:
		start = mid + 1
		result = mid

print(result)
