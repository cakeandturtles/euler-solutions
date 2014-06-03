chainStep :: Int -> Int
chainStep 0 = 0
chainStep x = (x `mod` 10) ^ 2 + chainStep (x `quot` 10)

chainTo89 :: Int -> Bool
chainTo89 1 = False
chainTo89 89 = True
chainTo89 x = chainTo89 (chainStep x)

--Pretty slow implementation. Over a minute long.
solve :: Int 
solve = length $ filter chainTo89 [1..9999999]

main = putStrLn $ show $ solve