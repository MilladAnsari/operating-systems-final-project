import numpy as np
import matplotlib.pyplot as plt

# داده‌های نمونه: تعداد page fault بر اساس اندازه صفحه
page_sizes = [512, 1024, 2048, 4096, 8192]  # اندازه‌های صفحه به بایت
page_faults = [100, 80, 60, 30, 10]  # تعداد page fault مربوط به هر اندازه صفحه

# ایجاد هیستوگرام
plt.bar(page_sizes, page_faults, width=300, color='blue', alpha=0.7)

# افزودن عنوان و برچسب‌ها
plt.title('LRU')
plt.xlabel('Page Size (bytes)')
plt.ylabel('Number of Page Faults')

# نمایش هیستوگرام
plt.xticks(page_sizes)  # تنظیم برچسب‌های محور x
plt.grid(axis='y')  # افزودن شبکه به محور y
plt.show()
