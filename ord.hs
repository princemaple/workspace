module Main where

data Ordered = A | B | C deriving(Eq, Show, Read)

instance Ord Ordered where
    A > _ = True
    _ > A = False
    _ > _ = False
    A < _ = False
    _ < A = True
    _ < _ = False

main :: IO ()
main = do print (A > B)
          print (B > C)
          print (C < C)
          print $ A == A
          print $ B == C