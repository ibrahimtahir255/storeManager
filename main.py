from simulation import *
from my_priorityq import *

def simulation():
  
  cashiers = 2
  total_time = 3000
  interarrival_time = 8
  cash_time = 14
  

  # cashiers = 1
  # total_time = 5
  # interarrival_time = 1
  # cash_time = 2

  # cashiers = 2
  # total_time = 30
  # interarrival_time = 2
  # cash_time = 5

  # cashiers = 2
  # total_time = 1000
  # interarrival_time = 2
  # cash_time = 14
  
  store_sim = StoreSimulation( cashiers, cash_time, \
                              interarrival_time, total_time)

  print( 'Simulation starts ...' )
  store_sim.run()
  store_sim.print_results()
  print( 'Simulation ends ...' )


def test_priority_queue():
  pq = PriorityQueue()
  # continue to do incremental testing
  # of your priority queue
  
  items = {'white':0, 'red':3, 'green':1, 'blue':1, \
         'yellow':5, 'black':1, 'brown':2, 'cyan':5, 'purple':4}
  #white green blue black brown red purple yellow cyan 
  
  size = len( items )
  # print(size)
  # pq = PriorityQueue()
  priority_level = 10  # this parameter makes the API consistent, change as needed
  print( 'test enqueue() ...' )
#for color in items:
  for color in items:
    p = items[color]
    print( 'enqueue item : ', color )
    # priority = color
    priority = p % priority_level
    pq.enqueue( color, priority )   # using color as a priority scheme
  print()
  print(pq)
  

  print( 'queue length : ', len (pq) )

  print( 'test peek() : ', pq.peek() )

  print( 'test dequeue() : remove first ...',  pq.dequeue() )

  print( 'test dequeue() : remove second ...', pq.dequeue() )

  print( 'test is_empty() : ', pq.is_empty() )

  print( 'test peek() : ', pq.peek() )

  print( 'test enqueue( purple ) : ' )
  pq.enqueue( 'purple', items['purple'] % priority_level )

  while pq.is_empty() == False:
    color = pq.dequeue()
    print( 'color : ', color )
    
  print( 'test is_empty() : ', pq.is_empty() )

  print( 'queue length : ', len ( pq ) )


# add any additional incremental testing

####### COMMENT OUT WHICH METHOD YOU'D LIKE TO RUN ####
simulation()
# test_priority_queue()