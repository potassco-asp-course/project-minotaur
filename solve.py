# Usage  python3 solve.py file.lp SAT/OPT
# Will run clingo 0 file.lp exXY.lp for all ex.lp in the instances folder
# and store the result in solution/exXY.json
import sys
from subprocess import run, PIPE
import os
import tempfile
import logging
import json
import time

CLINGO = "/home/npoi/miniconda3/bin/clingo"
INSTANCES = "instances/"
REF_ENC = "checker.lp"
DUMMY = "dummy.lp"
SOLUS = "925"
MAX_MEM = 2048
SOLUTIONS = "solutions/"


def call_clingo(input_names, expected):
    if expected == "SAT":
        cmd = [CLINGO, "--warn=no-atom-undefined", "--warn=no-file-included", "--warn=no-operation-undefined", "--warn=no-variable-unbounded", "--warn=no-global-variable", "--outf=2"] + input_names
    else:
        cmd = [CLINGO, "--warn=no-atom-undefined", "--warn=no-file-included", "--warn=no-operation-undefined", "--warn=no-variable-unbounded", "--warn=no-global-variable", "--outf=2", "--opt-mode=optN", "--quiet=1"] + input_names
    output = run(cmd, stdout=PIPE, stderr=PIPE)
    if output.stderr:
        raise RuntimeError("Clingo: %s" % output.stderr)
    return output.stdout

def solve_and_store(enc, inst, expected):
    try:
        stdout = call_clingo([enc, INSTANCES+inst, SOLUS], expected)
        output = json.loads(stdout)
        inst_sol = inst[:-2]+"json"
        with open(SOLUTIONS+inst_sol, "w") as outfile:
            json.dump(output, outfile, indent = 1)
    except RuntimeError as e:
        logging.debug(str(e))
        raise e

def main():
    # check input
    if len(sys.argv) < 2:
        raise RuntimeError("not enough arguments (%d instead of 2)" % (len(sys.argv) - 1))
    enc = sys.argv[1]
    expected = sys.argv[2]
    if not os.path.isfile(enc):
        raise IOError("file %s not found!" % enc)

    dir = os.listdir(INSTANCES)
    dir.sort()

    for inst in dir:
         solve_and_store(enc, inst)
    return True


if __name__ == '__main__':
    try:
        message = "success" if main() else "failure"
        sys.stdout.write("%s\n" % message)
    except Exception as e:
        sys.stderr.write("ERROR: %s\n" % str(e))
        exit(1)
