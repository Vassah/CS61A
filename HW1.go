import "fmt"

func a_abs_plus_b(a, b) {
  if b < 0 {
    return a - b
  }
  else {
    return a + b
  }
}

func two_of_three(a, b, c) {
  switch {
    case a < min(b, c): return b*b + c*c
    case b < min(a, c): return a*a + c*c
    case c < min(a, b): return a*a + b*b
    }
  }
/*
func iffer(cond, truf, failse) {
  x = cond and truf
  y = cond or failse
  return x or y
  }
I'd love to be able to use this but I think that since go is strongly typed I won't be able to.
*/
func hailstone(n) {
  fmt.println(n)
  if n == 1 {
    return
    }
  if n % 2 == 0 {
    hailstone(n / 2)
    }
  if n % 2 == 1 {
    hailstone(3*n + 1)
    }
}
//Done. Now just gotta go home and compile.
  
func main() {
  fmt.println(two_of_three(5,6,7))
  fmt.println(two_of_three(6,5,7))
  fmt.println(two_of_three(6,7,5))
  fmt.println(a_abs_plus_b(5,-6))
  fmt.println(a_abs_plus_b(5,6))
  hailstone(10)
  hailstone(27)
}
