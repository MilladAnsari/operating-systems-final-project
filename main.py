from MMU import MMU
from File import File
from CPU import CPU
from Thread import Thread
import random
import matplotlib.pyplot as plt

cpu = CPU()
file_cnt = 1024
current = 0
for _ in range(file_cnt):
    tah = random.randint(1, 16)
    File(0, tah )
for _ in range(32):
    cpu.AddThread(Thread())
# print(t)
TEMP = [[0] * 10, [0] * 10, [0] * 10]
# SC_TEMP = []
# LRU2x_TEMP = []
# for _ in range(10):
#     LRU_TEMP.append(0)
#     SC_TEMP.append(0)
#     LRU2x_TEMP.append(0)
mmu = MMU()
fig, axs = plt.subplots(11, 3, figsize=(15, 35))
# fig.suptitle('Page Faults vs Page Size for Different Scenarios')
for i in range(10):
    mmu.resize_mem(4000)
    mmu.resize_page(4)
    for case in range(3):
        if case % 2 == 0:
            mmu.set_policy('LRU')
            if case == 2:
                mmu.resize_mem(8000)
        else:
            mmu.set_policy('SECOND_CHANCE')
        ss = 1
        page_faults = []
        page_sizes = []# اندازه‌های صفحه به بایت
        dc = dict()
        for __ in range(10):
            # print(ss)
            mmu.resize_page(ss)
            page_sizes.append(str(ss))
            mmu.reset()
            cpu.reset()
            cpu.run(mmu)
            page_faults.append(MMU.page_faults - 190)
            ss += 1
            # axs[i, case].bar(ss, MMU.page_faults, width= 7, color='blue', alpha=0.7)
            # print('(', ss, ' ', MMU.page_faults, ')', end = ' ')
            # page_sizes = [512, 1024, 2048, 4096, 8192]  # اندازه‌های صفحه به بایت
            # page_faults = [100, 80, 60, 30, 10]  # تعداد page fault مربوط به هر اندازه صفحه
        # print()
        # TEMP[case] += page_faults
        for j in range(10):
            TEMP[case][j] += page_faults[j] / 10
        axs[i, case].bar(page_sizes, page_faults, color='skyblue', edgecolor='black')
    # print(i)
axs[10, 0].bar(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], TEMP[0], color='skyblue', edgecolor='black')
axs[10, 1].bar(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], TEMP[1], color='skyblue', edgecolor='black')
axs[10, 2].bar(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], TEMP[2], color='skyblue', edgecolor='black')


            # ایجاد هیستوگرام
        # plt.bar(page_sizes, page_faults, width=300, color='blue', alpha=0.7)

        # # افزودن عنوان و برچسب‌ها
        # plt.title('Page Faults vs Page Size')
        # plt.xlabel('Page Size (bytes)')
        # plt.ylabel('Number of Page Faults')

        # نمایش هیستوگرام
        # plt.xticks(page_sizes)  # تنظیم برچسب‌های محور x
        # plt.grid(axis='y')  # افزودن شبکه به محور y
        # plt.show()
            
            
# plt.subplots_adjust(wspace=0.4 * 5000, hspace=0.6 * 1000)
# plt.tight_layout(pad=5.5 * 10)
# تنظیم فاصله بین زیرنویس‌ها
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

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