-module(collatz).
-module([hailstone/1]).

hailstone(1) -> [1|[]];
hailstone(n) where n % 2 == 0 -> [n|hailstone(n / 2)];
hailstone(n) -> [n|hailstone(3 * n + 1)].
  