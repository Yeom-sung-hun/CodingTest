N, K = map(int, input().split())

"""
f(n, k) = n, k일 때 마지막에 남는 사람의 번호
번호를 1-idx로 붙였을 때 다음과 같은 점화식을 얻을 수 있다.
f(1, k) = 1
f(n, k) = ((f(n-1, k) + k-1) % n) + 1

번호를 0-idx로 붙이면 점화식이 조금 더 간결해진다.
f(1, k) = 0;
f(n, k) = ((f(n-1, k) + k) % n)


f(n, k)에서 첫 번째 사람이 죽은 뒤, n-1명이 남는다.
따라서 f(n-1, k)를 호출하면 마지막에 죽는 사람(idx)이 누구인지 알 수 있다.

f(n, k) 기준의 idx가 필요하니, 현재 k번째를 죽이고 난 뒤를 기준으로 삼는다. (k + idx) % n을 취해줘야 한다.   (0-idx 기준으로)

현재 죽어야 할 사람은 k-1, 따라서 f(n-1, k)의 idx 0의 기준은 k-1의 다음인 k가 된다. 따라서 마지막에 죽는 사람은 (k + idx) % n이다.
"""

idx = 0
for i in range(1, N+1):
    idx = (idx+K) % i
    # print(f'마지막: {idx+1}   인원: {i}')

print(idx + 1)