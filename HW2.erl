-module(hw2).
-export([productus/2, factorialus/1, range/1]).

range(0) -> [];
range(n) -> [n | range(n - 1)].

productus(0, _) -> 1;
productus(n, F) -> list:map(F, range(n)).

factorialus(m) -> productus(m, fun(x) -> x end).