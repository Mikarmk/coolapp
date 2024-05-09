program RandomNumberGenerator
    implicit none
    
    integer, parameter :: n = 10  
    integer :: seed, a, c, m, i, j
    real, dimension(n, n) :: random_numbers
    
    seed = 12345
    a = 1664525
    c = 1013904223
    m = 2**32
    
    do i = 1, n
        do j = 1, n
            seed = mod(a * seed + c, m)
            random_numbers(i, j) = real(seed) / real(m)
        end do
    end do
    
    print *, "Сгенерированные случайные числа в виде двумерного массива:"
    do i = 1, n
        write(*, '(10F8.4)') (random_numbers(i, j), j = 1, n)
    end do
    
end program RandomNumberGenerator
