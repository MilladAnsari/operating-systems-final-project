import numpy as np
import matplotlib.pyplot as plt

# داده‌های نمونه: تعداد page fault بر اساس اندازه صفحه
page_sizes = [512, 1024, 2048, 4096, 8192]  # اندازه‌های صفحه به بایت
# فرض کنید که برای هر هیستوگرام داده‌های مختلفی دارید
page_faults_list = [np.random.randint(10, 100, size=len(page_sizes)) for _ in range(33)]

# ایجاد یک شکل با 11 ردیف و 3 ستون
fig, axs = plt.subplots(11, 3, figsize=(15, 35))
fig.suptitle('Page Faults vs Page Size for Different Scenarios')

# پر کردن هیستوگرام‌ها
for i in range(11):
    for j in range(3):
        index = i * 3 + j
        if index < len(page_faults_list):
            axs[i, j].bar(page_sizes, page_faults_list[index], width=300, color='blue', alpha=0.7)
            # axs[i, j].set_title(f'Scenario {index + 1}')
            # axs[i, j].set_xlabel('Page Size (bytes)')
            # axs[i, j].set_ylabel('Number of Page Faults')
            axs[i, j].set_xticks(page_sizes)  # تنظیم برچسب‌های محور x
            axs[i, j].grid(axis='y')  # افزودن شبکه به محور y

# plt.tight_layout(pad=10.5,)
plt.subplots_adjust(wspace=0.4 * 5000, hspace=0.6 * 1000)
plt.tight_layout(pad=5.5 * 10)
# تنظیم فاصله بین زیرنویس‌ها
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
