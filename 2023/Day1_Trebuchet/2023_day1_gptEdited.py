import os
import re

current_directory = os.getcwd()
input_file_path = os.path.join(current_directory, "input.txt")

def process_line(line):
    # Part 1
    numberList = ['0','1','2','3','4','5','6','7','8','9']
    textNumList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = re.findall(r'\d', line)
    partial_answer1 = digits[0] if digits else '0'
    partial_answer2 = line.rstrip('abcdefghijklmnopqrstuvwxyz')[-1]
    answer1 = int(partial_answer1 + partial_answer2)

    # Part 2
    partial_answer1, partial_answer2 = '', ''
    for index in range(10):
        match = re.search(fr'\b{textNumList[index]}\b', line)
        if match:
            if not partial_answer1 or match.start() < line.find(partial_answer1):
                partial_answer1 = numberList[index]
            if not partial_answer2 or match.start() > line.find(partial_answer2):
                partial_answer2 = numberList[index]

    answer2 = int(partial_answer1 + partial_answer2)
    return answer1, answer2

answer1_total, answer2_total = 0, 0

with open(input_file_path, "r") as f:
    for i, line in enumerate(f, start=1):
        line = line.strip()
        answer1, answer2 = process_line(line)
        print(answer1, answer2, f"Line #{i}")
        answer1_total += answer1
        answer2_total += answer2

print("Part 1 Answer:", answer1_total)
print("Part 2 Answer:", answer2_total)
