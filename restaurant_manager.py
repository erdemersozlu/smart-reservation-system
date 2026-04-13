"""
Smart Restaurant Reservation System
A portfolio project demonstrating file handling, resource allocation, 
and basic algorithmic logic in Python.
"""

def read_table_config(filename):
    tables = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Expecting format: TableID Capacity (e.g., T1 4)
                parts = line.split()
                if len(parts) == 2:
                    table_id, capacity = parts
                    tables[table_id] = int(capacity)
    except FileNotFoundError:
        print(f"Critical Error: {filename} not found.")
    return tables

def run_simulation(tables_file, bookings_file):
    table_capacities = read_table_config(tables_file)
    occupancy = {tid: None for tid in table_capacities}
    
    try:
        with open(bookings_file, 'r') as file:
            for line in file:
                parts = line.split()
                if not parts:
                    continue
                
                command = parts[0] 
                customer = parts[1]
                
                if command == "RES":
                    group_size = int(parts[2])
                    assigned = False
                    
                   
                    for tid, capacity in table_capacities.items():
                        if occupancy[tid] is None and capacity >= group_size:
                            occupancy[tid] = customer
                            print(f"[SUCCESS] {customer} (Party of {group_size}) -> {tid}")
                            assigned = True
                            break
                    
                    if not assigned:
                        print(f"[FAILED]  No table available for {customer} (Size: {group_size})")
                
                elif command == "CANCEL":
                    found = False
                    for tid, guest in occupancy.items():
                        if guest == customer:
                            occupancy[tid] = None
                            print(f"[CANCEL]  Reservation for {customer} released from {tid}")
                            found = True
                            break
                    if not found:
                        print(f"[ERROR]   No active booking found for {customer}")
                            
    except Exception as error:
        print(f"Runtime Error: {error}")

    return occupancy

def display_final_report(final_state):
    print("\n" + "="*40)
    print(f"{'TABLE':<10} | {'STATUS':<25}")
    print("-" * 40)
    for tid, guest in final_state.items():
        status = f"Occupied by {guest}" if guest else "AVAILABLE"
        print(f"{tid:<10} | {status:<25}")
    print("="*40)

if __name__ == "__main__":
    final_occupancy = run_simulation('tables.txt', 'reservations.txt')
    display_final_report(final_occupancy)
