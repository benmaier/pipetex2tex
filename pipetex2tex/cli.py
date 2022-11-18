import sys
import argparse
from pipetex2tex import convert

def main():
    parser = argparse.ArgumentParser(description='Convert \input{|command} to the output of command.')
    parser.add_argument('filename', type=str, nargs='?',
                        help='Files to convert',default=None)
    parser.add_argument('-e','--enc',
                        default='utf8',
                        help='encoding')

    args = parser.parse_args()

    # if no positional argument was given, read in the piped input
    if args.filename is None:
        s = sys.stdin.read()
    else:
        with open(args.filename,'r',encoding=args.enc) as f:
            s = f.read()

    converted = convert(s)

    sys.stdout.write(converted)

if __name__=="__main__":
    main()

