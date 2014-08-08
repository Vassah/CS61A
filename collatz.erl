-module(collatz).
-module([hailstone/1]).

%Assumes that both n and m are positive. 
%This is sufficient for the needs of the hailstone function, so why waste time?

hailstone(1) -> [1|[]];
hailstone(n) where n rem 2 == 0 -> [n|hailstone(n / 2)];
hailstone(n) -> [n|hailstone(3 * n + 1)].