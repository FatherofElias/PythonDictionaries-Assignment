#  Question 2
#  Task 1


def enter_new_ticket():
    """Enter a new service ticket."""
    ticket_id = input("Enter the ticket ID: ")
    customer = input("Enter the customer name: ")
    issue = input("Enter the issue description: ")
    open_ticket(ticket_id, customer, issue)

def open_ticket(ticket_id, customer, issue):
    """Open a new service ticket."""
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

def update_ticket_status(ticket_id, status):
    """Update the status of an existing ticket."""
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
    else:
        print(f"Ticket {ticket_id} does not exist.")

def display_tickets(status=None):
    """Display all tickets or filter by status."""
    for ticket_id, ticket_info in service_tickets.items():
        if status:
            if ticket_info["Status"] == status:
                print(f"{ticket_id}: {ticket_info}")
        else:
            print(f"{ticket_id}: {ticket_info}")

# Initialize with some sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Test the functions
enter_new_ticket()
open_ticket("Ticket003", "Charlie", "Account locked")
update_ticket_status("Ticket001", "closed")
display_tickets()