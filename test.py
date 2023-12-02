"""
suits = "cdhs"
ranks = "AKQJT98765432"


deck = [f"{rank}{suit}" for rank in ranks for suit in suits]

# Generate all possible combinations of two cards
max_length = 50
pocket_range = []
for card1 in deck:
    for card2 in deck:
        if card1 != card2:
            pocket_range.append([card1, card2])
            if len(pocket_range) >= max_length:
                break
    if len(pocket_range) >= max_length:
        break

# Display the combinations
for combination in pocket_range:
    print(combination)
print(len(pocket_range))

def has_duplicates(lst):
    seen = set()
    for inner_list in lst:
        # Convert the inner list to a tuple to make it hashable
        inner_tuple = tuple(inner_list)
        if inner_tuple in seen:
            return True
        seen.add(inner_tuple)
    return False

if has_duplicates(pocket_range):
    print("There are duplicates in the list.")
else:
    print("No duplicates found in the list.")
"""
"""
# Example usage
hand1 = ["7s", "9h", "9h", "5s", "As", "6s", "7c"]
#["6s", "5s", "7s", "8s", "9s", "As", "Ac"]
hand2 = ["7s", "9h", "9h", "5s", "As", "6s", "7c"]

['2s', '3h', '4d', '5s', '6s']
['2s', '3h', '4d', '5s', '7c']
['2s', '3h', '4d', '5s', '8h']
['2s', '3h', '4d', '5s', '9d']
['2s', '3h', '4d', '5s', '10c']

compare_hands(hand1, hand2)
"""