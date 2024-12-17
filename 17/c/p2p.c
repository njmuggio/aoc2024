#include <stdint.h>
#include <stdio.h>
#include <inttypes.h>
#include <stdatomic.h>
#include <threads.h>
#include <unistd.h>

void cycle(uint64_t* pA, uint64_t* pB, uint64_t* pC)
{
  *pB = *pA & 0x07;
  *pB = *pB ^ 1;
  *pC = *pA >> *pB;
  *pB = *pB ^ 5;
  *pB = *pB ^ *pC;
  *pA = *pA >> 3;
}

int test(uint64_t initialA)
{
  uint64_t a = initialA;
  uint64_t b = 0;
  uint64_t c = 0;

  cycle(&a, &b, &c);
  if (b % 8 != 2) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 4) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 1) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 1) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 7) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 5) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 1) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 5) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 4) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 3) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 0) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 3) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 5) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 5) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 3) return 0;

  cycle(&a, &b, &c);
  if (b % 8 != 0) return 0;

  return 1;
}

int entry(void* pSharedA)
{
  while (1)
  {
    uint64_t seed = atomic_fetch_add((atomic_uint_fast64_t*)pSharedA, UINT32_MAX);
    for (uint64_t off = 0; off < UINT32_MAX; ++off)
    {
      if (test(seed + off)) printf("> %" PRIu64 "\n", seed + off);
    }
  }
}

int main(int argc, char** pArgv)
{
  atomic_uint_fast64_t a = 0;

  thrd_t aThrds[24];
  for (int i = 0; i < 24; i++)
  {
    thrd_create(&aThrds[i], entry, &a);
  }

  while (1)
  {
    printf("@ %" PRIu64 "\n", atomic_load(&a));
    sleep(15);
  }

  thrd_join(aThrds[0], 0);
}
