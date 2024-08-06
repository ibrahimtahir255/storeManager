import unittest
from simulation import *

class TestStoreSimulation(unittest.TestCase):
    def test_process_arrival(self):
        random.seed(62)
        simulation = StoreSimulation(num_cashier= 1, serv_time= 10, interarrival_time= 5, total_sim_time= 50)
        simulation.run()
        expected_customers = simulation.customer_count
        self.assertTrue(simulation.events.is_empty(), "Expected all events to be processed")
        self.assertEqual(simulation.customer_count, expected_customers, "Check if all customers were handled")

        # simulation.process_arrival(event)
        # self.assertEqual(simulation.clock, 14)
        # self.assertEqual(simulation.customer_count, 1)
        

if __name__ == '__main__':
    unittest.main()