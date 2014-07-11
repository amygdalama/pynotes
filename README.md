A note-taking app.

# Usage

## Add notes

    $ python pynotes.py add
    Enter the name of your note:
    > test
    Enter your contents, enter "STOP" to complete your note:
    > first line
    > second line
    > STOP
    Saved test.

## Read notes

Read a note:

    $ python pynotes.py read test
    first line
    second line

Display notes and choose one to read:

    $ python pynotes.py read
    Available notes:
    test
    test1
    test2
    Which note would you like to read?
    > test
    first line
    second line

## Update notes

TODO

## Delete notes

Delete a note:

    $ python pynotes.py delete test
    Deleted notes/test.txt

Display notes and choose one to delete:

    $ python pynotes.py delete
    Available notes:
    test
    test1
    test2
    Which note would you like to delete?
    > test
    Deleted test.