import os
import csv
from enum import IntEnum
from datetime import datetime
import matplotlib.pyplot as plt

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

            stats[date] = row[Entry.EMPLOYED]

    return stats

# Plot this
stats = load_statistics('12211-0001.csv')
plt.plot(stats.keys(), stats.values())
plt.xlabel('date')
plt.ylabel('employed')
plt.show()
