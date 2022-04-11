import os

if __name__ == "__main__":
    modified = 0
    for file in os.listdir():
        if os.path.isfile(file) and os.path.splitext(file)[1] != ".py":

            changed = False
            with open(file, "r+") as f:
                lines = f.readlines()

                if lines[7][:-1] != "Selection":
                    lines.insert(7, "Selection\n")
                    changed = True

                for i, line in enumerate(lines):
                    if 9 <= i <= 56 and line[-7:-1] != " F F F":
                        lines[i] = line[:-1] + " F F F\n"
                        changed = True
                    elif 57 <= i <= 58 and line[-7:-1] != " T T T":
                        lines[i] = line[:-1] + " T T T\n"
                        changed = True

                if changed:
                    f.seek(0)
                    for l in lines:
                        f.write(l)
                    modified += 1

    print("{} file(s) modified".format(modified))