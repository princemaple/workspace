module Main where

import System.IO
import Data.Char(toUpper)

data Tt = X | O | E deriving(Read, Eq)

instance Show Tt where
    show X = "X"
    show O = "O"
    show E = "_"

type Row = (Tt, Tt, Tt)
newtype Game = Game (Row, Row, Row)

instance Show Game where
    show (Game (a,b,c)) = show a ++ "\n" ++ show b ++ "\n" ++ show c

takeF :: (a,b,c) -> a
takeF (r,_,_) = r

takeS :: (b,a,c) -> a
takeS (_,r,_) = r

takeT :: (b,c,a) -> a
takeT (_,_,r) = r

initial :: Game
initial = Game ((E,E,E), (E,E,E), (E,E,E))

analyse :: Int -> (a,a,a) -> a
analyse i
    | i == 1 = takeF
    | i == 2 = takeS
    | i == 3 = takeT
    | otherwise = error "Wrong range"

exchange :: Char -> Char
exchange 'X' = 'O'
exchange 'O' = 'X'
exchange _ = undefined

fromChar :: Char -> Tt
fromChar 'X' = X
fromChar 'O' = O
fromChar _ = E

mark :: Game -> Int -> Int -> Char -> Game
mark (Game (a,b,c)) row col p
    | row == 1 = Game (markC a col p, b, c)
    | row == 2 = Game (a, markC b col p, c)
    | row == 3 = Game (a, b, markC c col p)
    | otherwise = error "Wrong range"

markC :: (Tt, Tt, Tt) -> Int -> Char -> (Tt, Tt, Tt)
markC (a,b,c) i p
    | i == 1 = (fromChar p, b, c)
    | i == 2 = (a, fromChar p, c)
    | i == 3 = (a, b, fromChar p)
    | otherwise = error "Wrong range"

lineUp :: (Tt, Tt, Tt) -> Bool
lineUp (a,b,c) = a == b && b == c

checkWin :: Game -> Tt
checkWin (Game (a, b, c))
    | lineUp a = takeF a
    | lineUp b = takeF b
    | lineUp c = takeF c
    | lineUp (takeF a, takeF b, takeF c) = takeF a
    | lineUp (takeS a, takeS b, takeS c) = takeS a
    | lineUp (takeT a, takeT b, takeT c) = takeT a
    | lineUp (takeF a, takeS b, takeT c) = takeF a
    | lineUp (takeT a, takeS b, takeF c) = takeT a
    | otherwise = E

play :: Game -> Char -> IO()
play w@(Game g) p = do
    print w
    putStr $ "Next move from " ++ show p ++ " (row column): "
    hFlush stdout
    l <- getLine
    let ll = map read.words $ l :: [Int]
        row = head ll
        col = head.tail $ ll
    if analyse col (analyse row g) == E
        then do
            let new = mark w row col p
                result = checkWin new
            if result /= E
                then do
                    putStrLn $ p : " won the game!!! Congrats"
                    print new
                    getLine >> print "See you!"
                else play new (exchange p)
        else do
            putStrLn "Occupied slot, try again"
            play w p

main :: IO ()
main = do
    putStr "which is to go first? X or O: "
    hFlush stdout
    p <- getLine
    let pp = toUpper.head $ p
    if pp `elem` "XO"
        then play initial pp
        else main
