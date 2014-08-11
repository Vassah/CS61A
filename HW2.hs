seq_product 0 term = 1
seq_product n term = (term n) * (seq_product (n - 1) term)

identat :: Int -> Int
identat x = x

factorialus :: Int -> Int
factorialus n = seq_product n identat

accumulate combiner start n term
  |start == n = term n
  |otherwise  = combiner (term start) (accumulate combiner (start + 1) n term)

main = putStrLn (show (seq_product 5 identat) ++ show (factorialus 5) ++ show (accumulate (\x y -> x * y) 1 5 (\x -> x)))