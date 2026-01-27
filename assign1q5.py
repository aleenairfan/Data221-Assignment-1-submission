# Circle Area Comparison with Validation

import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # Validate inputs
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Both radii must be positive integers."

    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Both radii must be positive integers."

    # Compute areas
    areaCircle1 = math.pi * radiusOfCircle1 ** 2
    areaCircle2 = math.pi * radiusOfCircle2 ** 2

    # Determine smaller and larger areas
    smallerArea = min(areaCircle1, areaCircle2)
    largerArea = max(areaCircle1, areaCircle2)

    # Percentage coverage
    coveragePercentage = (smallerArea / largerArea) * 100

    return coveragePercentage

print(circleAreaCoverage(3, 5))
