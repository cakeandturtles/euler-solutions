isPrime :: Int -> Bool
isPrime x = isPrimeHelper x $ floor $ sqrt $ fromIntegral x

isPrimeHelper :: Int -> Int -> Bool
isPrimeHelper 0 _ = False
isPrimeHelper 1 _ = False
isPrimeHelper x 1 = True
isPrimeHelper x n = x `mod` n /= 0 && isPrimeHelper x (n-1)

nextPrime :: Int -> Int
nextPrime x = head $ filter isPrime [(x+1)..(x*2)]

--I don't know how to specify list types :(
--calcLongestConsecutivePrimeSum :: Int -> Int -> [[Int, Int]]
calcLongestConsecutivePrimeSum x limit = clcpsHelper x 0 0 limit

--clcpsHelper :: Int -> Int -> Int -> Int -> [[Int, Int]]
clcpsHelper n sum m limit = 
	if sum + n > limit
		then if isPrime sum
			then [[m, sum]]
			else []
		else clcpsHelper (nextPrime n) (sum + n) (m + 1) limit 
		

--solHelper :: Int -> Int -> [Int, Int]
solHelper n limit = 
	if n >= limit 
		then []
		else calcLongestConsecutivePrimeSum n limit ++ solHelper (nextPrime n) limit 

--max' :: [Int, Int] -> [[Int, Int]] -> [Int, Int]
max' m xs =
	if xs == []
		then m
		else if head m > ((head xs) !! 0)
			then max' m (tail xs)
			else max' (head xs) (tail xs)

solution = max' [0, 0] $ solHelper 2 1000000

main = putStrLn $ show solution