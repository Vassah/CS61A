-module(abs_add_second).
-export([a_abs_plus_b/2]).

a_abs_plus_b(A, B) when B < 0 ->
  A - B;
a_abs_plus_b(A, B) when B >= 0 ->
  A + B.