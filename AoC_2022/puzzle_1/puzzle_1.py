from utils.puzzle import Puzzle


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()

    elf_sums = []
    elf_cal = 0
    for cal in data:
        if cal != '':
            elf_cal += int(cal)
        else:
            elf_sums.append(elf_cal)
            elf_cal = 0
    elf_sums.append(elf_cal)

    elf_sums.sort()
    print(f"Max elf calories: {elf_sums[-1]}")
    print(f"Max 3 elf calories: {sum(elf_sums[-3:])}")
