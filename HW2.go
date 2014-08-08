package hw2

import "fmt"

type intFun func(int) int

//Recursive product function over a sequence given by a function
func product(n int, term intFun) int {
  if n==1 {
    return 1
    }
  return term(n)*product(n-1, term)
}

//Tail recursive version?
func prod_aux(n int, term intFun, acc int) int {
  if n==1 {
    return 1
  } else {
    return prod_aux(n-1, term, term(n)*acc)
  }
}

func prod_tail(n int, term intFun) int {
  return prod_aux(n, term, 1)
}

//Recursive summation function over a sequence given by a function
func summation(n int, term intFun) int {
  if n==0 {
    return 0
    }
  return term(n)+summation(n-1, term)
  }

//Tail recursive version?
func summ_aux(n int, term intFun, acc int) int {
  if n==0 {
    return 0
    }
  return summ_aux(n-1, term, term(n)+acc)
}

func summ_tail(n int, term intFun) int {
  return summ_aux(n, term, 0)
  }

func main() {
  //Various Tests Here, It Compiles So Now Just The Rest
}