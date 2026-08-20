#!/usr/bin/env python

""" Convert one YAML file to JSON with yq (the Python yq, which defaults to JSON
output), reproducing the Makefile's `yq < input > output`. Invoked by the
generator processor as: yaml_to_json.py <input> <output>. """

import subprocess
import sys


def main():
    """ main entry point """
    source, target = sys.argv[1], sys.argv[2]
    with open(source, encoding="utf-8") as infile, \
            open(target, "w", encoding="utf-8") as outfile:
        sys.exit(subprocess.call(["yq"], stdin=infile, stdout=outfile))


if __name__ == "__main__":
    main()
