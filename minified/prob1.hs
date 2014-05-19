asum :: Integral a => a -> a -> a
asum n l = n * (l `div` n)*(1+(l `div` n)) `div` 2

main = putStrLn $ show $ asum 3 999 + asum 5 999 - asum 15 999