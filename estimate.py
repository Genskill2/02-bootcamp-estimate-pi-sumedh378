import math
import unittest
import random

class TestWallis(unittest.TestCase):
    
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
    def wallis(n):
    	if(n==0):
    		return 0
    	mul = 1.0
    	for i in range(0,n+1):
    		k = 4*(i**2)
    		mul = mul*k/(k-1)
    	return mul*2


class TestMC(unittest.TestCase):


    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
    def monte_carlo( n ):
    	for i in range(0,n+1):
    		x = random(-1,1)
    		y = random(-1,1)
    		 
    		check = x*x + y*y
    		
    		if (check < 1) :
    			cp+=1
    			
    	pi = 4*(cp/n)
    		return pi
        
    
if __name__ == "__main__":
    unittest.main()
