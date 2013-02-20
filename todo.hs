module Main where

import System.Environment
import System.Exit(exitFailure)

newtype TodoList = TodoList { getTodo :: [String] }

instance Show TodoList where
    show (TodoList l) = foldr (\x acc -> x ++ ('\n':acc)) [] $ zipWith (++) (map ((++". ").show) ([1..] :: [Int])) l

main :: IO ()
main = do
    args <- getArgs
    let len = length args
    if len >= 2 || len == 0
        then do
            putStrLn "Need exactly one argument"
            exitFailure
        else putStrLn "Reading TODO...\n"
    let todoFile = head args
    td <- readFile todoFile
    let things = TodoList $ lines td
    doneFile <- todo 's' things
    writeFile todoFile $ unlines doneFile
    putStrLn "See you next time!"

todo :: Char -> TodoList -> IO [String]
todo 'h' x = do
    putStrLn "Commands:\n-> s: show todo list\n-> a: add one item ( to the beginning )\n-> c: cancel one item ( choose which )\n-> p: promote ( set one item to the heighest priority )\n-> d: delay mode ( lower the priority of the first item )\n-> l: lazy mode ( delay first item to the end )\n-> b: backoff ( exit and save )"
    putStrLn "\nYour Action:"
    action <- getChar
    _ <- getChar
    todo action x
todo 's' x = do
    putStrLn "Your TODO:"
    print x
    todo 'h' x
todo 'a' (TodoList l) = do
    putStrLn "Your new todo item: "
    item <- getLine
    let ll = item : l
    putStrLn "Successfully added one item!"
    todo 's' (TodoList ll)
todo _ x@(TodoList []) = todo 's' x
todo a x@(TodoList l)
    | a == 'p' = do
        putStrLn "Which item do you want to promote?"
        n <- readLn :: IO Int
        if n > length l
            then do
                putStrLn $ "\nThere is no item no." ++ show n
                todo 's' x
            else do
                let temp = take n l
                todo 's' (TodoList $ last temp : init temp ++ drop n l)
    | a == 'c' = do
        putStrLn "Which item do you want to delete?"
        n <- readLn :: IO Int
        todo 's' (TodoList $ take (n-1) l ++ drop n l)
    | a == 'd' =
        if length l > 1
            then todo 's' (TodoList $ (head.tail $ l):head l:(tail.tail $ l))
            else todo 's' x
    | a == 'l' = todo 's' (TodoList $ tail l ++ [head l])
    | a == 'b' = return l
    | otherwise = putStrLn "\nNon-existing command!!" >> todo 's' x
