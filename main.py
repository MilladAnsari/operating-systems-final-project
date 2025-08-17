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
