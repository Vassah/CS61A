-module(iffer).
-export([if_fun/3]).

if_fun(Cond, A, B) when Cond == true ->
     A;
if_fun(Cond, A, B) -> B.