#!/usr/bin/env python3

from gendiff.modules.args_parser import args_parser
from gendiff.modules.generate_difference import generate_diff


def main():
    args = args_parser()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
