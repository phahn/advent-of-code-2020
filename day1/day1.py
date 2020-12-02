
def read_numbers(file):
    f = open(file)
    numbers = []
    for line in f.readlines():
        num = int(line)
        numbers.append(num)
    return numbers


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


numbers = read_numbers('day1/input.txt')
part1(numbers)
part2(numbers)
