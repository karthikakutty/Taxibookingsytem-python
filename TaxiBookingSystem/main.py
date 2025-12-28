import math
import uuid
from platform import system


class User:
    def __init__(self,name):
        self.user_id=str(uuid.uuid4())
        self.name=name
class Driver:
    def __init__(self,name,x,y):
        self.driver_id=str(uuid.uuid4())
        self.name=name
        self.x=x
        self.y=y
        self.available=True

class TaxiBookingSystem:
    def __init__(self):
        self.user={}
        self.driver={}
        self.trips=[]

    def add_user(self,name):
        user=User(name)
        self.user[user.user_id]=user
        return user.user_id

    def add_driver(self,name,x,y):
        driver=Driver(name,x,y)
        self.driver[driver.driver_id]=driver
        return

    def calculate_distance(self,x1,y1,x2,y2):
        return math.sqrt((x1-x2)**2 +(y1-y2)**2)

    def find_nearest_driver(self,x,y):
        nearest_driver=None
        min_dist=float('inf')
        for d in self.driver.values():
            if d.available:
                dist=self.calculate_distance(x,y,d.x,d.y)
                if dist<min_dist:
                    min_dist=dist
                    nearest_driver=d
        return nearest_driver, min_dist

    def request_ride(self,user_id,x,y,dest_x,dest_y):
        driver,dist=self.find_nearest_driver(x,y)
        if not driver:
            return "No drivers available!"
        driver.available=False
        trip={
            "trip_id":str(uuid.uuid4()),
            "user_id":user_id,
            "driver_id":driver.driver_id,
            "distance":dist,
            "fare":round(dist*10,2),
            "status":"ongoing"
        }
        self.trips.append(trip)
        return trip


    def complete_ride(self,trip_id):
        for trip in self.trips:
            if trip["trip_id"]==trip_id:
                trip["status"]="completed"
                self.driver[trip["driver_id"]].available=True
                return trip

        return "Trip not found!"

if __name__=="__main__":
    system=TaxiBookingSystem()
    u1=system.add_user("arun")
    d1=system.add_driver("Driver A",2,1)
    d2=system.add_driver("Driver b",4,3)
    trip=system.request_ride(u1,0,0,10,10)
    completed=system.complete_ride(trip["trip_id"])

    print('ride completed',completed)
print("\n🚕 Ride Completed!")
print(f"Driver ID  : {completed['driver_id']}")
print(f"User ID    : {completed['user_id']}")
print(f"Distance   : {completed['distance']:.2f} km")
print(f"Fare       : ₹{completed['fare']:.2f}")
print(f"Status     : {completed['status'].capitalize()}")
