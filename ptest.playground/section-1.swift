// Playground - noun: a place where people can play

import Cocoa
import Foundation

func a_plus_abs_b(a: Int, b: Int) -> Int {
    if b >= 0 {
        return a + b
    }
    else {
        return a - b
    }
}

a_plus_abs_b(5, -6)
//Should be 11
a_plus_abs_b(5, 6)
//Should also be 11
a_plus_abs_b(25, -11)
//Should be 36
