#!/usr/local/bin/python3


class tyfile:
    def __init__(self, file_name, *args, **kwargs):
        self.file = open(file_name, *args, **kwargs)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    def __iter__(self):
        return iter(self.file)

    def writeln(self, string=""):
        self.file.write(string)
        self.file.write("\n")
