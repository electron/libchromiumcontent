import argparse
import shutil


def parse_args():
  parser = argparse.ArgumentParser(description='Copy file')
  parser.add_argument('source')
  parser.add_argument('destination')
  return parser.parse_args()


def main():
  args = parse_args()
  shutil.copy2(args.source, args.destination)


if __name__ == '__main__':
  main()
