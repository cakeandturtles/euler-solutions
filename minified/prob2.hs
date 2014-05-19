--4.236068 (phi^3) is approximate ration between consecutive even terms in fibonacci sequence
--because phi = golden ratio, and # is even every 3rd term
evenFibs :: Integral a => a -> a -> [a]
evenFibs y x = if x > y
	then []
	else [x] ++ (evenFibs y $ truncate ((fromIntegral(x) * 4.236068) + 0.5))

main = putStrLn $ show $ sum $ evenFibs 4000000 2 