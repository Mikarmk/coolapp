program WeatherModel
    implicit none
    
    ! Константы
    integer, parameter :: days = 7
    integer, parameter :: hours_per_day = 24
    real, parameter :: initial_temperature = 20.0
    real, parameter :: heating_rate = 0.1
    real, parameter :: cooling_rate = 0.05
    
    ! Массив для хранения температуры
    real :: temperature(days, hours_per_day)
    
    ! Начальные условия
    temperature(:, :) = initial_temperature
    
    ! Моделирование изменения температуры
    call simulate_weather_model(days, hours_per_day, temperature, heating_rate, cooling_rate)
    
contains
    
    subroutine simulate_weather_model(d, h, temp, heat_rate, cool_rate)
        integer, intent(in) :: d, h
        real, intent(inout) :: temp(d, h)
        real, intent(in) :: heat_rate, cool_rate
        
        integer :: day, hour
        
        do day = 1, d
            do hour = 1, h
                if (hour > 6 .and. hour < 18) then
                    temp(day, hour) = temp(day, hour) + heat_rate
                else
                    temp(day, hour) = temp(day, hour) - cool_rate
                end if
            end do
        end do
    end subroutine simulate_weather_model
    
end program WeatherModel
