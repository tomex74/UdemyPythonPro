
import re
import io
import cProfile
import pstats

import numpy as np

# Test code
M = np.random.randint(low=-100, high=100, size=(8000, 8000))

# Single cProfiler
cProfile.run('np.linalg.inv(M)')

# cProfiler with pstats
pr = cProfile.Profile()
pr.enable()
pr.runcall(np.linalg.inv, M)
pr.disable()
s = io.StringIO()
sortby = pstats.SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
