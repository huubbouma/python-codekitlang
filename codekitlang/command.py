# -*- coding: utf-8 -*-

import argparse
from . import compiler


def main():
    parser = argparse.ArgumentParser(description='CodeKit Language Compiler.')
    parser.add_argument('src', nargs=1, metavar='SOURCE')
    parser.add_argument('dest', nargs=1, metavar='DEST')
    parser.add_argument('--strip-basenames', action='store_true',
                        default=False, help="apply CodeKit's buggy behavior.")
    parser.add_argument('--framework-paths', '-f', action='append',
                        metavar='DIR')
    namespace = parser.parse_args()
    options = vars(namespace)
    src = options.pop('src')
    dest = options.pop('dest')
    compiler_ = compiler.Compiler(**options)
    compiler_.generate_to_file(dest[0], src[0])

if __name__ == '__main__':  # pragma:nocover
    main()
