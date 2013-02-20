module Main where

import Control.Monad(forever)

fib :: [Integer]
fib = 1:1:zipWith (+) fib (tail fib)

main :: IO ()
main = forever $ do
	putStrLn "Which fib num?"
	--num <- getLine
	--print (last (take (read num::Int) fib))
	num <- readLn :: IO Int
	print.last.take num $ fib