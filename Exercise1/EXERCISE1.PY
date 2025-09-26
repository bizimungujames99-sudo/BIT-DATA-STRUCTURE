# Cinema Ticket Counter Data Handling Example

# 1. Integers: Quantities of tickets sold at different counters/windows
tickets_sold = [45, 30, 60, 80, 25]  # Example ticket counts at 5 counters

total_tickets = sum(tickets_sold)
average_tickets = total_tickets / len(tickets_sold)
min_tickets = min(tickets_sold)
max_tickets = max(tickets_sold)

# 2. Strings: Formatted report with f-strings
report = (
    f"--- Cinema Ticket Counter Report ---\n"
    f"Total Tickets Sold: {total_tickets}\n"
    f"Average Tickets per Counter: {average_tickets:.2f}\n"
    f"Minimum Tickets Sold at a Counter: {min_tickets}\n"
    f"Maximum Tickets Sold at a Counter: {max_tickets}\n"
)
print(report)

# 3. Booleans: Apply a threshold and compound boolean condition
threshold = 50
if average_tickets > threshold and max_tickets > 70:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# 4. Lists: Maintain and manipulate a list of ticket records
ticket_counters = ["Counter A", "Counter B", "Counter C", "Counter D", "Counter E"]
print("Original list of counters:", ticket_counters)

# Add a new counter
ticket_counters.append("Counter F")
# Remove a counter if its tickets sold are below 30
for i, tickets in enumerate(tickets_sold):
    if tickets < 30:
        removed_counter = ticket_counters.pop(i)
        print(f"Removed {removed_counter} due to low sales ({tickets} tickets).")
        break

# Sort and display before and after
print("Sorted counters:", sorted(ticket_counters))
print("Modified list of counters:", ticket_counters)

# 5. Arrays: Use array module for fixed-size numeric storage
import array
ticket_array = array.array('i', tickets_sold[:4])  # Take first 4 counters for example
array_sum = sum(ticket_array)
print("Sum using array module:", array_sum)
print("Sum using list (first 4 counters):", sum(tickets_sold[:4]))

# 6. Dictionaries: List of ticket sales records
ticket_records = [
    {"id": 1, "name": "Alice", "value": 45},
    {"id": 2, "name": "Bob", "value": 30},
    {"id": 3, "name": "Carol", "value": 60},
    {"id": 4, "name": "Dave", "value": 80},
]

# Update a record (e.g., Bob sold 35 instead of 30)
for record in ticket_records:
    if record["name"] == "Bob":
        record["value"] = 35

# Delete another record (remove Carol)
ticket_records = [rec for rec in ticket_records if rec["name"] != "Carol"]

# Compute total sales from records
total_from_records = sum(rec["value"] for rec in ticket_records)
print("Updated ticket records:", ticket_records)
print(f"Total tickets from records: {total_from_records}")

# Output: (All print statements will show intermediate and final results)