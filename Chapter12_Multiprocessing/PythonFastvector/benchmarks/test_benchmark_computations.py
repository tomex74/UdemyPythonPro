import random

import numba
import numpy as np

import fastvector

LEN = 100_000
v = fastvector.VectorND([random.random() for _ in range(LEN)])
a = np.array([random.random() for _ in range(LEN)])
print(type(v.values))

NUM_ROUNDS = 20
NUM_ITERATIONS = 50

# Pre-compile to benchmark only the runtime
fastvector._numba_clip_vector(v.values, -1.0, 1.0, v.values, LEN)

def test_python_clip_vector(benchmark):
    benchmark.pedantic(fastvector.python_clip_vector, args=(v, -1.0, 1.0, v), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_naive_cython_clip_vector(benchmark):
    benchmark.pedantic(fastvector.naive_cython_clip_vector, args=(v, -1.0, 1.0, v), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_cython_clip_vector(benchmark):
    benchmark.pedantic(fastvector.cython_clip_vector, args=(v, -1.0, 1.0, v), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_cython_clip_vector_omp2(benchmark):
    benchmark.pedantic(fastvector.cython_clip_vector_omp, args=(v, -1.0, 1.0, v, 2), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_cython_clip_vector_omp4(benchmark):
    benchmark.pedantic(fastvector.cython_clip_vector_omp, args=(v, -1.0, 1.0, v, 4), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_cython_clip_vector_omp6(benchmark):
    benchmark.pedantic(fastvector.cython_clip_vector_omp, args=(v, -1.0, 1.0, v, 6), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_cython_clip_vector_omp8(benchmark):
    benchmark.pedantic(fastvector.cython_clip_vector_omp, args=(v, -1.0, 1.0, v, 8), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_numba_clip_vector(benchmark):
    benchmark.pedantic(fastvector.numba_clip_vector, args=(v, -1.0, 1.0, v), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)

def test_np_clip(benchmark):
    benchmark.pedantic(np.clip, args=(a, -1.0, 1.0, a), rounds=NUM_ROUNDS, iterations=NUM_ITERATIONS)
