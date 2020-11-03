import unittest
from main import *

class UnitTests(unittest.TestCase) :
      def test_plot(self) :
         self.assertTrue( np.abs( ex-1.57664233576642)<1e-7, "your value for ex is not correct" )
         self.assertTrue( np.abs( ey-2.33868613138686)<1e-7, "your value for ey is not correct" )
         self.assertTrue( np.abs( varx-0.0784325217113322)<1e-7, "your value for varx is not correct" )
         self.assertTrue( np.abs( vary-0.285291704406201)<1e-7, "your value for vary is not correct" )
         self.assertTrue( np.abs( cov+0.00187010496030693)<1e-7, "your value for cov is not correct" )
         self.assertTrue( np.abs( rho+0.0125018222877928)<1e-7, "your value for rho is not correct" )
