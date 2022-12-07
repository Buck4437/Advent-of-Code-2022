with open("input.txt") as f:
    s = "\n".join([line.strip() for line in f])
puz_in = s.split("\n")


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def list_all_directories(self):
        dirs = [self]
        for file in self.files:
            if isinstance(file, Directory):
                dirs.extend(file.list_all_directories())
        return dirs

    def calc_size(self):
        total = 0
        for file in self.files:
            if isinstance(file, Directory):
                total += file.calc_size()
            if isinstance(file, File):
                total += file.size
        return total

    def get_directory(self, name):
        for file in self.files:
            if isinstance(file, Directory):
                if file.name == name:
                    return file
        return None

    def has_file(self, name):
        for file in self.files:
            if file.name == name:
                return True
        return False


root = Directory("/")
stack = [root]

for line in puz_in:
    cur_dir = stack[-1]
    if "$ cd" in line:
        if ".." in line:
            stack.pop()
        elif "/" in line:
            stack = [root]
        else:
            name = line[5:]
            sub_dir = cur_dir.get_directory(name)
            if sub_dir is None:
                sub_dir = Directory(name)
                cur_dir.add_file(sub_dir)
            stack.append(sub_dir)
    elif "$ ls" in line or "dir" in line:
        continue
    else:
        size, name = line.split()
        if not cur_dir.has_file(name):
            cur_dir.add_file(File(name, int(size)))


print(sum([x.calc_size() for x in root.list_all_directories() if x.calc_size() <= 100000]))

cur_ext = 70000000 - root.calc_size()
needed = 30000000 - cur_ext
print(min([x.calc_size() for x in root.list_all_directories() if x.calc_size() >= needed]))
