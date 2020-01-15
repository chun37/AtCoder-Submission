subjects, max_score, av_score = map(int, input().split())
result_scores = [int(i) for i in input().split()]

answer = -1

for i in range(max_score + 1):
    if (sum(result_scores) + i) / subjects >= av_score:
        answer = i
        break

print(answer)