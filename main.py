from MMU import MMU
from File import File
from CPU import CPU
from Thread import Thread
import random
cpu = CPU()
file_cnt = 2000
for _ in range(file_cnt):
    tah = random.randint(1, 16)
    file = File(0, tah * 1024)
for _ in range(64):
    t = Thread()
    cpu.AddThread(t)
# print(len(cpu.list_thread))

# print(File.number)
# for f in File.list_of_files:
#     print(f.starting_point, ' ', f.ending_point)

# mmu = MMU(policy='LRU')
# mmu2 = MMU(policy='SECOND_CHANCE')
# # تست شبیه‌سازی
# f0 = File(start=0, end=15)
# f1 = File(0, 25)
# f2 = File(25, 35)
# requests = [(f0, 0), (f0, 1), (f0, 2), (f0, 0), (f1, 0), (f2, 26)]
# for req in requests:
#     print(req, "=>", mmu.handle_request(req))
# print(mmu)
# mmu.reset()

# for req in requests:
#     print(req, "=>", mmu2.handle_request(req))


# print(mmu2)