from datetime import datetime

class StarCinema:
    _hall_list = []

    def add_hall(self, hall_obj):
        self._hall_list.append(hall_obj)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.seats()
        StarCinema().add_hall(self)

    def seats(self):
        seats = [['free' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[self._hall_no] = seats

    def add_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, id, seat_list):
        seats = self._seats.get(id)
        if seats is None:
            print("Invalid show ID.")
            return

        for seat in seat_list:
            row, col = seat
            if 0 <= row < self._rows and 0 <= col < self._cols:
                if seats[row][col] == 'free':
                    seats[row][col] = 'booked'
                    print(f"Seat {row}-{col} booked successfully.")
                else:
                    print(f"Seat {row}-{col} is already booked.")
            else:
                print(f"Seat {row}-{col} is invalid.")

    def view_available_seats(self, id):
        seats = self._seats.get(id)
        if seats is None:
            print("Invalid show ID.")
            return

        print("Available seats for show:")
        for i in range(self._rows):
            for j in range(self._cols):
                if seats[i][j] == 'free':
                    print("O", end=" ")
                else:
                    print("1", end=" ")
            print()

    def view_show_list(self):
        print("Running Shows:")
        for show_info in self._show_list:
            print(show_info)


def main():
    print("\n\n\n")
    print("*****************************************")
    print("*                                       *")
    print("*        WELCOME TO STATR CINEMA        *")
    print("*                                       *")
    print("*****************************************")

    rows = 10
    cols = 10
    hall_no = "1"
    hall = Hall(rows, cols, hall_no)

    hall.add_show(id="1", movie_name="Dune", time="2024-04-30 18:00")
    hall.add_show(id="2", movie_name="Inception", time="2024-04-30 21:00")

    while True:
        print("\nOptions:")
        print("1. VIEW SHOWS TODAY")
        print("2. VIEW AVAILBLE TICKETS")
        print("3. BOOKING TICKETS")
        print("4. EXIT")
        choice = input("Enter your Option: ")

        if choice == '1':
            hall.view_show_list()
        elif choice == '2':
            hall.view_show_list()
            id = input("Enter show ID to view available tickets: ")
            hall.view_available_seats(id)
        elif choice == '3':
            hall.view_show_list()
            id = input("Enter show ID to book tickets: ")
            hall.view_available_seats(id)
            row_col_str = input("Enter row and column (e.g., '0 1'): ")
            row, col = map(int, row_col_str.split())
            hall.book_seats(id, [(row, col)])
        elif choice == '4':
            print("Thank you for visiting Star Cinema.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
