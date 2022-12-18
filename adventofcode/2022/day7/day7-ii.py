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
        dirs = [x for d in self.directories for x in d.get_flat_sub_dirs()]
        dirs.append(self)

        return dirs

with open('input.txt') as f:
    cd = Directory("/", None)
    root = cd

    for line in f:
        line = line.rstrip()

        if line.startswith("$ cd"):
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

    deletion_size = root.total_size() - 70000000 + 30000000
    print(list(sorted(d.total_size() for d in root.get_flat_sub_dirs() if d.total_size() >= deletion_size))[0])
