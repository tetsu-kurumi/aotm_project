
from collections import Counter

hand1 = ["6s", "5c", "7h", "8s", "9s", "As", "Ac"]
hand2 = ["7s", "9c", "9h", "9s", "As", "6s", "7c"]

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

hand1.sort(key=lambda card: values[card[:-1]])

print(hand1[6][0])


def extract_nums(cards):
    num_list = []
    for i in range (len(cards)):
        key_to_convert = cards[i][0]
        num_list.append(values[key_to_convert])
    print(sorted(num_list))
    return(sorted(num_list))

num_list = extract_nums(hand1)
counter = Counter(num_list)
most_common = counter.most_common()
print(most_common)