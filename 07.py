class File():
    name: str
    size: int = 0

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Dir(File):
    files: list[File]
    parent_dir = None

    def __init__(self, name, parent_dir):
        super().__init__(name, 0)
        self.parent_dir = parent_dir
        self.files = []

    def dir_size(self) -> int:
        total = 0
        for f in self.files:
            if type(f) == File:
                total += f.size
            if type(f) == Dir:
                total += f.dir_size()
        return total


class FileSystem:
    root: Dir
    _cur_dir: Dir

    def __init__(self):
        self.root = Dir('', parent_dir=None)
        self._cur_dir = self.root
        self.mkdir('/')

    def add_file(self, name: str, size: int):
        self._cur_dir.files.append(File(name=name, size=size))

    def mkdir(self, dir_name: str):
        self._cur_dir.files.append(Dir(name=dir_name, parent_dir=self._cur_dir))

    def chdir(self, name: str):
        if name == '..':
            self._cur_dir = self._cur_dir.parent_dir
            return
        assert name in [n.name for n in self._cur_dir.files]
        for item in self._cur_dir.files:
            if type(item) == Dir and item.name == name:
                self._cur_dir = item
                break


class Part1:
    result: int
    fs: FileSystem()
    dir_list: list[int]

    def __init__(self, file: str):
        self.result = 0
        self.fs = FileSystem()
        self.dir_list = []
        with open(f'{file}', mode='r', encoding='utf-8') as f:
            line = f.readline().rstrip()
            while len(line) > 0:
                if not line.startswith('$'):
                    raise Exception('expecting a line starting with $')
                cmd = line.lstrip('$ ')
                if cmd.startswith('cd'):
                    dir_name = cmd.removeprefix('cd ')
                    self.fs.chdir(dir_name)
                    line = f.readline().rstrip()
                    continue
                if cmd.startswith('ls'):
                    # Read next lines until a new '$'
                    line = f.readline().rstrip()
                    while not line.startswith('$') and len(line) > 0:
                        if line.startswith('dir'):
                            self.fs.mkdir(line.removeprefix('dir '))
                        else:
                            size, name = line.split(' ')[0], line.split(' ')[1]
                            self.fs.add_file(name, int(size))
                        line = f.readline().rstrip()

    def compute(self):
        self._fill_dir_list_size(self.fs.root)
        for dir_size in self.dir_list:
            if dir_size < 100000:
                self.result += dir_size

    def _fill_dir_list_size(self, d: Dir):
        for item in d.files:
            if type(item) == Dir:
                self.dir_list.append(item.dir_size())
                self._fill_dir_list_size(item)


class Part2(Part1):
    def compute(self):
        needed_space = 30000000 - (70000000 - self.fs.root.dir_size())
        self._fill_dir_list_size(self.fs.root)
        self.dir_list.sort()
        for dir_size in self.dir_list:
            if dir_size >= needed_space:
                self.result = dir_size
                break


if __name__ == '__main__':
    for input_dir in ['test-files', 'input-files']:
        part_1 = Part1(f'{input_dir}/07.txt')
        part_1.compute()
        if input_dir == 'test-files':
            assert part_1.result == 95437
        else:
            print(part_1.result)

        part_2 = Part2(f'{input_dir}/07.txt')
        part_2.compute()
        if input_dir == 'test-files':
            assert part_2.result == 24933642
        else:
            print(part_2.result)
