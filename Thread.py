import random
from File import File 
import numpy as np
from MMU import MMU
import math
import time
class Thread:
    number = 0
    MAXIMUM_NUMBER_OF_FILES = 4
    def __init__(self):
        self.id = Thread.number
        Thread.number += 1
        self.files = []
        self.file_weights = []
        temp = random.randrange(1, Thread.MAXIMUM_NUMBER_OF_FILES)
        for i in range(temp):
            selected = random.randint(0, len(File.list_of_files))
            chosen = File.list_of_files.pop(selected)
            self.files.append(chosen)
            self.file_weights.append(1)
            File.list_of_files.remove(File.list_of_files[selected])
    
    def reset(self):
        for weight in self.file_weights:
            weight = 1     
    
    def Start(self):
        if not self.files:
            return
        
        # Choose a file index based on weights
        selected_index = random.choices(range(len(self.files)), weights=self.file_weights, k=1)[0]
        file = self.files[selected_index]
        
        # Increase weight to favor future selections
        self.file_weights[selected_index] += 1

        return (file, Thread.generate_random_file_access(file.starting_point, file.ending_point))
    
    def generate_random_file_access(a, b):
        mean =  np.random.choice([1, 2, 3]) * (b - a) / 4 + a
        std_dev = math.log2(b - a)
        return int(np.clip(np.random.normal(mean, std_dev), a, b))
