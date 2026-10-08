x = 5
d = 2.4
values = [x - 2,
          x + d,
          x / 2,
          d + x / 4,
          x // 3,
          x + 0x2a,
          d + 0x2a,
          d * 2 // 3,
]

for value in values:
    print(type(value).__name__, value)
