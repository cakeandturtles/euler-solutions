import Data.List

--http://stackoverflow.com/questions/4541415/haskell-prime-test
isPrime :: Integral a => a -> Bool
isPrime x = not $ any divisible $ takeWhile notTooBig [2..] where
     divisible y = x `mod` y == 0
     notTooBig y = y*y <= x


commonDif :: Integral a => [a] -> [a]
commonDif [] = []
commonDif (x:[]) = []
commonDif (x:xs) = let y = ((head xs) + ((head xs) - x)) in
	if (isPrime y && y `elem` xs)
		then if (x == head xs)
			then []
			else [x, (head xs), y]
		else commonDif ([x]++(tail xs))
	
purge :: Integral a => [[a]] -> [[a]]
purge [] = []
purge (x:xs) = if (x == [])
	then purge xs
	else ([x]++(purge xs))
	 
main = putStrLn $ show $ purge $ map commonDif $ map (filter isPrime . map (\x -> read x :: Int) . permutations . show) [1000..9999]
