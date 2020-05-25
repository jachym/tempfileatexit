import atexit
import collections
import time
import os
import shutil

__FILES__ = []

def remove():
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
    global __FILES__
    if os.path.isfile(fobj) or\
      os.path.isdir(fobj):
        __FILES__.append(fobj)
    else:
        raise TempFileAtExitException("Object [{}] does not seem to be file or directory")


def list(verbose=False):
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

class TempFileAtExitException(Exception):
    pass
