module Main where

import qualified Data.Foldable as F
import Data.Monoid

data T a = Tree {getI::a, getL::T a, getR::T a} | Null deriving(Read, Eq)

treeToList :: T a -> [a]
treeToList = F.foldMap (\x -> [x])

treeToList2 :: T a -> [a]
treeToList2 = F.foldr (:) []

instance Show a => Show (T a) where
    show Null         = "Null"
    show (Tree i l r) = '(':show l ++ " <-" ++ show i ++ "-> " ++ show r ++ ")"

instance F.Foldable T where
    foldMap _ Null = mempty
    foldMap f (Tree x l r) = F.foldMap f l `mappend`
                             f x           `mappend`
                             F.foldMap f r

main :: IO ()
main = do
    let t = Tree 1 (Tree 5 Null (Tree 7 (Tree 9 Null Null) Null)) (Tree 8 Null Null) :: T Int
    print t
    print (read "Tree{getI=1, getL=Null, getR=Null}" :: T Int)
    print $ F.foldl (*) 1 t
    print $ F.foldl (+) 0 t
    print $ treeToList t
    print $ treeToList2 t
