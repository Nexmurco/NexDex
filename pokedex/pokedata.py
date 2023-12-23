from pokedex import pokestats

class Pokemon:
    def __init__(self, id):
        self.id = id
    
    def set_ivs(self, ivs):
        self.ivs = ivs

    def set_evs(self, evs):
        self.evs = evs
    
    def set_base_stats(self, base_stats):
        self.base_stats = base_stats
    
    def set_stats(self, stats):
        self.stats = stats
    
    def set_name(self, name):
        self.name = name

    def set_nickname(self, nickname):
        self.nickname = nickname

    def add_location(self, location):
        if self.location is None:
            self.location = []
        self.location.append(location)

    def set_type1(self, type1):
        self.type1 = type1

    def set_type2(self, type2):
        self.type2 = type2

    def add_battle_experience(self, pokemon, level):
        if self.battle_log is None:
            self.battle_log = []
        self.battle_log((pokemon, level))
        #potentially add exp and ev here?
    
    def set_current_hp(self, hp):
        self.current_hp = hp
    
    def set_status_condition(self, status):
        self.status_condition = status
    
    def set_held_item(self, item):
        self.held_item = item
    
    
    

    
    
