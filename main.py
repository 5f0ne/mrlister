import argparse

from src.classes.StringSanitizer import StringSanitizer

parser = argparse.ArgumentParser()
parser.add_argument("--path", "-p", type=str, required=True, help="Path to Text File")
parser.add_argument("--result", "-r", type=str, default="list.txt", help="Name of the generated list")
parser.add_argument("--lower", "-l", type=bool, default=False, help="Set all words to lowercase")
parser.add_argument("--minlength", "-m", type=int, default=6, help="Number of min chars for words in the list")

args = parser.parse_args()

sanitizer = StringSanitizer()

pwList = open(args.path, 'r', encoding="utf8")

final = []

while True:
    textLine = pwList.readline().rstrip('\n')
    
    if not textLine:
        break

    parts = textLine.split(" ")
    
    for part in parts:
        if part not in final:
            if len(part) >= args.minlength:
                part = sanitizer.sanitize(part)
                if(args.lower):
                    part = part.lower()
                final.append(part)

f = open(args.result, "w", encoding="utf8")

for word in final:
    f.write(word + "\n")
    
f.close()
pwList.close()