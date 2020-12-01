f = open('day1/input.txt')
numbers = []
for line in f.readlines():
    num = int(line)
    numbers.append(num)


def part1(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) == 2020:
                print(numbers[i] * numbers[j])


def part2(numbers):
    for i in range(len(numbers) - 2):
        for j in range(i + 1, len(numbers) - 1):
            for k in range(j + 1, len(numbers)):
                if (numbers[i] + numbers[j] + numbers[k]) == 2020:
                    print(numbers[i] * numbers[j] * + numbers[k])


part1(numbers)
part2(numbers)
