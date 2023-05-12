# Problem D
# Secure Doors
def detect_anomalies():
    # Read the number of log entries
    n = int(input())

    # Set to keep track of people inside the building
    inside_building = set()

    # Process each log entry
    for _ in range(n):
        entry = input().split()
        action, name = entry[0], entry[1]

        # Check if the action is an entry
        if action == "entry":
            # Check if the person is already inside the building
            if name in inside_building:
                print(name, "entered (ANOMALY)")
            else:
                # Add the person to the inside_building set
                inside_building.add(name)
                print(name, "entered")
        else:
            # Check if the person is not supposed to be inside the building
            if name not in inside_building:
                print(name, "exited (ANOMALY)")
            else:
                # Remove the person from the inside_building set
                inside_building.remove(name)
                print(name, "exited")

detect_anomalies()
