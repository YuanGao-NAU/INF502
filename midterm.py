import csv

class ant_bait:
    def __init__(self, month, year, plot, stake, species, abundance):
        self.month = month
        self.year = year
        self.plot = plot
        self.stake = stake
        self.species = species
        self.abundance = abundance
        self.species_code = species

    def __str__(self):
        return self.species + " - " + self.month + ", " + self.year + ": " + self.abundance

    def replace_attribute(self, species):
        self.species = species

class ant_species:
    def __init__(self, species_code, genus, alt_genus, species, alt_species, tribe, sub_family, Dissues):
        self.species_code = species_code
        self.genus = genus
        self.alt_genus = alt_genus
        self.species = species
        self.alt_species = alt_species
        self.tribe = tribe
        self.sub_family = sub_family
        self.Dissues = Dissues
    
    def __str__(self):
        return self.genus + " " + self.species

def read_ant_bait(filename):
    ant_bait_list = []
    fd = open(filename, 'r')
    reader = csv.reader(fd)
    for line in reader:
        ant_bait1 = ant_bait(line[0], line[1], line[2], line[3], line[4], line[5])
        ant_bait_list.append(ant_bait1)
        print(line)
    ant_bait_list = ant_bait_list[1:]
    return ant_bait_list

def read_ant_species(filename):
    ant_species_list = []
    fd = open(filename, 'r')
    reader = csv.reader(fd)
    for line in reader:
        ant_species1 = ant_species(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
        #print(ant_species1)
        ant_species_list.append(ant_species1)
    ant_species_list = ant_species_list[1:]
    return ant_species_list

def replace_species(ant_bait_list, ant_species_list):
    for item1 in ant_bait_list:
        for item2 in ant_species_list:
            if item1.species == item2.species_code:
                item1.replace_attribute(item2.species)

def aver_of_certain_species(ant_bait_list, species_code):
    total = 0
    cnt = 0
    average = 0
    for item in ant_bait_list:
        if item.species_code == species_code:
            cnt = cnt + 1
            total = total + int(item.abundance)
    try:
        average = total / cnt
    except ZeroDivisionError:
        print("devided by zero, no assigned species abundance found!")
        return -1
    else:
        return average

if __name__ == "__main__":
    list0 = read_ant_bait("./ant_bait.csv")
    list1 = read_ant_species("./ant_species.csv")
    #for item in list0:
        #print(item)
    replace_species(list0, list1)
    print("------------------------------------------------------------------------------")
    #for item in list0:
        #print(item)
    av = aver_of_certain_species(list0, "cono bico")
    print(av)