# Create  list with cities.
# Create a dictionary for cities with their flight costs.
# Create a dictionary for hotel daily cost for each city.
# Create a dictionary for car rental costs for each city.
# Request user to enter the name of the city they will be flying to.
# Request user to enter number of nights they will be staying at a hotel.
# Request user to enter the number of days they will be hiring a car for.
# Create a function that will calculate the total cost for hotel stay
# given the city.
# Create a function that will calculate flight cost given the city.
# Create a function that will calculate the total cost of renting
# a car given the city.
# Create a function that will calculate total cost of holiday.


cities = ["cape town", "durban", "johannesburg",
          " port alfred", "east london"]

city_flight_cost = {"cape town": 2000,
                    "durban": 1500,
                    "johannesburg": 1800,
                    "port alfred": 1200,
                    "east london": 999
                    }


hotel_daily_cost = {"cape town": 3200,
                    "durban": 1200,
                    "johannesburg": 1100,
                    "port alfred": 1650,
                    "east london": 1100
                    }

car_rental_cost = {"cape town": 242,
                   "durban": 247,
                   "johannesburg": 370,
                   "port alfred": 499,
                   "east london": 279
                   }

city_flight = input("Enter the city you will be flying to between Cape Town,"
                    " Durban, Johannesburg,"
                    " Port Alfred and East London:").lower()

num_nights = int(input("Enter number of nights"
                       " you will be staying at the hotel:"))

rental_days = int(input("Enter number of days you will be hiring a car for:"))

print()
def hotel_cost(num_nights):

    if city_flight in cities:

        total_hotel_cost = num_nights * hotel_daily_cost[city_flight]

        return total_hotel_cost

    else:

        print("City not found")

        return 0

def plane_cost(city_flight):

    if city_flight in cities:

        total_plane_cost = city_flight_cost[city_flight]

        return total_plane_cost

    else:

        return 0

def car_rental(rental_days):

    if city_flight in cities:

        total_rental_cost = rental_days * car_rental_cost[city_flight]

        return total_rental_cost

    else:

        return 0

def holiday_cost(hotel_cost, plane_cost, car_rental):

    total_holiday_cost = hotel_cost + plane_cost + car_rental

    print(f"Total hotel cost is R{total_hotel_cost}\n")

    print(f"Total plane cost is R{total_plane_cost}\n")

    print(f"Total car rental cost is R{total_rental_cost}\n")

    print(f"Total holiday costs are R{total_holiday_cost}")

total_hotel_cost = hotel_cost(num_nights)
total_plane_cost = plane_cost(city_flight)
total_rental_cost = car_rental(rental_days)

holiday_cost(total_hotel_cost, total_plane_cost, total_rental_cost)