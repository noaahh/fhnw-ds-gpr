class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

        self.files = []
        self.directories = []

    def total_size(self):
        size_sum = 0
        for f in self.files:
            size_sum += f.size

        for d in self.directories:
            size_sum += d.total_size()

        return size_sum

    def ls(self, level=0):
        print("\t" * level + f"- {self.name} (dir, size={self.total_size()})")

        for f in self.files:
            print("\t" * (level + 1) + f"- {f.name} (file, size={f.size})")

        for d in self.directories:
            d.ls(level=level + 1)

    def get_flat_sub_dirs(self):
        dirs = [self]
        for d in self.directories:
            dirs.extend(d.get_flat_sub_dirs())

        return dirs

class FileSystem:
    def __init__(self):
        self.root = Directory(name="/")


with open('input.txt') as f:
    cd = Directory("/", None)
    root = cd

    for line in f:
        line = line.rstrip()

        if line.startswith("$"):
            command = line[2:4]

            if command == "ls":
                continue

            if command == "cd":
                target = line[5:]

                if target == "..":
                    cd = cd.parent
                    continue

                if target == "/":
                    cd = root
                    continue

                for d in cd.directories:
                    if d.name == target:
                        cd = d
                        break

        else:
            if line.startswith("dir"):
                dir_name = line[4:]
                cd.directories.append(Directory(name=dir_name, parent=cd))

            elif line[0].isdigit():
                size = line.split(" ")[0]
                file = File(name=line[len(size) + 1:], size=int(size))
                cd.files.append(file)

    print(sum([d.total_size() for d in root.get_flat_sub_dirs() if d.total_size() <= 100000]))