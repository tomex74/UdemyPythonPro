
import re
import io
import cProfile
import pstats

import vector

test_code = '''\
v = vector.Vector2D(-1, 1)
v *= vector.Vector2D(-2, 2)
v /= 2.0
'''

# Single cProfiler
cProfile.run(test_code)

# cProfiler with pstats
pr = cProfile.Profile()
pr.enable()
# START CODE
v = vector.Vector2D(-1, 1)
v *= vector.Vector2D(-2, 2)
v /= 2.0
# END CODE
pr.disable()
s = io.StringIO()
sortby = pstats.SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
