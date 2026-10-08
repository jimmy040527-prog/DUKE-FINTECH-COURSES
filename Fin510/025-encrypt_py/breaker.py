import sys

if len(sys.argv) != 2:
    print("Invalid number of arguments", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("file not found", file=sys.stderr)
    sys.exit(1)

# initialize the count
count = {}
for char in text:
    if char.isalpha():
        char = char.lower()
        count[char] = count.get(char, 0) + 1

if not count:
    print("No letters found", file=sys.stderr)
    sys.exit(1)
    
most_freq = max(count, key=count.get)
max_count = count[most_freq]

how_many = 0
for i in count.values():
    if i == max_count:
        how_many += 1

if how_many > 1:
    print("More than 1 letter has the highest frequency", file=sys.stderr)
    sys.exit(1)

key = (ord(most_freq) - ord('e')) % 26

print(key)


        
