isPrime :: Integral a => a -> Bool
isPrime x = isPrimeHelper x $ floor $ sqrt $ fromIntegral x

isPrimeHelper :: Integral a => a -> a -> Bool
isPrimeHelper 0 _ = False
isPrimeHelper 1 _ = False
isPrimeHelper x 1 = True
isPrimeHelper x n = x `mod` n /= 0 && isPrimeHelper x (n-1)

isNotPrime :: Integral a => a -> Bool
isNotPrime x = not $ isPrime x

nextPrime :: Integral a => a -> a
nextPrime x = head $ filter isPrime [(x+1)..(x*2)]

isGoldbach :: Integral a => a -> Bool
isGoldbach x = isGoldbachHelper x 2 1

isGoldbachHelper :: Integral a => a -> a -> a -> Bool
isGoldbachHelper x p n = 
	if ((p + (2*(n^2))) > x)
		then if (p > x)
			then False
			else isGoldbachHelper x (nextPrime p) 1
		else (x == p + (2*(n^2))) || isGoldbachHelper x p (n+1)
				
isNotGoldbach :: Integral a => a -> Bool
isNotGoldbach x = not $ isGoldbach x

solution = head . filter isNotGoldbach $ filter isNotPrime [9,11..]

main = putStrLn $ show solution