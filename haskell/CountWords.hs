import System.IO
import System.Environment

main = do
    (target:args) <- getArgs
    withFile "CountWords.txt" ReadMode (\handle -> do
        contents <- hGetContents handle
        print $ countWords target contents)

countWords :: (Num a) => String -> String -> a
countWords target xs =
    let iter [] n = n
        iter (y:ys) n = if y == target
                        then iter ys n+1
                        else iter ys n
    in iter (words xs) 0
