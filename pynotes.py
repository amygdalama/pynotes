import argparse


def _get_next_line():
    while True:
        line = raw_input("> ")
        if line == 'STOP':
            raise StopIteration
        yield line


def add_note(title, content):
    with open('notes/%s.txt' % title, 'w') as f:
        f.write(content)


def add(title):
    user_input = _get_next_line()
    content = '\n'.join([line for line in user_input])
    add_note(title, content)


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