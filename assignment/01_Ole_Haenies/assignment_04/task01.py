import sys

test_arr = list(range(30))

sys.stdout.write(f"Original: {test_arr}\n")
sys.stdout.write(f"Filtered: {str(list(filter(lambda x: x % 2 == 0, test_arr)))}\n")
