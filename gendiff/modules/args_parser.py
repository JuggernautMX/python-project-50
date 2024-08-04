import argparse
import pathlib


def args_parser():
    parser = argparse.ArgumentParser(description='Generate diff',
                                     conflict_handler='resolve')
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument('-f', '--format',
                        help='set format of output (default: stylush)',
                        default='stylish',
                        metavar='FORMAT',
                        choices=['stylish', 'plain', 'json'])

    args = parser.parse_args()
    return args
