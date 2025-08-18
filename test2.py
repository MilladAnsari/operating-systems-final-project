import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# تنظیمات
np.random.seed(42)
n_histograms = 33
n_rows = 11
n_cols = 3

# ایجاد figure
fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 35))
axes = axes.flatten()

# لیست شهرها یا مناطق مختلف (برای عناوین)
# locations = [f'District {i+1}' for i in range(33)]

# تولید داده‌های متنوع برای شبیه‌سازی واقعی‌تر
for i in range(n_histograms):
    # پارامترهای مختلف برای هر منطقه
    if i < 11:  # مناطق مرکزی (زمان کمتر)
        mean = np.random.uniform(20, 35)
        std = np.random.uniform(5, 10)
        n_commuters = np.random.randint(800, 1200)
    elif i < 22:  # مناطق حومه (زمان متوسط)
        mean = np.random.uniform(30, 45)
        std = np.random.uniform(8, 15)
        n_commuters = np.random.randint(600, 1000)
    else:  # مناطق دور (زمان بیشتر)
        mean = np.random.uniform(40, 55)
        std = np.random.uniform(10, 20)
        n_commuters = np.random.randint(400, 800)
    
    # تولید داده با توزیع‌های مختلف
    if i % 3 == 0:  # توزیع نرمال
        data = np.random.normal(mean, std, n_commuters)
    elif i % 3 == 1:  # توزیع چوله
        data = np.random.gamma(2, mean/2, n_commuters)
    else:  # ترکیب دو توزیع (دو پیک)
        data1 = np.random.normal(mean - 10, std/2, n_commuters//2)
        data2 = np.random.normal(mean + 10, std/2, n_commuters//2)
        data = np.concatenate([data1, data2])
    
    data = data[data > 0]  # حذف مقادیر منفی
    data = data[data < 100]  # حذف مقادیر خیلی بزرگ
    
    # رسم هیستوگرام
    n, bins, patches = axes[i].hist(data, bins=15, color='#6B8CAE', 
                                   edgecolor='white', linewidth=1)
    
    # تنظیمات ظاهری
    axes[i].set_xlabel('Time (min)', fontsize=8)
    axes[i].set_ylabel('Count', fontsize=8)
    # axes[i].set_title(locations[i], fontsize=9, fontweight='bold')
    axes[i].grid(True, axis='y', alpha=0.3, linewidth=0.5)
    axes[i].set_xlim(0, 80)
    
    # تنظیم تیک‌ها
    axes[i].tick_params(axis='both', labelsize=7)
    
    # حذف خطوط کادر
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)
    
    # اضافه کردن آمار روی نمودار
    # axes[i].text(0.7, 0.95, f'n={len(data)}', 
    #             transform=axes[i].transAxes, fontsize=7,
    #             verticalalignment='top')
    # axes[i].text(0.7, 0.85, f'μ={np.mean(data):.1f}', 
    #             transform=axes[i].transAxes, fontsize=7,
    #             verticalalignment='top')

# تنظیم فاصله بین نمودارها
plt.tight_layout(pad=5.5)

# ذخیره و نمایش
plt.savefig('33_histograms_grid.png', dpi=150, bbox_inches='tight')
plt.show()
