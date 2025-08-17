# OS Project – Page Replacement Simulation

## 📌 Description
This project simulates Operating System memory management to analyze how **page size** affects **page faults**.  
Two replacement policies are implemented: **LRU** (Least Recently Used) and **Second Chance**, within a custom **MMU** (Memory Management Unit) class.  
Workload generation is **multi‑threaded** and models locality in file access patterns.

---

## 🚀 Features
- Adjustable memory size and page size for experiments.
- Implementation of LRU & Second Chance replacement algorithms.
- Thread‑based file access with locality-aware random access simulation.
- Modular Python code structure for easy extensions.

---

## 📂 Project Structure
```
.
├── CPU.py           # Simulates CPU and thread scheduling
├── File.py          # Represents files with start/end addresses
├── Thread.py        # Simulates threads and weighted file selection
├── MMU.py           # Memory management unit – implement your algorithms here
├── main.py          # Entry point (to be created by user for running simulation)
├── os-project.pdf   # Project description
└── README.md
```

---

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/MilladAnsari/operating-systems-final-project.git
cd operating-systems-final-projec

# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

## ▶️ Usage
1. Implement the missing methods inside `MMU.py`:
   - `reset()`
   - `handle_request()`
   - `eviction_system()` (LRU and Second Chance logic)
   - `search()`
2. Create `main.py` to:
   - Initialize `MMU`, `CPU`, and `Thread` objects
   - Run the simulation
   - Print statistics (total page faults, etc.)

Example `main.py` skeleton:
```python
from CPU import CPU
from Thread import Thread
from MMU import MMU

# Example setup
MMU.page_size = 4
MMU.mem_size = 4000

cpu = CPU()
# Add threads and start simulation
cpu.start()

print(f"Total page faults: {MMU.page_faults}")
```

---

## 📊 Example Output
```
Running simulation...
Total page faults: 157
```

---

## 🏷 License
This project is for **educational purposes** as part of an Operating Systems course.
