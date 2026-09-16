from collections import deque

def main():
    with open("input.txt") as f:
        raw = f.read().split()
    
    solution1(raw)
    solution2(raw)


def solution1(input):
    stones = deque(input)
    print(len(blink(stones, 25)))


def solution2(input):
    print()


def blink(stones, iterations=1):
    # print(stones)

    post_blink_stones = deque()
    while stones:
        current_stone = int(stones.popleft())
        if current_stone == 0:
            post_blink_stones.append(1)
            continue
        if len(str(current_stone)) % 2 == 0:
            half = int(len(str(current_stone))/2)
            post_blink_stones.append(int(str(current_stone)[:half]))
            post_blink_stones.append(int(str(current_stone)[half:]))
            continue
        post_blink_stones.append(current_stone*2024)

    if iterations == 1:
        return post_blink_stones

    return blink(post_blink_stones, iterations-1)


if __name__ == "__main__":
    main()