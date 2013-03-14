module Primes
    --(primes)
    where

main :: IO ()
main = print $ take 100 primes

primes :: [Integer]
primes = [x | x <- 2:[3,5..], notElem 0 $ map (x`mod`) [2..(floor $ sqrt (fromInteger x :: Double))]]
