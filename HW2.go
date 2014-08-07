//Recursive product function over a sequence given by a function
func product(n int, term func) int {
  if n==1 {
    return 1
    }
  return term(n)*product(n-1, term)
}

//Tail recursive version?
func prod_aux(n int, term func, acc int) {
  if n==1 {
    return 1
    }
  return prod_aux(n-1, term, term(n)*acc)

func prod_tail(n int, term func) int {
  return prod_aux(n, term, 1)
}

//Recursive summation function over a sequence given by a function
func summation(n int, term func) int {
  if n==0 {
    return 0
    }
  return term(n)+summation(n-1, term)
  }

//Tail recursive version?
func summ_aux(n int, term func, acc int) int {
  if n==0 {
    return 0
    }
  return summ_aux(n-1, term, term(n)+acc)

func summ_tail(n int, term func) int {
  return summ_aux(n, term, 0)
  }
