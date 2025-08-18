from MMU import MMU


mmu = MMU(policy='LRU')
mmu2 = MMU(policy='SECOND_CHANCE')
# تست شبیه‌سازی
requests = [(1, 0), (1, 1), (1, 2), (1, 0), (2, 0), (3, 0)]
for req in requests:
    print(req, "=>", mmu.handle_request(req))
print(mmu)
mmu.reset()

for req in requests:
    print(req, "=>", mmu2.handle_request(req))
    

print(mmu2)