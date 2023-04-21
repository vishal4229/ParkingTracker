"""
Design Parking Lot solution.
"""
class ParkingTracker:
    """
    Class Parking Tracker contains main logic for Parking vehicle and retriving the parked ones
    """
    def __init__(self):
        self.total_capacity = 40
        self.spaces = [None for i in range(1,40)]

    def park(self,vehicle_no):
        if None in self.spaces:
            available_spot = self.spaces.index(None)
            self.spaces[available_spot] = vehicle_no
            print(f"\nVehicle {vehicle_no} is parked at {available_spot}")
        else:
            print("\nNo Parking Space Available")
    
    def get_parking_spot(self,vehicle_no):
        if vehicle_no in self.spaces:
            parking_spot = self.spaces.index(vehicle_no)
            parking_level = "A" if parking_spot <=20 else "B"
            return {"level":parking_level,"spot":parking_spot+1}
        else:
            return None
    
def terminal_options():
    """
    Display options for terminal based window
    """
    print()
    print("*"*20)
    print("1. Park a vehicle\n")
    print("2. Retrive the parked spot number\n")
    print("*"*20)
    print("\n")

def get_vehicle_number():
    vehicle_no = input("Enter Vehicle Number\n")
    return vehicle_no

def do_operation(choice,parking_lot):
    if choice == 1:
        vehicle_no = get_vehicle_number()
        parking_lot.park(vehicle_no)
    elif choice == 2:
        vehicle_no = get_vehicle_number()
        spot_data = parking_lot.get_parking_spot(vehicle_no)
        print()
        print(spot_data if spot_data else "No Vehicle with given")

if __name__ == "__main__":
    parking_lot = ParkingTracker()
    while True:
        terminal_options()
        user_input = int(input("Please Enter Your Choice\n"))
        if user_input in [1,2,3]:
            do_operation(user_input,parking_lot)
        else:
            print("Invalid Choice, Please Enter Again\n")
        

