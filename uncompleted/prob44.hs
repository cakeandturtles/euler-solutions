pentagonize :: Int -> Int
pentagonize x = quot (x*(3*x-1)) 2

isPentagon :: Int -> Bool
isPentagon x = isPentagonHelper x 0

isPentagonHelper :: Int -> Int -> Bool
isPentagonHelper x n = ((pentagonize n) == x) || ((pentagonize n) < x && isPentagonHelper x (n+1))

--Very very slow and unoptimized solution to the problem. Takes well over a minute to solve
solve :: Int -> Int -> [Int]
solve j k = if j >= k
	then []
	else if (isPentagon $ (pentagonize k) - pentagonize j) && (isPentagon $ (pentagonize k) + pentagonize j)
		then [(pentagonize k) - pentagonize j]
		else (solve (j+1) k) ++ (solve 1 (k+1))
		
main = putStrLn $ show $ head $ solve 1 2
