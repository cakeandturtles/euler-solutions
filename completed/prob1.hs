multOf3Or5 :: Int -> Bool
multOf3Or5 x = x `mod` 3 == 0 || x `mod` 5 == 0
	
main = putStrLn $ show (sum (filter multOf3Or5 [3..999]))