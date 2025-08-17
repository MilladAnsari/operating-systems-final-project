class File:
    number = 0
    list_of_files = []
    def __init__(self, start, end):
        self.id = File.number
        File.number += 1
        self.starting_point = start
        self.ending_point = end
        File.list_of_files.append(self)