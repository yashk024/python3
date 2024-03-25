import matplotlib.pyplot as plt
from matplotlib import style

# style.use("ggplot")
style.use("dark_background")

# link: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes, labels=people)
plt.show()
