--http://stackoverflow.com/questions/3596502/lazy-list-of-prime-numbers
primes :: Integral a => [a]
primes = sieve [2..]
  where
    sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]

--http://stackoverflow.com/questions/4541415/haskell-prime-test
isPrime :: Integral a => a -> Bool
isPrime x = not $ any divisible $ takeWhile notTooBig [2..] where
     divisible y = x `mod` y == 0
     notTooBig y = y*y <= x

primeFactors :: Integral a => a -> [a]
primeFactors x = 
	if isPrime x 
		then [x]
		else [y] ++ primeFactors(x `quot` y) where
			y = head(filter divisible primes)
			divisible n = x `mod` n == 0
			
fourPrimeFactors :: Integral a => [a] -> Bool
fourPrimeFactors xs = fpfHelper xs 0 0

fpfHelper :: Integral a => [a] -> a -> a -> Bool
fpfHelper [] n _ = n >= 4
fpfHelper (x:[]) n _ = (n+1) >= 4
fpfHelper (x:xs) n p =
	if x == head xs && not (x == p)
		then fpfHelper xs (n+1) x
		else if x == p
			then fpfHelper xs n x
			else fpfHelper xs (n+1) 0

--ys is of the form [[z::zs]], where z is the number and zs is its prime factors
consecutive :: Integral a => [[a]] -> Bool
consecutive [] = True
consecutive (y:[]) = True
consecutive (y:ys) = (head y == (head (head ys))-1) && consecutive ys

distinct :: Integral a => [a] -> [a] -> Bool
distinct [] _ = True
distinct _ [] = True
distinct (x:[]) (y:[]) = x /= y
distinct (x:[]) (y:ys) = x /= y || y == head ys
distinct (x:xs) (y:[]) = x /= y || x == head xs
distinct (x:xs) (y:ys) = 
	if x /= y
		then distinct ([x]++xs) ys && distinct xs ([y]++ys)
		else if x == head xs && y == head ys
			then distinct xs ys
			else if x == head xs
				then distinct (tail xs) ys
				else if y == head ys
					then distinct xs (tail ys)
					else False

--ys is of the form [[z::zs]], where z is the number and zs is its prime factors			
distinctFactors :: Integral a => [[a]] -> Bool
distinctFactors [] = True
distinctFactors (y:[]) = True
distinctFactors (y:ys) = distinct(tail y) (tail(head ys)) && distinctFactors ([y]++(tail ys)) && distinctFactors ys
			
consecutiveFourDistinctPrimeFactors :: Integral a => a -> [[a]]
consecutiveFourDistinctPrimeFactors x = cfdpfHelper x []
		
--ys is of the form [[z::zs]], where z is the number and zs is its prime factors
cfdpfHelper :: Integral a => a -> [[a]] -> [[a]]
cfdpfHelper x ys = 
	if length ys == 4
		then [[head (head ys)]] ++ cfdpfHelper (x+1) []
		else if not (fourPrimeFactors (primeFactors x)) || not (consecutive ys) || not (distinctFactors ys)
			then cfdpfHelper (x+1) []
			else if consecutive(ys)
				then cfdpfHelper (x+1) (ys ++ [[x]++(primeFactors x)])
				else []
			
--solution = head (filter consecutiveDistinctPrimes (map primeFactors [647..]))
solution = head(consecutiveFourDistinctPrimeFactors 647)