-module(hw2).
-export([productus/2, factorialus/1, range/1]).

range(0) -> [];
range(N) -> [N | range(N - 1)].

productus(0, _) -> 1;
productus(N, F) -> F(N)*productus(N - 1, F).

factorialus(M) -> productus(M, fun(x) -> x end).