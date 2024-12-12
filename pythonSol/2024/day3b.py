#wasnt able to come up with anything myself, gave up and took the following code which i then tried to learn from and understand how it works
import re


memory_content = open('../../data/day3.txt').read()
instruction_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')


conditional_pattern = re.compile(r".+?(?=don?'?t?\(\)|\Z)", re.DOTALL)
memory_parts_match = conditional_pattern.findall(memory_content)
result = sum([sum([int(instruction.group(1)) * int(instruction.group(2)) for instruction in instruction_pattern.finditer(part)]) for part in memory_parts_match if not part.startswith("don't()")])

print(result)
