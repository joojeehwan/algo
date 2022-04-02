

#
# S = input()
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# dic = {}
#
# for i in range(len(S)):
#     if S[i] not in dic.keys():
#         dic[S[i]] = i
#
# for alpha in alphabet:
#     if (alpha in S):
#         print(str(dic[alpha]), end=" ")
#
#     else:
#         print("-1", end=" ")


lst = ["a","a","a","a","a","a","b","b","b"]

dic = {}

for li in lst:
    if li in dic.keys():
        dic[li] += 1

    else:
        dic[li] = 1

print(dic)

