import time

# Benchmark list.append() O(1) amortised time over 10,000,000 appends
lst = []
count = 0
starttime = time.perf_counter()
print("Elapsed (s) | Appended Items")
print("-" * 30)

while count < 10000000:
    lst.append(count)
    if count % 1000000 == 0 and count > 0:
        elapsed = time.perf_counter() - starttime
        print(f"{elapsed:11.4f} | {count:14d}")
    count += 1

total_time = time.perf_counter() - starttime
print("-" * 30)
print(f"Total time for 10M appends: {total_time:.4f} s (strictly O(1) amortised)")
    
