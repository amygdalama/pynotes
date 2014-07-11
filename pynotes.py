import argparse
import os
import subprocess


def _get_next_line():
    while True:
        line = raw_input("> ")
        if line == 'STOP':
            raise StopIteration
        yield line


def _get_filename(title):
    return 'notes/%s.txt' % title


def add(title):
    filename = _get_filename(title)
    if os.path.isfile(filename):
        print "%s already exists." % title
    else:
        subprocess.call(['touch', filename])
        subprocess.call(['open', filename])


def read(title):
    content = open('notes/%s.txt' % title, 'r').read()
    print read_note(title)
    return content


def update(title):
    pass


def delete(title):
    os.remove('notes/%s.txt' % title)


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