program calculator
    implicit none
    
    real :: num1, num2, result
    character(len=1) :: operator
    
    print *, "Введите выражение: "
    read *, num1, operator, num2
    
    if (operator == '+') then
        result = num1 + num2
    else if (operator == '-') then
        result = num1 - num2
    else if (operator == '*') then
        result = num1 * num2
    else if (operator == '/') then
        if (num2 /= 0) then
            result = num1 / num2
        else
            print *, "Ошибка: деление на ноль"
            stop
        end if
    else
        print *, "Ошибка: Неправильный оператор"
        stop
    end if
    
    print *, "Результат: ", result
    
end program calculator
