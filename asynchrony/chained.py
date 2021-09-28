# chained.py

import asyncio
import random
import time

async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"at {time.time()-now:.2f} part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"at {time.time()-now:.2f} Returning part1({n}) == {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"at {time.time()-now:.2f} part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"at {time.time()-now:.2f} Returning part2{n, arg} == {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    print(f'before p1: at {time.time()-now:.2f} n={n}')
    p1 = await part1(n)
    print(f'before p2: at {time.time()-now:.2f} n={n}')
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"at {time.time()-now:.2f} -->Chained result{n} => {p2} (took {end:0.2f} seconds).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))  # == await asyncio.gather(chain(1), chain(2), chain(3))

if __name__ == "__main__":
    now = time.time()
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"at {time.time()-now:.2f} Program finished in {end:0.2f} seconds.")
