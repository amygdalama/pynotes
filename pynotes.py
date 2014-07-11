import argparse
import glob
import os
import re
import subprocess


def _get_next_line():
    while True:
        line = raw_input("> ")
        if line == 'STOP':
            raise StopIteration
        yield line


def _get_filename(title):
    if title:
        return 'notes/%s.txt' % title
    else:
        raise ValueError("title must be more than one character")


def _title(title):
    if re.match(r'[a-zA-Z0-9]+\Z', title):
        return title
    else:
        raise ValueError("titles must be alphanumberic plus \
                dashes and underscores")


def _extract_title(filepath):
    match = re.match(r'notes/([a-zA-Z0-9_-]+).txt', filepath)
    if match:
        return match.group(1)


def _prompt_title(command):
    existing_notes = glob.glob("notes/*.txt")
    print "Current notes:"
    for note in existing_notes:
        print _extract_title(note)
    print "Enter the title of the note you wish to %s:" % command
    return raw_input("> ")


def add(title=None):
    if not title:
        title = _prompt_title('add')
    filename = _get_filename(title)
    if os.path.isfile(filename):
        print "%s already exists." % title
    else:
        subprocess.call(['touch', filename])
        subprocess.call(['open', filename])


def read(title=None):
    if not title:
        title = _prompt_title('read')
    content = open('notes/%s.txt' % title, 'r').read()
    print content


def edit(title=None):
    if not title:
        title = _prompt_title('edit')
    filename = _get_filename(title)
    if os.path.isfile(filename):
        subprocess.call(['open', filename])
    else:
        print "%s doesn't exist." % title


def delete(title=None):
    if not title:
        title = _prompt_title('delete')
    os.remove('notes/%s.txt' % title)


if __name__ == '__main__':
    commands = {
        'add' : add,
        'read' : read,
        'edit' : edit,
        'delete' : delete
    }
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=commands)
    parser.add_argument('title', nargs='?', type=_title)
    args = parser.parse_args()
    print args.title
    commands[args.command](args.title)