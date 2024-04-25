service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_new_ticket(ticket_id, customer, issue):
    service_tickets[ticket_id] = {"customer": customer, "issue": issue, "status": "open"}

def modify_ticket(ticket_id, blah, new_value):
    
    service_tickets[ticket_id][blah] = new_value      
   
       

def show():
    for ticket_id, ticket_info in service_tickets.items():
        print(f"Ticket ID: {ticket_id}")                       
        for key, value in ticket_info.items():
            print(f"{key}: {value}")
        print()


open_new_ticket("Ticket003", "charlie", "website not loading")
modify_ticket("Ticket001", "status", "solved it")
show()
