import time

# Benchmark random access time O(1) across growing list sizes
lst = []
print("List Size (N) | Time for 1,000 reads (seconds)")
print("-" * 46)

for length in range(4000, 1000001, 100000):
    while len(lst) < length:
        lst.append(42)
    count = 0
    x = 0
    starttime = time.perf_counter()
    while count < 1000:
        x += lst[count]                 # read from beginning: O(1)
        # x += lst[length//2 + count]   # read from middle:    O(1)
        # x += lst[length - (count+1)]  # read from end:       O(1)
        count += 1
    elapsed = time.perf_counter() - starttime
    print(f"{length:13d} | {elapsed:.8f} s")

