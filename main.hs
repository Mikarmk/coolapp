calculate :: Double -> Double -> Char -> Double
calculate x y op
    | op == '+' = x + y
    | op == '-' = x - y
    | op == '*' = x * y
    | op == '/' = x / y
    | otherwise = error "Неподдерживаемая операция"

readNumber :: String -> Double
readNumber str = read str :: Double

main :: IO ()
main = do
    putStrLn "Введите первое число:"
    input1 <- getLine
    let num1 = readNumber input1

    putStrLn "Введите операцию (+, -, *, /):"
    operation <- getLine

    putStrLn "Введите второе число:"
    input2 <- getLine
    let num2 = readNumber input2

    let result = calculate num1 num2 (head operation)
    putStrLn $ "Результат: " ++ show result