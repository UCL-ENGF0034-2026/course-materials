import time

# Demonstrating the O(N^2) trap of repeated list.pop(0)
# Deleting from index 0 shifts all remaining elements on each pop.
# We test with N = 100,000 items so the benchmark completes in a few seconds.
N = 100_000
print(f"Creating a list of {N:,} items...")
lst = list(range(N))

print("\nEmptying the list via lst.pop(0)...")
print("Elapsed (s) | Items Popped | Remaining Items")
print("-" * 46)

starttime = time.perf_counter()
count = 0
while count < N:
    lst.pop(0)  # delete first item: shifts remaining (N - 1 - count) elements
    count += 1
    if count % 10_000 == 0:
        elapsed = time.perf_counter() - starttime
        remaining = len(lst)
        print(f"{elapsed:11.4f} | {count:12d} | {remaining:15d}")

total_time = time.perf_counter() - starttime
print("-" * 46)
print(f"Total time for {N:,} front pops: {total_time:.4f} s (O(N^2) cumulative)")
print("Note: In Week 3 we introduce Queues (FIFO) where front pop is O(1)!")
