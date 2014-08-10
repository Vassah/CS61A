seq_product 0 term = 1
seq_product n term = (term n) * (seq_product (n - 1) term)

identat :: Int -> Int
identat x = x

factorialus :: Int -> Int
factorialus n = seq_product n identat


main = putStrLn (show (seq_product 5 identat) ++ show (factorialus 5))