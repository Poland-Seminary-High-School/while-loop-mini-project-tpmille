print("Welcome to your vacation planner!")
spots = []
while True:
    spot = input("enter your vacation spot( type done when finished.): ")
    if spot== "done":
        break
    spots.append(spot)
    print(f"{spot.lower()} Has been added.")