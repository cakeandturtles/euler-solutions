rev :: Integer -> Integer
rev x | x < 0     = 0 - (read . reverse . tail . show $ x)
      | otherwise = read . reverse . show $ x

isLychrel :: Integer -> Integer -> Bool
isLychrel n x = ((x + rev x) /= rev (x + rev x)) && ((n >= 50) || isLychrel (n+1) (x + rev x))

main = putStrLn $ show $ length $ filter (\x -> isLychrel 0 x) [10..10000]