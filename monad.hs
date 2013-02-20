module Main where

main :: IO ()
main = myForever (getLine >>= print)

myForever :: (Monad m) => m a -> m b
myForever m = m >> myForever m