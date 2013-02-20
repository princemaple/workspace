-- testing tuple constructor/properties
-- testing Haskell return type polymorphism

module Main where

main :: IO ()
main = do
	--let (a, b) = (1, 2)
	--print a
	--print b
	--print $ (,) a b
	print (fromTuple (1, 'a') :: Int)
	print (fromTuple (1, 'a') :: Char)

class Tp a where
	fromTuple :: (Int, Char) -> a

instance Tp Int where
	fromTuple (i, _) = i

instance Tp Char where
	fromTuple (_, s) = s