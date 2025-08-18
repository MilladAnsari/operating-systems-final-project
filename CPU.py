from MMU import MMU

class CPU:
    def __init__(self):
        self.list_thread = []

    def AddThread(self, Thread):
        self.list_thread.append(Thread)

    def reset(self):
        for t in self.list_thread:
            t.reset()

    def run(self, mmu):
        for i in range(50):
            for i in range(len(self.list_thread)):
                selected_thread = self.list_thread[i]

                mmu.handle_request(selected_thread.Start())