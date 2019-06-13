from pathlib import Path


def preprocess(f):
    newlines = []
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        if line.count('=') >= 2:
            continue
        newlines.append(line)
    return newlines


def main():
    path = Path('./')

    with open(path / 'train.raw.txt') as f:
        lines = preprocess(f)
    with open(path / 'train.txt', 'w') as f:
        f.write('\n'.join(lines))

    with open(path / 'valid.raw.txt') as f:
        lines = preprocess(f)
    with open(path / 'valid.txt', 'w') as f:
        f.write('\n'.join(lines))

    with open(path / 'test.raw.txt') as f:
        lines = preprocess(f)
    with open(path / 'test.txt', 'w') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    main()
