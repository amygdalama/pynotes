import argparse


def _get_next_line():
    while True:
        line = raw_input("> ")
        if line == 'STOP':
            raise StopIteration
        yield line


def add(title):
    lines = _get_next_line()
    for line in lines:
        print line


def read(title):
    pass


def update(title):
    pass


def delete(title):
    pass


if __name__ == '__main__':
    commands = {
        'add' : add,
        'read' : read,
        'update' : update,
        'delete' : delete
    }
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=commands)
    parser.add_argument('title')
    args = parser.parse_args()
    commands[args.command](args.title)