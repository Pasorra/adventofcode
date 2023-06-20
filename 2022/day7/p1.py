with open(r"2022\day7\input.txt", "r") as file:
    lines = [line.strip() for line in file]


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, parent, depth) -> None:
        self.name: str = name
        self.parent: Directory = parent
        self.dirs: list = []
        self.files: list = []
        self.dir_size: int = 0
        self.depth: int = depth

    def evaluate(self):
        for file in self.files:
            self.dir_size += file.size
        for dir in self.dirs:
            self.dir_size += dir.dir_size


dir = Directory("/", None, 0)
all_dirs = [dir]

depth = 0
for line in lines[1:]:
    line_split = line.split()
    if line == "$ cd ..":
        depth -= 1
        dir = dir.parent
        continue
    if line.startswith("$ cd"):
        depth += 1
        new_dir = Directory(line_split[2], dir, depth)
        dir.dirs.append(new_dir)
        dir = new_dir
        all_dirs.append(new_dir)
        continue
    if line.startswith("$ ls"):
        continue
    if line.startswith("dir"):
        new_dir = Directory(line_split[1], dir, depth + 1)
        dir.dirs.append(new_dir)
        all_dirs.append(new_dir)
        continue
    else:
        new_file = File(line_split[1], int(line_split[0]))
        dir.files.append(new_file)
        continue

sorted_items = sorted(all_dirs,
                      key=lambda x: x.depth, reverse=True)

total = 0
for item in sorted_items:
    item.evaluate()
    if item.dir_size <= 100000:
        total += item.dir_size

print(total)
