import Numeric
import Data.Char
import Data.Maybe

isPalindrome :: String -> Bool
isPalindrome a = a == reverse a

isIntPalindrome :: Int -> Bool
isIntPalindrome a = isPalindrome . show $ a

convertToBinary :: Int -> String
convertToBinary n = showIntAtBase 2 intToDigit n ""

convertToDecimal :: Integral a => String -> a
convertToDecimal s = fst $ head $ readInt 2 (`elem` "01") digitToInt s

solution0 = sum (map convertToDecimal (filter isPalindrome (map convertToBinary (filter isIntPalindrome [1..1000000]))))
solution1 = sum $ map convertToDecimal $ filter isPalindrome $ map convertToBinary $ filter isIntPalindrome [1..1000000]
solution2 = sum . map convertToDecimal . filter isPalindrome . map convertToBinary $ filter isIntPalindrome [1..1000000]

main = putStrLn $ show solution0
