import pandas as pd

class CarPoolSystem:
    def __init__(self, excel_file):
        self.data = pd.read_excel(excel_file)

    def add_person(self, serial_number, pickup, drop, plate, contact, gender, count, age, trip_fare, avg_trip_hrs, trips_per_day,
                   trips_per_week, same_route_since, driver_rating, car_type):
        self.data = self.data.append({
            'sl_no': serial_number,
            'pickup_location': pickup,
            'dropoff_location': drop,
            'number_plate': plate,
            'Contact': contact,
            'Gender': gender,
            'passenger_count': count,
            'age_of_user': age,
            'trip_fare': trip_fare,
            'avg_trip_hrs': avg_trip_hrs,
            'trips_per_day': trips_per_day,
            'trips_per_week': trips_per_week,
            'same_route_since': same_route_since,
            'driver_rating': driver_rating,
            'car_type': car_type
        }, ignore_index=True)

    def find_carpool_match(self, pickup, drop):
        matches = self.data[(self.data['pickup_location'] == pickup) & (self.data['dropoff_location'] == drop)]
        return matches

    def suggest_carpool(self, pickup, drop):
        matches = self.find_carpool_match(pickup, drop)
        if not matches.empty:
            print("Possible carpool matches:")
            print(matches[["sl_no", 'pickup_location', 'dropoff_location', 'passenger_count']])
            chosen_serial = int(input("Enter the serial number of the carpool you want more details about: "))
            self.show_carpool_details(chosen_serial)

        else:
            print("No carpool matches found.")

    def show_carpool_details(self, serial_number):
        carpool = self.data[self.data['sl_no'] == serial_number]
        if not carpool.empty:
            print("\nCarpool Details:")
            carpool.loc[:, ['trip_fare', 'avg_trip_hrs', 'driver_rating']] = carpool.loc[:,
                                                                             ['trip_fare', 'avg_trip_hrs',
                                                                'driver_rating']].round(1)
            print(carpool[
                      ["pickup_location", "dropoff_location","age_of_user", "trip_fare",'avg_trip_hrs', "passenger_count", "Gender", "trips_per_day",
                       "trips_per_week",'same_route_since','driver_rating','car_type']])
        else:
            print("Invalid serial number. Carpool not found.")


excel_file = r'C:\RVCE(2023-27)\main_dataset.xlsx'
car_pool_system = CarPoolSystem(excel_file)

pickup = input("Enter pickup location: ").title()
drop = input("Enter drop location: ").title()
car_pool_system.suggest_carpool(pickup, drop)
