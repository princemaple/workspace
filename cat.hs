module Main where

import System.Environment(getArgs)

main :: IO ()

main = getArgs >>= putFiles

putFiles :: [String] -> IO ()
putFiles l = do
    let files = map readFile l
        ifiles = zip [1..] files :: [(Int, IO String)]
        end i = putStrLn $ " <<<<<End of file>>>>>\n\n==--------------- No. " ++ show i ++ " ---------------==\n"
        execute x = do
            snd x >>= putStr
            end.fst $ x
    mapM_ execute ifiles
