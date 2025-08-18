class MMU:
    page_faults = 0
    page_size = 4     
    mem_size = 4000
    
    def __init__(self):
        self.mmap = [(-1, -1)] * (MMU.mem_size // MMU.page_size)
        self.free_places = MMU.mem_size // MMU.page_size
        self.page_usage = []

    def reset(self):
        self.mmap = [(-1, -1)] * (MMU.mem_size // MMU.page_size)
        self.page_faults = 0
        self.free_places = MMU.mem_size // MMU.page_size
        self.page_usage.clear()

    def handle_request(self, request):
        pid, page = request

        if self.search(request):
            if request in self.page_usage:
                self.page_usage.remove(request)
            self.page_usage.append(request)
            return "HIT"

        MMU.page_faults += 1

        if self.free_places > 0:
            index = self.mmap.index((-1, -1))
            self.mmap[index] = (pid, page)
            self.page_usage.append((pid, page))
            self.free_places -= 1
        else:
            self.eviction_system()
            index = self.mmap.index((-1, -1))
            self.mmap[index] = (pid, page)
            self.page_usage.append((pid, page))

        return "PAGE_FAULT"

    def eviction_system(self):
        if self.page_usage:
            lru_page = self.page_usage.pop(0) 
            index = self.mmap.index(lru_page)
            self.mmap[index] = (-1, -1)
            self.free_places += 1

    def search(self, request):
        return request in self.mmap

    def __repr__(self):
        return f"MMU(mem={self.mmap}, page_faults={MMU.page_faults})"
