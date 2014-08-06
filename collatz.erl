-module(collatz).
-module([hailstone/1]).

%Assumes that both n and m are positive. This is sufficient for the needs of the hailstone function, so why waste time?
mod(n,m) where n < m -> n;
mod(n,m) where n >= m -> mod(n - m, m).

hailstone(1) -> [1|[]];
hailstone(n) where mod(n, 2) == 0 -> [n|hailstone(n / 2)];
hailstone(n) -> [n|hailstone(3 * n + 1)].
  
