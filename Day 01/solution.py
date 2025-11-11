"""Spent actual hours on part 2 wondering why
duplicate left list values weren't being processed.
But there are none!!"""

from typing import Deque

def main():
    with open("input.txt") as f:
        pairs = [[int(char) for char in line.split()] for line in f.read().splitlines()]

    left_list = []
    right_list = []
    for pair in pairs:
        left_list.append(pair[0])
        right_list.append((pair[1]))
    
    left_list.sort()
    right_list.sort()
    
    solution_1(left_list, right_list)
    solution_2(left_list, right_list)

def solution_1(left_list_par, right_list_par):
    difference = 0
    for i in range(len(left_list_par)):
        difference += abs(left_list_par[i]-right_list_par[i])

    print(f"Solution 1: {difference}")

def solution_2(left_list_par, right_list_par):
    processed_ids = {}
    similarity_score = 0
    right_list_deque = Deque(right_list_par)

    for left_id in left_list_par:
        if left_id in processed_ids:
            similarity_score += left_id * processed_ids[left_id]
            continue

        if len(right_list_deque) == 0:
            break

        local_similarity = 0
        while len(right_list_deque) > 0:
            if left_id < right_list_deque[0]:
                break
            else:
                if left_id == right_list_deque[0]:
                    local_similarity += 1
                right_list_deque.popleft()

        processed_ids[left_id] = local_similarity
        similarity_score += left_id * local_similarity
    
    print(f"Solution 2: {similarity_score}")

if __name__ == "__main__":
    main()