import time

# Benchmark pop(0) execution time across increasing list sizes N
# Each step measures the time to perform 100 deletions from index 0
lst = []
print("List Size (N) | Time for 100 pops from index 0 (seconds)")
print("-" * 55)

for length in range(10000, 500001, 50000):
    while len(lst) < length:
        lst.append(42)
    count = 0
    starttime = time.perf_counter()
    while count < 100:
        lst.pop(0)           # pop from start:  O(N) per pop
        # lst.pop()          # pop from end:    O(1) per pop
        # lst.pop(len(lst)//2) # pop from middle: O(N) per pop
        count += 1
    elapsed = time.perf_counter() - starttime
    print(f"{length:13d} | {elapsed:.8f} s")

