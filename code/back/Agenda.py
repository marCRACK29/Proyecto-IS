class Agenda:
    ID = None
    rutM = None
    start = None
    free = True

    def __init__(self, ID, rutM, start, free):
        self.ID = ID
        self.rutM = rutM
        self.start = start
        self.free = free