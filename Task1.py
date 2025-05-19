#Task1
from collections import Counter
from typing import List

def most_frequent_lengths(strings: List[str]) -> List[str]:
    if not strings:
        return []

    lengths = [len(s) for s in strings]
    freq = Counter(lengths)
    max_freq = max(freq.values())
    common_lengths = [length for length, count in freq.items() if count == max_freq]

    return [s for s in strings if len(s) in common_lengths]

# Example test cases
if __name__ == "__main__":
    print("Test 1:", most_frequent_lengths(['a', 'ab', 'abc', 'cd', 'def', 'gh']))
    # Explanation: lengths = [1, 2, 3, 2, 3, 2] => most frequent = 2 => ['ab', 'cd', 'gh']
    # Output: ['ab', 'cd', 'gh']

    print("Test 2:", most_frequent_lengths(['hello', 'hi', 'yo', 'yes', 'no']))
    # Explanation: lengths = [5, 2, 2, 3, 2] => most frequent = 2 => ['hi', 'yo', 'no']
    # Output: ['hi', 'yo', 'no']

    print("Test 3:", most_frequent_lengths([]))
    # Explanation: empty input => []

    print("Test 4:", most_frequent_lengths(['apple', 'dog', 'cat', 'banana', 'pear', 'fig']))
    # Explanation: lengths = [5, 3, 3, 6, 4, 3] => most frequent = 3 => ['dog', 'cat', 'fig']
    # Output: ['dog', 'cat', 'fig']

    print("Test 5:", most_frequent_lengths(['x', 'yy', 'zzz', 'ww', 'pp', 'k']))
    # Explanation: lengths = [1, 2, 3, 2, 2, 1] => most frequent = 2 => ['yy', 'ww', 'pp']
    # Output: ['yy', 'ww', 'pp']