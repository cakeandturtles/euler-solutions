power :: Integral x => [x] -> [x] -> [x] -> [x]
power [] _ _ = []
power _ [] _ = []
power (x:xs) (y:[]) zs = [(x ^ y)] ++ power (xs) zs zs
power (x:xs) (y:ys) zs = [(x ^ y)] ++ power (x:xs) ys zs

digs :: Integral x => x -> [x]
digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]

digitalSum :: Integral x => x -> x
digitalSum = sum . digs

solution = maximum (map digitalSum $ power [2..99] [2..99] [2..99])

main = print solution