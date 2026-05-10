import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# find all slide divs
slide_matches = list(re.finditer(r'<div class="slide">', html))
print(f"Total slides found: {len(slide_matches)}")

# simple stack to track divs inside the body
lines = html.split('\n')
stack = []
for i, line in enumerate(lines):
    line_num = i + 1
    # Very rudimentary count, assumes tags are relatively clean
    opens = len(re.findall(r'<div\b[^>]*>', line))
    closes = len(re.findall(r'</div>', line))
    for _ in range(opens):
        stack.append(line_num)
    for _ in range(closes):
        if stack:
            stack.pop()
        else:
            print(f"Unmatched closing div at line {line_num}")

print(f"Remaining open divs: {len(stack)}")
if stack:
    print(f"Lines where they were opened: {stack}")
