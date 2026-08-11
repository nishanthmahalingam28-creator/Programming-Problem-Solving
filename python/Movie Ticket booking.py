import csv
from datetime import datetime
import os

try:

    class Movie:

        def loc(self):
            Place = ['Chennai', 'Namakkal', 'Erode', 'Tiruchengode', 'Velur']

            print("==========Location==========")
            for i in Place:
                print(i)

            self.location = input("Choose Location: ")

            if self.location in Place:
                print("")
            else:
                print("Choose Valid location")

        def movie_selection(self):
            Tamil = ['Leo', 'Ghilli', 'Coolie', 'Goat']
            Hindi = ['Dark', 'Con city', 'Alpha', 'Colony']
            Telugu = ['Habeebi', 'Governor', 'Game changer', 'Spider man']
            print("==========Language==========")
            Available_language=['Tamil','Hindi','Telugu']
            for i in Available_language:
                print(i,"\n")
                
            Language = input("Choose language: ")
            self.language = Language.capitalize()

            if self.language == 'Tamil':
                movie = Tamil

            elif self.language == 'Hindi':
                movie = Hindi

            elif self.language == 'Telugu':
                movie = Telugu

            else:
                print("Choose Tamil or Hindi or Telugu")
                return

            print("========Movie list========")
            for i in movie:
                print(i)
            print("=====================================")
            select_movie = input("Movie: ")

            if select_movie in movie:
                self.movie = select_movie
                print("")
            else:
                print("Choose movie from the above list")
                return

        def ticket_booking(self):
            print("=====================================")
            ticket = input("Are you booking ticket (yes or no): ")

            if ticket == 'yes':

                print("Total number of seats in theatre: 20")

                seat = {
                    1:'0',2:'1',3:'1',4:'0',5:'1',
                    6:'0',7:'0',8:'1',9:'1',10:'0',
                    11:'0',12:'1',13:'1',14:'0',15:'0',
                    16:'1',17:'0',18:'1',19:'0',20:'1'
                }

                Available = 0
                seats_available = []

                for i, j in seat.items():

                    if j == '0':
                        Available += 1
                        seats_available.append(i)

                print("Number of seats available:", Available)

                no_of_ticket = int(input("How many number of tickets: "))

                if no_of_ticket <= Available:

                    print("==========These Seats Are Available==========")

                    for i in seats_available:
                        print(i,"\t")

                    confirm_seats_csv = []

                    for j in range(no_of_ticket):

                        confirm_seats = int(input("Select the seat: "))
                        confirm_seats_csv.append(confirm_seats)
                        
                    price=no_of_ticket *200

                    print("Ticket Price is Rs.200 per seat")

                    print("Total_ticket price:",price)

                    choice = input("Confirm to book seats (yes or no): ")

                    if choice == 'yes':

                        name = input("Name: ")
                        

                        with open("Movie_ticket_data.csv", "a", newline="") as file:

                            writer = csv.writer(file)

                            if os.path.getsize("Movie_ticket_data.csv") == 0:
                                writer.writerow(["Name", "Location", "Language", "Movie", "Seat","Price"])

                            writer.writerow([
                                name,
                                self.location,
                                self.language,
                                self.movie,
                                confirm_seats_csv,
                                price
                            ])

                        print("Ticket Booked Successfully")

                    else:
                        print("Visit Again Later")

                else:
                    print("Seats not available")

            else:
                print("Visit Again Later")

    m1 = Movie()
    m1.loc()
    m1.movie_selection()
    m1.ticket_booking()

except ValueError:
    print("Error: Give valid input")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("===============================================")
    print("Thank you")
    print(datetime.now())
    print("===============================================")
