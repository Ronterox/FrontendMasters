from sys import argv
import re


def main(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        lines.sort(key=lambda x: float(re.search(r'(\d+\.\d+)', x)[1]))
        with open('sorted.log', 'w') as f:
            f.writelines(lines)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python sortit.py <output.log>")
        exit(1)

    main(argv[1])
