class MMU:
    page_faults = 0
    page_size = 4
    mem_size = 4000
    def __init__(self):
        self.mmap = [(-1, -1)] * (MMU.mem_size // MMU.page_size)
        self.free_places = (MMU.mem_size // MMU.page_size)
    
    def reset(self):
        self.mmap = [(-1, -1)] * (MMU.mem_size // MMU.page_size)
        self.free_places = (MMU.mem_size // MMU.page_size)
    
    def handle_request(self, request):
        # TO DO 
        pass
    
    
    def eviction_system(self):
        # TO DO
        pass
        
    def search(self, request):
        # TO DO
        pass
    