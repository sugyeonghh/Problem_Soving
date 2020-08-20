T = int(input())
quiz = []
score_list = []
for i in range(T):
    quiz.append(input())

for i in quiz:
    count = 0
    score = 0
    for j in i:
        if j=='O':
            count += 1
            score += count
        else:
            count = 0
    score_list.append(score)

for i in score_list:
    print(i)