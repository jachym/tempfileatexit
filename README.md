# tempfileatexit

Python library for removing temporary files and directories when program finishes.

## Installation
```
pip install tempfileatexit
```

## Usage


```
import tempfileatexit
import tempfile

(fs, my_tempfile) = tempfile.mkstemp()
my_tempdir = tempfile.mkdtemp()

tempfileatexit.register(my_tempfile)
tempfileatexit.register(my_tempdir)


print(tempfileatexit.list(verbose=True))
```

After you run the code and the program exxists, the `my_tempfile` and
`my_tempdir` will be gone.
