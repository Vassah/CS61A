seq_product 0 term = 1
seq_product n term = (term n) * (seq_product (n - 1) term)

identat :: Int -> Int
identat x = x

factorialus :: Int -> Int
factorialus n = seq_product n identat

accumulate combiner start n term
  |start == n = term n
  |otherwise  = combiner (term start) (accumulate combiner (start + 1) n term)

multus :: Int -> Int -> Int
multus x y = x*y

addit :: Int -> Int -> Int
addit x y = x + y

productus n term = accumulate multus 1 n term

summatus n term = accumulate addit 0 n term

repeated _ 0 = identat
repeated fz n = (\ x -> fz (repeated fz (n - 1)))

double fz = repeated fz 2

main = putStrLn (show (seq_product 5 identat) ++ show (factorialus 5) ++ show (accumulate (\x y -> x * y) 1 5 (\x -> x)) ++ show ((repeated (\x -> x + 2) 5) 2)) 