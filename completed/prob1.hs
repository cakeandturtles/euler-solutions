sumOfSmallMultiples :: Int 
sumOfSmallMultiples = sum (filter mult35 [3..999])
	where mult35 x = x `mod` 3 == 0 || x `mod` 5 == 0
