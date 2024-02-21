import Events as Events
import Schedular as Schedular

import random

class Simulator:
    def __init__(self):
        self.schedular = Schedular()
        self.generate_events(100)
        
    def generate_events(self,num_events):
        
        # lambda_arrival = 1.0  # Rate parameter for arrival times, mean = 1/lambda
        # lambda_departure = 0.5  # Rate parameter for departure times, mean = 1/lambda

        for i in num_events:
            random.seed(os.urandom(10))
            # Generate an exponential arrival time
            arrival_time = random.expovariate(random.randint(1, 10))
            # Generate an exponential departure time
            dep_time = random.expovariate(random.randint(1, 10))
            
            print(f"Iteration {i}, Arrival Time: {arrival_time:.2f}, Departure Time: {departure_time:.2f}")
            # Small sleep to ensure the time-based seed changes between iterations
            time.sleep(0.1)
            
            _event = Events(arrival_time,dep_time)
            self.schedular.schedule_event(_event)
            
            
            
          