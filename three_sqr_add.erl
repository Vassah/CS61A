-module(three_sqr_add).
-export([three_square_add/3]).

three_square_add(A,B,C) when A < B andalso B =< C -> 
  (B * B) + (C * C);
three_square_add(A,B,C) when A < C andalso C =<  B -> three_square_add(A,C,B);
three_square_add(A,B,C) when B < A andalso A =< C ->
  (A * A) + (C * C);
three_square_add(A,B,C) when B < C andalso C =< A -> three_square_add(C,B,A);
three_square_add(A,B,C) when C < A andalso A =< B ->
  (A * A) + (C * C);
three_square_add(A,B,C) when C < B andalso B =< A -> three_square_add(B,A,C).