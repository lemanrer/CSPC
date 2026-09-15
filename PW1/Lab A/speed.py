import time
from decay import simulate, simulate_loop


N0 = 200000
lam = 0.4
dt = 0.05
steps = 200


start = time.perf_counter()
simulate_loop(N0, lam, dt, steps)
python_time = time.perf_counter() - start


start = time.perf_counter()
simulate(N0, lam, dt, steps)
numpy_time = time.perf_counter() - start


print(f"Pure Python: {python_time:.4f} seconds")
print(f"NumPy: {numpy_time:.4f} seconds")
print(f"NumPy is {python_time / numpy_time:.2f} times faster")