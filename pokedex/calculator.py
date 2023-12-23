from fractions import Fraction
import random
import json

class Calculator:
    LOW_ROLL = 0.85
    HIGH_ROLL = 1

    CHARACTERISTIC_DICT = {
        "Loves to eat": ("hp", 0),
        "Often dozes off": ("hp", 1),
        "Often scatters things": ("hp", 2), 
        "Scatters things often": ("hp", 3),
        "Likes to relax": ("hp", 4),

        "Proud of its power": ("attack", 0),
        "Likes to thrash about": ("attack", 1),
        "A little quick tempered": ("attack", 2),
        "Likes to fight": ("attack", 3),
        "Quick tempered": ("attack", 4),

        "Sturdy body": ("defense", 0),
        "Capable of taking hits": ("defense", 1),
        "Highly persistent": ("defense", 2),
        "Good endurance": ("defense", 3),
        "Good perseverance": ("defense", 4),

        "Likes to run": ("speed", 0),
        "Alert to sounds": ("speed", 1),
        "Impetuous and silly": ("speed", 2),
        "Somewhat of a clown": ("speed", 3),
        "Quick to flee": ("speed", 4),

        "Highly curious": ("special_attack", 0),
        "Mischievous": ("special_attack", 1),
        "Thoroughly cunning": ("special_attack", 2),
        "Often lost in thought": ("special_attack", 3),
        "Very finicky": ("special_attack", 4),

        "Strong willed": ("special_defense", 0),
        "Somewhat vain": ("special_defense", 1),
        "Strongly defiant": ("special_defense", 2),
        "Hates to lose": ("special_defense", 3),
        "Somewhat stubborn": ("special_defense", 4),
    }

    NATURE_SET_NEGATIVE = frozenset([
        frozenset(["adamant", "special_attack"]),
        frozenset(["bashful", "special_attack"]),
        frozenset(["bold", "attack"]),
        frozenset(["brave", "speed"]),
        frozenset(["calm", "attack"]),
        frozenset(["careful", "special_attack"]),
        frozenset(["docile", "defense"]),
        frozenset(["gentle", "defense"]),
        frozenset(["hardy", "attack"]),
        frozenset(["hasty", "defense"]),
        frozenset(["impish", "special_attack"]),
        frozenset(["jolly", "special_attack"]),
        frozenset(["lax", "special_defense"]),
        frozenset(["lonely", "defense"]),
        frozenset(["mild", "defense"]),
        frozenset(["modest", "attack"]),
        frozenset(["naive", "special_defense"]),
        frozenset(["naughty", "special_defense"]),
        frozenset(["quiet", "speed"]),
        frozenset(["quirky", "special_defense"]),
        frozenset(["rash", "special_defense"]),
        frozenset(["relaxed", "speed"]),
        frozenset(["sassy", "speed"]),
        frozenset(["serious", "speed"]),
        frozenset(["timid", "attack"])
    ])

    NATURE_SET_POSITIVE = frozenset([
        frozenset(["adamant", "attack"]),
        frozenset(["bashful", "attack"]),
        frozenset(["bold", "defense"]),
        frozenset(["brave", "attack"]),
        frozenset(["calm", "defense"]),
        frozenset(["careful", "special_defense"]),
        frozenset(["docile", "defense"]),
        frozenset(["gentle", "special_defense"]),
        frozenset(["hardy", "attack"]),
        frozenset(["hasty", "speed"]),
        frozenset(["impish", "defense"]),
        frozenset(["jolly", "speed"]),
        frozenset(["lax", "defense"]),
        frozenset(["lonely", "attack"]),
        frozenset(["mild", "special_attack"]),
        frozenset(["modest", "special_attack"]),
        frozenset(["naive", "speed"]),
        frozenset(["naughty", "attack"]),
        frozenset(["quiet", "special_attack"]),
        frozenset(["quirky", "special_defense"]),
        frozenset(["rash", "special_attack"]),
        frozenset(["relaxed", "defense"]),
        frozenset(["sassy", "special_defense"]),
        frozenset(["serious", "speed"]),
        frozenset(["timid", "speed"])
    ])

    __reverse_level_dict = None

    @staticmethod
    def possible_iv_values(characteristic):
        highest_iv = {}
        highest_iv["stat"] = Calculator.CHARACTERISTIC_DICT[characteristic][0]
        remainder = Calculator.CHARACTERISTIC_DICT[characteristic][1]

        iv_values = []

        while remainder < 32:
            iv_values.append(remainder)
            remainder += 5

        highest_iv["values"] = iv_values
        return highest_iv

    @staticmethod
    def reverse_level_dict():
        if Calculator.__reverse_level_dict is None:
            file = open('D:\Code\Pokedex\level_data_rev.json')
            Calculator.__reverse_level_dict = json.load(file)
        return Calculator.__reverse_level_dict

    @staticmethod
    def divide_low(dividend, divisor):
        return round(dividend / divisor, 0)

    @staticmethod
    def divide_high(dividend, divisor):
        if(divisor >= 1):
            return (round(dividend / divisor))
        
        return (int((dividend + 1) / divisor))
    
    @staticmethod
    def multiply_low(multiplicand, multiplier):
        return (int(multiplicand * multiplier))

    @staticmethod
    def multiply_high(multiplicand, multiplier):
        if(multiplier <= 1):
            return (round(multiplicand * multiplier))
        
        return (int((multiplicand + 1) * multiplier) - 1)
    
    @staticmethod
    def get_nature_bonus(nature, stat):
        if set([nature, stat]) in Calculator.NATURE_SET_POSITIVE:
            return 1.1
        if set([nature, stat]) in Calculator.NATURE_SET_NEGATIVE:
            return 0.9
        return 1

    @staticmethod
    def hp_calc(base_stat, level, iv, ev):
        ev_calc = int(ev / 4)
        base_calc = (base_stat * 2) + iv + ev_calc
        level_calc = int(base_calc * level / 100) + level + 10
        return int(level_calc)

    @staticmethod
    def randomize_stats_within_bst(bst):
        base = bst - 70

        stats = []

        weight = 0
        for i in range(6):
            stats.append(random.uniform(0,1))
            weight += stats[i]

        stats = [int(max(1, round(base * s / weight)))+10  for s in stats]
        
        stats[0] = stats[0] + 10

        new_weight = 0

        for i in range(6):
            new_weight += stats[i]

        return new_weight

        



    @staticmethod
    def base_hp_calc(stat, level):
        possibility_list = {}
        possibility_list["high"] = stat
        possibility_list["low"] = stat

        possibility_list = {k: int(v - (10 + level)) for k,v in possibility_list.items()}

        frac = Fraction(100, level)

        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], frac.denominator)
        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], frac.denominator)

        possibility_list["high"] = Calculator.multiply_high(possibility_list["high"], frac.numerator)
        possibility_list["low"] = Calculator.multiply_low(possibility_list["low"], frac.numerator)

        #skip ev step

        possibility_list["high"] = possibility_list["high"] - 0
        possibility_list["low"] = possibility_list["low"] - 31

        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], 2)
        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], 2)
        return possibility_list


    @staticmethod
    def stat_calc(base_stat, level, iv, ev, nature):
        ev_calc = int(ev / 4)
        base_calc = (base_stat * 2) + iv + ev_calc
        level_calc = int(base_calc * level / 100) + 5
        stat = int(level_calc * nature)
        return stat

    @staticmethod
    def base_stat_calc(stat, nature, level):
        possibility_list = {}
        possibility_list["high"] = stat
        possibility_list["low"] = stat

        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], nature)
        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], nature)

        possibility_list = {k: int(v - 5) for k,v in possibility_list.items()}

        frac = Fraction(100, level)

        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], frac.denominator)
        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], frac.denominator)

        possibility_list["high"] = Calculator.multiply_high(possibility_list["high"], frac.numerator)
        possibility_list["low"] = Calculator.multiply_low(possibility_list["low"], frac.numerator)

        #skip ev step

        possibility_list["high"] = possibility_list["high"] - 0
        possibility_list["low"] = possibility_list["low"] - 31

        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], 2)
        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], 2)
        return possibility_list

    @staticmethod 
    def base_stats(level, hp, attack, defense, special_attack, special_defense, speed, nature, characteristic_stat, characteristic_value):


        #the bst should be the same within a margin of error as the original pokemon
        #base stats have a range of 11-255 and hp from 21-255
        #hp calc is HP = floor(0.01 *(2 * base + IV + florr(0.25 * EV)) * LEVEL) + LEVEL + 10
        #Stat calc is STAT = (floor(0.01 * (2 * base + IV + floor(.25 * EV)) * Level) + 5) * Nature

        # we will assume 0 ev and calc for 0 and 31 iv

        #docile, likes to run, 18hp 10atk 12def 9sat 10sdef 15(speed)

        return 0
    
    @staticmethod
    def damage_calc(level, base_power, attack, defense, stab, type1, type2):
        damage = {}
        value = int(level * 2 / 5) + 2
        value = int(value * base_power)
        value = int(value * attack)
        value = int(value / 50)
        value = int(value / defense) + 2
       
        damage["high"] = value
        damage["low"] = int(value * .85)
        damage = {k: int(v * stab) for k,v in damage.items()}

        damage = {k: int(v * type1) for k,v in damage.items()}
        damage = {k: int(v * type2) for k,v in damage.items()}
        return damage
    
    @staticmethod
    def damage_calc_debug(level, base_power, attack, defense, stab, type1, type2):
        damage = {}
        value = int(level * 2 / 5) + 2
        print(value)
        value = int(value * base_power)
        print(value)
        value = int(value * attack)
        print(value)
        value = int(value / 50)
        print(value)
        value = int(value / defense) + 2
        print(value)
       
        damage["high"] = value
        damage["low"] = int(value * .85)
        print(damage)
        damage = {k: int(v * stab) for k,v in damage.items()}
        print(damage)

        damage = {k: int(v * type1) for k,v in damage.items()}
        print(damage)
        damage = {k: int(v * type2) for k,v in damage.items()}
        print(damage)
        return damage

    @staticmethod
    def reverse_calc_attack(hp_lost, defense, type1, type2, stab, crit, base_power, level):
        
        possibility_list = {}
        
        possibility_list["high"] = hp_lost
        possibility_list["low"] = hp_lost

        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], type2)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], type2)

        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], type1)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], type1)

        possibility_list = {k: round(v / stab) for k,v in possibility_list.items()}

        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], Calculator.HIGH_ROLL)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], Calculator.LOW_ROLL)

        possibility_list = {k: int(v / crit) for k,v in possibility_list.items()}

        possibility_list = {k: int(v - 2) for k,v in possibility_list.items()}

        possibility_list["low"] = Calculator.multiply_low(possibility_list["low"], defense)
        possibility_list["high"] = Calculator.multiply_high(possibility_list["high"], defense)

        possibility_list["low"] = Calculator.multiply_low(possibility_list["low"], 50)
        possibility_list["high"] = Calculator.multiply_high(possibility_list["high"], 50)

        forward_calc = ((int((level * 2) / 5)) + 2) * base_power

        possibility_list = {k: int(v / forward_calc) for k,v in possibility_list.items()}

        return possibility_list

    @staticmethod
    def reverse_calc_attack_debug(hp_lost, defense, type1, type2, stab, crit, base_power, level):
        
        possibility_list = {}
        
        possibility_list["high"] = hp_lost
        possibility_list["low"] = hp_lost
        print(possibility_list)

        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], type2)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], type2)
        print(possibility_list)
        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], type1)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], type1)
        print(possibility_list)
        possibility_list = {k: round(v / stab) for k,v in possibility_list.items()}
        print(possibility_list)
        # reasoning why "low" uses HIGH_ROLL and "high" uses LOW_ROLL
        # "low" and "high" refer to the value of the attack stat.
        # A low attack value needs a high roll and a high attack value needs a low roll to produce the same damage output
        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], Calculator.HIGH_ROLL)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], Calculator.LOW_ROLL)
        print(possibility_list)
        possibility_list = {k: int(v / crit) for k,v in possibility_list.items()}
        print(possibility_list)
        possibility_list = {k: int(v - 2) for k,v in possibility_list.items()}
        print(possibility_list)
        possibility_list["low"] = Calculator.multiply_low(possibility_list["low"], defense)
        possibility_list["high"] = Calculator.multiply_high(possibility_list["high"], defense)
        print(possibility_list)
        possibility_list["low"] = Calculator.multiply_low(possibility_list["low"], 50)
        possibility_list["high"] = Calculator.multiply_high(possibility_list["high"], 50)
        print(possibility_list)
        forward_calc = ((int((level * 2) / 5)) + 2) * base_power
        print("forward_calc: " + str(forward_calc))
        possibility_list = {k: int(v / forward_calc) for k,v in possibility_list.items()}
        print(possibility_list)


        return possibility_list

    @staticmethod
    def reverse_calc_defense(percent_lost, defense, type1, type2, stab, base_power, level, crit = 1):
        possibility_list = {}
        
        possibility_list["high"] = percent_lost
        possibility_list["low"] = percent_lost

        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], type2)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], type2)

        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], type1)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], type1)

        possibility_list = {k: round(v / stab) for k,v in possibility_list.items()}

        possibility_list["low"] = Calculator.divide_low(possibility_list["low"], Calculator.HIGH_ROLL)
        possibility_list["high"] = Calculator.divide_high(possibility_list["high"], Calculator.LOW_ROLL)

        possibility_list = {k: int(v / crit) for k,v in possibility_list.items()}

        possibility_list = {k: int(v - 2) for k,v in possibility_list.items()}

        possibility_list["low"] = Calculator.multiply_low(possibility_list["low"], defense)
        possibility_list["high"] = Calculator.multiply_high(possibility_list["high"], defense)

        possibility_list["low"] = Calculator.multiply_low(possibility_list["low"], 50)
        possibility_list["high"] = Calculator.multiply_high(possibility_list["high"], 50)

        forward_calc = ((int((level * 2) / 5)) + 2) * base_power

        possibility_list = {k: int(v / forward_calc) for k,v in possibility_list.items()}

        return possibility_list

