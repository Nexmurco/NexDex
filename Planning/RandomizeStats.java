int bst = bst() - 70;

// Make weightings
double hpW = random.nextDouble(), atkW = random.nextDouble(), defW = random.nextDouble();
double spaW = random.nextDouble(), spdW = random.nextDouble(), speW = random.nextDouble();

double totW = hpW + atkW + defW + spaW + spdW + speW;

hp = (int) Math.max(1, Math.round(hpW / totW * bst)) + 20;
attack = (int) Math.max(1, Math.round(atkW / totW * bst)) + 10;
defense = (int) Math.max(1, Math.round(defW / totW * bst)) + 10;
spatk = (int) Math.max(1, Math.round(spaW / totW * bst)) + 10;
spdef = (int) Math.max(1, Math.round(spdW / totW * bst)) + 10;
speed = (int) Math.max(1, Math.round(speW / totW * bst)) + 10;

/*
nextdouble returns a uniformly random value between 0 and 1

the random stat value is then normalized against the other values and scaled to the bst

example

Lets give this pokemon a bst of 420 (like linoone)
we scale down to allow for minimums, so the new bst is 350

generate random numbers for each stat
hp .83
attack .40
defense .22
spatk .25
spdef .88
speed .65

total = 3.23


Scale the values

hp = (83/323) * 350 = 89. -> 89
atk = 43
def = 23
spatk = 27
spdef = 95
speed = 70

then add back in the original subtracted values

hp = 109
atk = 53
def = 33
spatk = 37
spdef = 105
speed = 80

so our new bst is 417 vs 420, with some value lost due to rounding