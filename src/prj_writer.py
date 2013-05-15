import sys
from srcfile import VerilogFile, VHDLFile, SVFile

class PrjWriter(object):
    def __init__(self):
        self._file = None

    def open(self, filename):
        if self._file:
            raise Exception("Please close prj-file before opening a new")
        self._file = open(filename, "w")

    def writeln(self, text=""):
        if self._file:
            self._file.write("%s\n" % text)

    def close(self):
        if self._file:
            self._file.close()
            self._file = None

    def generate_vhdl_prj(self, fileset):
        for vhdl in fileset.filter(VHDLFile):
            self.writeln("vhdl work %s" % vhdl.rel_path())

    def generate_vl_prj(self, fileset):
        vl_paths = [x.rel_path() for x in fileset.filter(VerilogFile)]
        self.writeln("verilog work %s" % ' '.join(vl_paths))
