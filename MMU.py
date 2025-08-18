class MMU:
    page_faults = 0
    page_size = 4
    mem_size = 4000

    def __init__(self, policy="LRU"):
        self.policy = policy.upper()
        self.mmap = [(-1, -1)] * (MMU.mem_size // MMU.page_size)
        self.free_places = MMU.mem_size // MMU.page_size

        self.page_usage = []
        self.page_queue = []
        self.reference_bits = {}

    def reset(self):
        self.mmap = [(-1, -1)] * (MMU.mem_size // MMU.page_size)
        self.page_faults = 0
        self.free_places = MMU.mem_size // MMU.page_size
        self.page_usage.clear()
        self.page_queue.clear()
        self.reference_bits.clear()

    def handle_request(self, request):
        pid, page = request

        if self.search(request):
            if self.policy == "LRU":
                if request in self.page_usage:
                    self.page_usage.remove(request)
                self.page_usage.append(request)
            elif self.policy == "SECOND_CHANCE":
                self.reference_bits[request] = 1
            return "HIT"

        MMU.page_faults += 1

        if self.free_places > 0:
            index = self.mmap.index((-1, -1))
            self.mmap[index] = (pid, page)
            self.free_places -= 1

            if self.policy == "LRU":
                self.page_usage.append((pid, page))
            elif self.policy == "SECOND_CHANCE":
                self.page_queue.append((pid, page))
                self.reference_bits[(pid, page)] = 1
        else:
            self.eviction_system()
            index = self.mmap.index((-1, -1))
            self.mmap[index] = (pid, page)

            if self.policy == "LRU":
                self.page_usage.append((pid, page))
            elif self.policy == "SECOND_CHANCE":
                self.page_queue.append((pid, page))
                self.reference_bits[(pid, page)] = 1

        return "PAGE_FAULT"

    def eviction_system(self):
        if self.policy == "LRU":
            if self.page_usage:
                lru_page = self.page_usage.pop(0)
                index = self.mmap.index(lru_page)
                self.mmap[index] = (-1, -1)
                self.free_places += 1

        elif self.policy == "SECOND_CHANCE":
            while self.page_queue:
                page = self.page_queue.pop(0)
                if self.reference_bits.get(page, 0) == 0:
                    index = self.mmap.index(page)
                    self.mmap[index] = (-1, -1)
                    self.free_places += 1
                    self.reference_bits.pop(page, None)
                    break
                else:
                    self.reference_bits[page] = 0
                    self.page_queue.append(page)

    def search(self, request):
        return request in self.mmap

    def __repr__(self):
        return f"MMU(policy={self.policy}, mem={self.mmap}, page_faults={MMU.page_faults})"
