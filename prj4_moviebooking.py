def createseats(rows, cols):
    seat_no = 1
    seating_chart = []
    for row in range(rows):
        current_row = []
        for col in range(cols):
            current_row.append(f's{seat_no}')
            seat_no += 1
        seating_chart.append(current_row)
    return seating_chart

def printseats(seat):
    print("=" * 30)
    for row in seat:
        print(" | ".join(row))
    print("=" * 30)
    print()

def select_seat(seating_chart, row, col, name, theater_name, data):
    if seating_chart[row][col].startswith('s'):
        seat_no = seating_chart[row][col]
        seating_chart[row][col] = 'X'
        data.append((theater_name, name, seat_no))
        print(f"\n{'*' * 30}")
        print(f"{seat_no} has been successfully booked to {name}.")
        print(f"{'*' * 30}\n")
    else:
        print(f"\n{'!' * 30}")
        print(f"Seat at row {row + 1}, column {col + 1} is already taken.")
        print(f"{'!' * 30}\n")

Ram = createseats(5, 5)
Muthuram = createseats(6, 6)
Data = []
while True:
    user=input("Viewer / Owner: ").lower()
    if user=="viewer":
        theatrename = input("Select theater: 1. Ram Cinemas 2. Grand Muthuram: ").lower()
        if theatrename == 'ram':
            theater_name = 'Ram'
            print(f"\n{'=' * 30}")
            print("Welcome to Ram Cinemas")
            print(f"{'=' * 30}\n")
            printseats(Ram)
            while True:
                row = int(input("Select the row (1 to 5): "))-1
                col = int(input("Select the column (1 to 5): "))-1
                if row >= 5 or col >= 5 or row < 0 or col < 0:
                    print(f"\n{'!' * 30}")
                    print("Invalid Selection")
                    print(f"{'!' * 30}\n")
                else:
                    name = input("Enter your name: ")
                    select_seat(Ram, row, col, name, theater_name, Data)
                    printseats(Ram)
                continue_booking = input("Do you want to book another seat? (yes/no): ").lower()
                if continue_booking != 'yes':
                    break

        elif theatrename == 'muthuram':
            theater_name = 'Muthuram'
            print(f"\n{'=' * 30}")
            print("Welcome to Grand Muthuram")
            print(f"{'=' * 30}\n")
            printseats(Muthuram)
            while True:
                row = int(input("Select the row (1 to 6): "))
                col = int(input("Select the column (1 to 6): "))
                if row >= 6 or col >= 6 or row < 0 or col < 0:
                    print(f"\n{'!' * 30}")
                    print("Invalid Selection")
                    print(f"{'!' * 30}\n")
                else:
                    name = input("Enter your name: ")
                    select_seat(Muthuram, row, col, name, theater_name, Data)
                    printseats(Muthuram)
                continue_booking = input("Do you want to book another seat? (yes/no): ").lower()
                if continue_booking != 'yes':
                    break

    if user=="owner":
        print(f"\n{'=' * 30}")
        print("All Bookings:")
        print(f"{'=' * 30}\n")
        for booking in Data:
            print(f"Theater: {booking[0]}, Name: {booking[1]}, SeatNumber: {booking[2]}")
        print(f"\n{'=' * 30}\n")
