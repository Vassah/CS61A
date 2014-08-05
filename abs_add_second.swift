//
//  abs_add_second.swift
//  
//
//  Created by Stephen Lazaro on 8/5/14.
//
//

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