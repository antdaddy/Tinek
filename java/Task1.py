def vadim_reverse(intervals):
    unique_numbers = set()

    for interval in intervals.split(','):
        if '-' in interval:
            start, end = map(int, interval.split('-'))
            for num in range(start, end + 1):
                unique_numbers.add(num)
        else
            unique_numbers.add(int(interval))

    return sorted(unique_numbers)

input_string = input("Введите интервалы: ").strip()
output_numbers = vadim_reverse(input_string)
print(' '.join(map(str, output_numbers)))