package main

import "fmt"
import "math"

func a_abs_plus_b(x int, y int) int {
  if x < 0 {
    return x - y
  } else {
    return x + y
  }
}

func two_of_three(a float, b float, c float) float {
  switch {
    case a < math.Min(b, c): return b*b + c*c
    case b < math.Min(a, c): return a*a + c*c
    case c < math.Min(a, b): return a*a + b*b
    }
  }
/*
func iffer(cond bool, truf, failse) {
  x := cond && truf
  y := cond || failse
  return x || y
  }
I'd love to be able to use this but I think that since go is strongly typed I won't be able to. We'll see.
Since you don't HAVE to declare types, maybe it'll be ok.
*/
func hailstone(n int) {
  fmt.Println(n)
  if n % 2 == 0 {
    hailstone(n / 2)
    }
  if n % 2 == 1 {
    hailstone(3*n + 1)
    }
  return none
}
//Done. Now just gotta go home and compile.
  
func main() {
  fmt.Println(two_of_three(5,6,7))
  fmt.Println(two_of_three(6,5,7))
  fmt.Println(two_of_three(6,7,5))
  fmt.Println(a_abs_plus_b(5,-6))
  fmt.Println(a_abs_plus_b(5,6))
  hailstone(10)
  hailstone(27)
}
