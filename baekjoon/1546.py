N = int(input())
score_list = list(map(int,input().split()))
max_score = max(score_list)

new_score = []
for i in score_list:
    new_score.append(i/max_score*100)
print(sum(new_score, 0.0)/N)