from pathlib import Path

file_path = Path(__file__).parent / "answers.txt"

with open(file_path, "w") as f:
    f.write(bin(42) + "\n")
    f.write(hex(42) + "\n")
    f.write(oct(42) + "\n")
    f.write(str(int("0xC4", 16)) + "\n")
    f.write(str(int("0o755", 8)) + "\n")
    f.write(str(int("0b1101111", 2)) + "\n")

print(file_path)