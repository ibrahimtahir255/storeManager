"""Implementation of the main simulation class."""
from my_array import Array
from normal_q import Queue
from my_priorityq import PriorityQueue
from sim_people import Customer, Cashier

import random

"""This class simulates the operation of a store where a number
of cashiers to serve customers arriving  in a random 
fashion. The customers arrive at a common waiting queue for a group
of cashiers. If a cashier is free, the newly arrived customer receives 
the service immediately. If no cashier is availabe, the customer
waits in the queue for the next available cashier. When a customer
finishes the service at the cashier, with a probability, the customer
goes to the gift-wraper to receive a further service.
"""

class StoreSimulation :
    ''' Class Attributes:
        - debug; boolean; use to create debug print statements
        - max_service_time; int; maximum time to serve one customer
        - total_sim_time; int; number of steps in simulation
        - max_interarrival_time; int; maximum time between customer arrivals
        - waiting; Queue of Customers; for customers who are waiting for cashier
        - cashiers; Array of Cashiers; 
        - events; PriorityQueue of Events, prioritized by time
        - clock; int; current time in the simulation
        - total_wait_time; int; sum of time each customer waited between arriving and beginning service
        - customer_count; total number of customers that have arrived
        - service_gen; random number generator for service times
        - arrival_gen; random number generator for arrival times
  '''
    def __init__( self, num_cashier, serv_time, \
                interarrival_time, total_sim_time ):
        """Create a simulation object.
        Parameters:
            num_cashier; int
            serv_time; int; maximum service time for a single customer
            interarrival_time; int; maximum time between two customer arrivals
            total_sim_time; int
        """
        # Debug state or not
        # self.debug = True
        self.debug = False

        # Time parameters supplied by the user.
        self.max_service_time = serv_time
        self.total_sim_time = total_sim_time
        self.max_interarrival_time = interarrival_time
        self.lastArrival = 0
            
        # Simulation components.
        self.waiting = Queue()   
        self.cashiers = Array( num_cashier )    
        for i in range( num_cashier ):
            self.cashiers[ i ] = Cashier( i)   # 'i' is the ID

        self.events = PriorityQueue()
        self.clock = 0

        # Computed during the simulation.
        self.total_wait_time = 0
        self.customer_count = 0

        # Random number generator, we define two separate random generators
        # so they don't share states.
        self.service_gen = random.Random()
        self.arrival_gen = random.Random()
        self.ids = 0 
    
    def run(self):
        self.schedule_next_arrival()
        while not self.events.is_empty() and self.clock < self.total_sim_time:
            event = self.events.dequeue()
            print("self.clock before: ", self.clock)
            print("event.time before: ", event.time)
            if self.clock < event.time:
                self.clock = event.time
            print("self.clock after: ", self.clock)
            print("event.time after: ", event.time)
            #if the clock is ahead of the total sim time, the simulation stops
            if self.clock >= self.total_sim_time:
                break
            if event.type == Event.ARRIVAL:
                self.process_arrival(event)
            elif event.type == Event.DEPARTURE:
                self.process_departure(event)
            if self.clock < self.total_sim_time:
                self.schedule_next_arrival()
        
    def schedule_next_arrival(self):
        #First event generation
        for index in range (1):
            arrival_time = self.arrival_gen.randint(self.lastArrival,self.lastArrival + self.max_interarrival_time)
            print("arrival time: ", arrival_time)
            if arrival_time < self.total_sim_time:
                self.events.enqueue(Event(0, Customer(self.ids), arrival_time), arrival_time)
                self.ids += 1
        self.lastArrival = arrival_time
      
    def process_arrival(self, event):

        # if self.clock < event.time :
        #     self.clock = event.time 
        # #if the clock is ahead of the total sim time, the simulation stops
        # if self.clock >= self.total_sim_time:
        #     return
        
        #Handling events
        print(f'Time {self.clock} : {event.type} ')
        if event.type == Event.ARRIVAL:
            print(f'\tTime {self.clock} : customer {event.who.id} arrived')
            available = False
            for cashier in self.cashiers:
                if cashier.status == True:
                    print(f'\tTime {self.clock} : customer {event.who.id} was served by cashier {cashier.id}')
                    cashier.status = False 
                    available = True
                    departure_event_time = self.service_gen.randint(event.time,event.time + self.max_service_time)
                    departure_event = Event(1,cashier,departure_event_time)
                    self.events.enqueue(departure_event,departure_event_time)
                    break
            
            if available == False:
                print(f'\tTime {self.clock} : customer {event.who.id} was put in line')
                timein = event.time
                self.waiting.enqueue([event.who,timein])
            self.customer_count += 1 

    def process_departure(self, event):
        print(f'\tTime {self.clock} : customer at cashier {event.who.id} left ')
        cashier = event.who
        if self.waiting.is_empty():
          cashier.status = True
        else:
          customer, timein = self.waiting.dequeue()
          self.total_wait_time += (self.clock-timein)
          print(f'\tTime {self.clock} : customer {customer.id} was served by cashier {cashier.id} : {(event.time-timein)} ')
          departure_event_time = self.service_gen.randint(self.clock,self.clock + self.max_service_time)
          departure_event = Event(1,cashier,departure_event_time)
          self.events.enqueue(departure_event,departure_event_time)
        
    
          
      

