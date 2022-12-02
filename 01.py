if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        with open(f'{input_dir}/01.txt', mode='r', encoding='utf-8') as f:
            elf_idx = 0
            max_cal = 0
            max_cal_elf = 0
            calories = [0]
            for line in f:
                if line == '\n':
                    elf_idx += 1
                    calories.append(0)
                    continue
                calories[elf_idx] += int(line)
                if calories[elf_idx] > max_cal:
                    max_cal_elf = elf_idx
                    max_cal = calories[elf_idx]

            # Part 1
            if input_dir == 'test-files':
                assert max_cal == 24000
            print(f'max_cal[{max_cal_elf}] = {calories[max_cal_elf]}')

            # Part 2
            calories.sort(reverse=True)
            top_3 = 0
            for i in range(0, 3):
                top_3 += calories[i]
            if input_dir == 'test-files':
                assert top_3 == 45000

            print(f'top 3 = {top_3}')
