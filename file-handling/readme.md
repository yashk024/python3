# File Handling

## Opening the streams

* `stream = open(file, mode = 'r', encoding = None)`
* modes
    * `r`, `w`, `a`, `r+`, `w+`
    *   | Text mode (default) | Binary Mode |
        | --- | --- |
        | `rt` | `rb` |
        | `wt` | `wb` |
        | `at` | `ab` |
        | `r+t` | `r+b` |
        | `w+t` | `w+b` |
    * `x` mode, creates new file

## Opening the stream for the first time

```py
try:
    stream = open("C:\\Users\\User\\Desktop\\file.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)
```

## Pre-opened streams

* Three predefined streams are already open when the program starts
* `import sys`
    * `sys.stdin`
    * `sys.stdout`
    * `sys.stderr`

## Closing a stream

* `stream.close()`
    * raise `IOError`
    * returns `None`
    * takes no argument

## Working with real files

* `read()` method
* `readline()` method
* `readlines()` method
* `write()` method

## What is a bytearray?

* amorphous data
* `bytearray` class
* writing bytearray to a binary file
    * `write()` method
* reading from binary file 
    * `readinto()` method