#   def run(self):
#     lastArrival = 0
      # First event generation
#     for index in range (1):
#       arrival_time = self.arrival_gen.randint(lastArrival,lastArrival + self.max_interarrival_time)
#       self.events.enqueue(Event(0, Customer(self.ids), arrival_time), arrival_time)
#       self.ids += 1
#       lastArrival = arrival_time
      
      # This is the main simulation loop
#     while self.events.is_empty()== False and self.clock < self.total_sim_time:
#       #arrival
#       p = self.events.dequeue()
#       if self.clock < p.time :
#         self.clock = p.time 
        # if the clock is ahead of the total sim time, the simulation stops
#       if self.clock >= self.total_sim_time:
#         break
        
        # Handling events
#       print(f'Time {self.clock} : {p.type} ')
#       if p.type == Event.ARRIVAL:
#         print(f'\tTime {self.clock} : customer {p.who.id} arrived')
#         available = False
#         for cashier in self.cashiers:
#           if cashier.status == True:
            
#             print(f'\tTime {self.clock} : customer {p.who.id} was served by cashier {cashier.id}')
#             cashier.status = False 
#             available = True
#             departure_event_time = self.service_gen.randint(p.time,p.time + self.max_service_time)
#             departure_event = Event(1,cashier,departure_event_time)
#             self.events.enqueue(departure_event,departure_event_time)
#             break
#         
#         if available == False:
#           print(f'\tTime {self.clock} : customer {p.who.id} was put in line')
#           timein = p.time
#           self.waiting.enqueue([p.who,timein])
#         self.customer_count += 1 

#       elif p.type == Event.DEPARTURE:
#         print(f'\tTime {self.clock} : customer at cashier {p.who.id} left ')
#         cashier = p.who
#         if self.waiting.is_empty():
#           cashier.status = True
#         else:
#           customer, timein = self.waiting.dequeue()
#           self.total_wait_time += (self.clock-timein)
#           print(f'\tTime {self.clock} : customer {customer.id} was served by cashier {cashier.id} : {(p.time-timein)} ')
#           departure_event_time = self.service_gen.randint(self.clock,self.clock + self.max_service_time)
#           departure_event = Event(1,cashier,departure_event_time)
#           self.events.enqueue(departure_event,departure_event_time)
#       arrival_time = self.arrival_gen.randint(lastArrival,lastArrival + self.max_interarrival_time)
#       if arrival_time < self.total_sim_time or True:
#         self.events.enqueue(Event(0, Customer(self.ids), arrival_time), arrival_time)
#         self.ids += 1
#         lastArrival = arrival_time
      

      
  
    def print_results( self ):
        """Print the simulation results."""
        print( '====== Simulation Statistics =======' )
        print( 'number of cashier : ', len( self.cashiers ) )

        print( 'totalSimTime: ', self.total_sim_time )
        print( 'max interarrival time: ', self.max_interarrival_time )
        print( 'cashier max service time: ', self.max_service_time )

        num_served = self.customer_count - len( self.waiting )
        avg_wait = float( self.total_wait_time ) / num_served
        print( "" )
        print( "Number of customers served = ", num_served )
        print( "Number of customers remaining in line = ",
            len(self.waiting) )
        print( "The average wait time was", avg_wait, "minutes.") 
        print( '=====================================' )


class Event:
    # These constants define the types of events
    ARRIVAL      = 0    # customer arrival
    DEPARTURE   = 1    # cashier ending
    #Serve = 2 
    SYSTEM_UPDATE = 2

    '''
    Class attributes:
        time; int; the time step the event occurs
        type; int constant (see below); identifies the event
        who; Customer; customer the event serves
    '''
    
    def __init__(self, event_type, person, time, details=None):
        '''
        Parameters:
            time; int; the time step the event occurs
            type; int constant (see below); identifies the event
            person; StorePerson; 
        '''
        self.time = time
        self.type = event_type
        self.who = person
        self.details = details

        def __str__(self):
            return f"Event(type={self.type}, time={self.time}, details={self.details})"


