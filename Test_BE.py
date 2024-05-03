import Lab2.BE as test
import statistics

test_temps = list[12,23,25,10,5,15,20]

def Test_find_min_max():
   result = test.find_min_max(test_temps)
   
   assert (result == min(test_temps) & result == max(test_temps))

def Test_calc_average():
   result = test.calc_average(test_temps)

   assert (result == (sum(test_temps) / len(test_temps)))

def Test_calc_median_temperature():
   result = test.calc_median_temperature(test_temps)

   assert (result == statistics.median(test_temps) )