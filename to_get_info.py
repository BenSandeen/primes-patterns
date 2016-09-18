import pstats
p = pstats.Stats('results.txt')
p.sort_stats('time').print_stats(20)
