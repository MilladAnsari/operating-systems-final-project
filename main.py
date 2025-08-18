from MMU import MMU
from File import File

mmu = MMU(policy='LRU')
mmu2 = MMU(policy='SECOND_CHANCE')
# تست شبیه‌سازی
f0 = File(start=0, end=15)
f1 = File(0, 25)
f2 = File(25, 35)
requests = [(f0, 0), (f0, 1), (f0, 2), (f0, 0), (f1, 0), (f2, 26)]
for req in requests:
    print(req, "=>", mmu.handle_request(req))
print(mmu)
mmu.reset()

for req in requests:
    print(req, "=>", mmu2.handle_request(req))


print(mmu2)