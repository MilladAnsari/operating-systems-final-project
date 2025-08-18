from MMU import MMU


algo = input("Enter replacement policy (LRU / SECOND_CHANCE): ")
mmu = MMU(policy=algo)

# تست شبیه‌سازی
requests = [(1, 0), (1, 1), (1, 2), (1, 0), (2, 0), (3, 0)]
for req in requests:
    print(req, "=>", mmu.handle_request(req))

print(mmu)