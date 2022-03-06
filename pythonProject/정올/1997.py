d,k = map(int,input().split())
# d 는 넘어온 날 3<=d<=30 // k 는 d날 준 떡의 개수 10<=k<=100,000

dp = [ [0,0] for _ in range(d)]

dp[0] = [1,0]
dp[1] = [0,1]

for i in range(2,d):
  dp[i][0] = dp[i-2][0] + dp[i-1][0]
  dp[i][1] = dp[i-2][1] + dp[i-1][1]

for i in range(1, k//2+1):
  if (k - dp[d-1][0]*i) % dp[d-1][1] == 0 :
    print(i)
    print((k - dp[d-1][0]*i) // dp[d-1][1])
    break