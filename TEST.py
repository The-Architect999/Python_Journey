# The Architect's Dictionary Drill

tactics = {
    "Mirroring": 0,
    "Victim Card": 0,
    "Silence": 0
}

while True:
    print("\nCurrent Intel:", tactics)
    action = input("Enter tactic observed (or 'exit' to quit): ")
    
    if action == "exit":
        print("Session Closed. Final Data:", tactics)
        break
    
    if action in tactics:
        tactics[action] = tactics[action] + 1
        print(f"Recorded. {action} count is now: {tactics[action]}")
    else:
        print("Unknown tactic. Stay alert.")