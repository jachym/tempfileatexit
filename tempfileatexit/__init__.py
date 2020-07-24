import atexit
import collections
import time
import os
import shutil
import tempfile

__FILES__ = []

def remove():
    """Remove all registered files and directories
    """
    global __FILES__

    for f in __FILES__:
        try:
            if os.path.isfile(f):
                os.remove(f)
            elif os.path.isdir(f):
                shutil.rmtree(f)
        except Exception as myexcp:
            print("Could not remove file object [{}]".format(f))
            raise

atexit.register(remove)


def register(fobj):
    """Register new file or directory
    """
    global __FILES__
    if os.path.isfile(fobj) or\
      os.path.isdir(fobj):
        __FILES__.append(fobj)
    else:
        raise TempFileAtExitException("Object [{}] does not seem to be file or directory")


def list(verbose=False):
    """List registered objects
    """
    if not verbose:
        return __FILES__
    else:
        data = collections.OrderedDict()
        for f in __FILES__:
            data[f] = dict(
                    zip(
                        ["ino", "dev", "nlink", "uid", "gid", "size",
                        "atime", "mtime", "ctime"],
                        os.stat(f)
                        )
                    )
            if os.path.isfile(f):
                data[f]["type"] = "file"
            elif os.path.isfile(f):
                data[f]["type"] = "dir"

        return data

def mkdtemp(*args, **kwargs):
    """Call tempfile.mkdtemp and register it to be removed at exit
    """
    new_dir = tempfile.mkdtemp(*args, **kwargs)
    register(new_dir)
    return new_dir

def mkstemp(*args, **kwargs):
    """Call tempfile.mkstemp and register it to be removed at exit
    """
    (fd, name) = tempfile.mkstemp(*args, **kwargs)
    register(name)
    return (fd, name)

class TempFileAtExitException(Exception):
    pass
