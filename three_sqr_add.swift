//
//  three_sqr_add.swift
//  
//
//  Created by Stephen Lazaro on 8/5/14.
//
//

import Foundation

func three_sqr_add(a: Int, b: Int, c: Int) -> Int {
    if a < min(b, c) {
        return b*b + c*c
    }
    else if b < min(a, c) {
        return a*a + c*c
    }
    else if c < min(a, b) {
        return a*a + b*b
    }
    else {
        return a*a + b*b
    }
}