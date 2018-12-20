import os
import csv
from enum import Enum, IntEnum
from datetime import datetime
import matplotlib.pyplot as plt

class Gender(Enum):
    """
    Describes the possible genders in the data set
    """
    MALE = 'männlich'
    FEMALE = 'weiblich'
    GENEREL = 'Allgemein'

class Entry(IntEnum):
    """
    Describes records from the Genesis (https://www-genesis.destatis.de/) table 12211-0001
    """
    GENDER               = 0
    DATE                 = 1
    EMPLOYED             = 2
    UNEMPLODED           = 3
    WORKING_POPULATION   = 4
    DEPENDANT_POPULATION = 5

def load_statistics(filename):
    """
    Loads statistics as specified in the entry format
    """
    stats = {} 

    with open(os.path.join(os.getcwd(), filename)) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            #print(row)
            if not row[Entry.DATE]:
                continue

            date = None
            if '/' in row[Entry.DATE]:
                date = datetime.strptime(row[Entry.DATE], '%m/%Y')
            else:
                date = datetime.strptime(row[Entry.DATE], '%Y')

            row.pop(Entry.DATE) # remove duplicate data. NOTE: From now on you must use Entry.FEATURE - 1 as the index
            if date in stats:
                stats[date].append(row)
            else:
                stats[date] = [row]

    return stats

# Gather data
stats = load_statistics('12211-0001.csv')
years = stats.keys()

male_employed_per_year, female_employed_per_year, general_employed_per_year = [], [], []

for year in years:
    for e in stats[year]:
        if e[Entry.GENDER] == Gender.MALE.value:
            male_employed_per_year.append(int(e[Entry.EMPLOYED - 1]))
        elif e[Entry.GENDER] == Gender.FEMALE.value:
            female_employed_per_year.append(int(e[Entry.EMPLOYED - 1]))
        #else:
        #    general_employed_per_year.append(int(e[Entry.EMPLOYED - 1]))

# Plot this
plt.scatter(years, male_employed_per_year, label='Male employed', c='b')
plt.scatter(years, female_employed_per_year, label='Female employed', c='r')
#plt.scatter(years, general_employed_per_year, label='General employed', c='c')
plt.xlabel('date')
plt.ylabel('employed')
plt.legend()
plt.show()
