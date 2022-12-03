def get_elves_calories(input_file: str, *, sort_by_order=True) -> list:
    elves_calories = []

    with open(input_file) as f:
        current_elf_calories = 0

        for line in f:
            if line == f'\n':
                elves_calories.append(int(current_elf_calories))
                current_elf_calories = 0
            else:
                current_elf_calories += int(line)

    if sort_by_order:
        elves_calories.sort(reverse=True)

    return elves_calories


if __name__ == '__main__':
    sorted_elves_calories = get_elves_calories('input.txt')
    print(f"Part 1:\n\tThe Elf with most calories has {sorted_elves_calories[0]} calories")
    print(f"Part 2:\n\tTop 3 Elves are carrying a total of {sum(sorted_elves_calories[:3])} calories")