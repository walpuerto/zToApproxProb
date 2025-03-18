# Z-score to Approximate Probability
# Version 0.1
# By noob_undone

def isValidFloat(value):
    try: float(value)
    except: return False
    else: return True

import precomputed

def main():
    zScore = input("Enter the z-score: ")
    if isValidFloat(zScore):
        zScore = float(zScore)

        print(f"Probability of z-score {zScore} is: {precomputed.getProbabilityFromZ(zScore)}")

    else:
        print(f"{zScore} is not a valid input.")

main()