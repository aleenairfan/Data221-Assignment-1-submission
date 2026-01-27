# Pandas DataFrame with Computed Column

import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

dataFrame = pd.DataFrame(data)

# New column derived from existing columns
dataFrame["D"] = dataFrame["A"] * dataFrame["B"] + dataFrame["C"]

print(dataFrame)
