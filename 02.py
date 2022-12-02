class RockPaperScissors:
    my_score = 0

    def play_1(self, lines: list[str]):
        for line in lines:
            elf_and_mine = line.rstrip().split(' ')
            elf = ord(elf_and_mine[0]) - ord('A') + 1
            mine = ord(elf_and_mine[1]) - ord('X') + 1
            outcome = self.compute_outcome(elf, mine)
            self.my_score += outcome + mine
        print(f'score = {self.my_score}')

    def play_2(self, lines: list[str]):
        for line in lines:
            elf_and_strategy = line.rstrip().split(' ')
            elf = ord(elf_and_strategy[0]) - ord('A') + 1
            mine = self.from_strategy_2(elf, elf_and_strategy[1])
            outcome = self.compute_outcome(elf, mine)
            self.my_score += outcome + mine
        print(f'score = {self.my_score}')

    @staticmethod
    def compute_outcome(elf, mine) -> int:
        outcome = 0
        if elf == mine:
            outcome = 3
        if mine == 2 and elf == 1 or \
                mine == 3 and elf == 2 or \
                mine == 1 and elf == 3:
            outcome = 6
        return outcome

    @staticmethod
    def from_strategy_2(elf, strategy) -> int:
        # Default is draw
        mine = elf
        if strategy == 'X':  # loose
            mine = elf - 1
            if elf == 1:
                mine = 3
        if strategy == 'Z':  # win
            mine = elf + 1
            if elf == 3:
                mine = 1
        return mine


if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        with open(f'{input_dir}/02.txt', mode='r', encoding='utf-8') as f:
            game = RockPaperScissors()

            game.play_1(f.readlines())
            if input_dir == 'test-files':
                assert game.my_score == 15

            game = RockPaperScissors()
            f.seek(0)
            game.play_2(f.readlines())
            if input_dir == 'test-files':
                assert game.my_score == 12

