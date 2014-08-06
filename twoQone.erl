-module(twoQone).
-export().

praux(n, term, acc) -> praux(n-1, term, term(n)*acc);
praux(1, term, acc) -> term(1) * acc.

product(n, term) -> praux(n, term, 1).

factorial(n) -> product(n, lambda x: x).

accaux(combiner, start, n, term, acc) where start == n -> combiner(term(n), acc)
accaux(combiner, start, n, term, acc) -> accaux(combiner, start, n-1, term, combiner(term(n), acc))
accumulate(combiner, start, n, term) -> accaux(combiner, start, n, term, 1)
