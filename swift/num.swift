import Foundation

let randomNumber = Int.random(in: 1...100)

print("Добро пожаловать в игру 'Угадай число'!")
print("Попробуйте угадать число от 1 до 100.")

var guessed = false
var attempts = 0

while !guessed {
    print("Введите ваше предположение:")
    
    if let input = readLine(), let guess = Int(input) {
        attempts += 1
        
        if guess == randomNumber {
            print("Поздравляем! Вы угадали число за \(attempts) попыток.")
            guessed = true
        } else if guess < randomNumber {
            print("Загаданное число больше.")
        } else {
            print("Загаданное число меньше.")
        }
    } else {
        print("Пожалуйста, введите корректное число.")
    }
}
