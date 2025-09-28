# "https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki"
# "https://pypi.org/"

from prettytable import PrettyTable
table = PrettyTable()

# we can add the table column-wise
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Pokemon Type", ["Electric", "Water", "Fire", "Grass"])

# default alignment is center
print(table)

# for left alignment
table.align = "l"
print(table)

# for right alignment
table.align = "r"
print(table)
