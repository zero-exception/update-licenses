import re
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", type=str, required=True)
parser.add_argument("-r", "--replacement", type=str, required=True)
args = parser.parse_args()

exp = re.compile(rf"{args.target}", re.MULTILINE)
paths = ["LICENSE", *glob.glob(r"**/*.py", recursive=True)]

for path in paths:
    if "fix_license" in path:
        continue

    with open(path, mode="r+", encoding="utf-8") as fp:
        text = fp.read()
        new_text = re.sub(exp, args.replacement, text)
        fp.truncate(0)
        fp.seek(0)

        fp.write(new_text)
