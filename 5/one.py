import re
input = open("input.txt", "r")

input_lines = input.readlines()
input_divider_index = input_lines.index("\n")

page_order = []
updates = []
max_page_number = 0

for line in input_lines[input_divider_index+1:]:
  update = [int(x) for x in line.strip().split(",")]
  max_page_number = max(max_page_number, max(update))
  updates.append(update)

page_order = [[] for _ in range(max_page_number + 1)]

for line in input_lines[:input_divider_index]:
  match = re.match("([0-9]+)\\|([0-9]+)", line)
  a = int(match[1])
  b = int(match[2])
  page_order[a].append(b)

def get_middle(update):
  assert(len(update) % 2 == 1)
  return update[int((len(update) - 1) / 2)]

def check_update_page(update, index):
  update_head = update[:index]
  pages = page_order[update[index]]
  for i in pages:
    if i in update_head:
      return False
  return True

def check_update(update):
  for i in range(len(update)):
    if not check_update_page(update, i):
      return False
  return True

update_score = 0

for update in updates:
  if check_update(update):
    update_score += get_middle(update)

print(update_score)
