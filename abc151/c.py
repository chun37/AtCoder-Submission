all_question, submission_count = map(int, input().split())
results = {}
for _ in range(submission_count):
    question_num, res = input().split()
    if question_num not in results:
        results[question_num] = []
    results[question_num].append(res)


def get_index(l, x):
    if x in l:
        return l.index(x)
    else:
        return -1

clear_count = penalty_count = 0

for questuin_num, res_list in results.items():
    index = get_index(res_list, "AC")
    if index == -1:
        continue
    penalty_count += index
    clear_count += 1

print(clear_count, penalty_count)