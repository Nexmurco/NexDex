

class Species:
    def __init__(self, id):
        self.id = id
    
    def set_base_stats(self, base_stats):
        self.base_stats = base_stats
    
    def set_name(self, name):
        self.name = name

    def add_location(self, location):
        if self.location is None:
            self.location = []
        self.location.append(location)

    def set_type1(self, type1):
        self.type1 = type1

    def set_type2(self, type2):
        self.type2 = type2

    def set_ev_yield(self, ev_yield):
        self.ev_yield = ev_yield
    
    def set_exp_yield(self, exp_yield):
        self.exp_yield = exp_yield
    
    def add_move(self, move, level = None):
        if self.move_pool is None:
            self.move_pool = []
        self.move_pool.append((move, level))

    
