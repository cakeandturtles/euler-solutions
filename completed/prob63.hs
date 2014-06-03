solve :: Int -> Int -> Int
solve 9 n = if (length . show) (9^n) == n
	then 1 + solve 1 (n+1)
	else 0
solve x n = if (length . show) (x^n) == n
	then 1 + solve (x+1) n
	else solve (x+1) n


main = putStrLn $ show $ solve 1 1