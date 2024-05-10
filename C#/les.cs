using System;

class Program
{
    static void Main()
    {
        Random random = new Random();
        string[] forest = new string[] { "Дерево", "Камень", "Река", "Лес" };
        string[] spirit = new string[] { "Деревенский дух", "Лесной дух", "Речной дух", "Каменный дух" };
        string[] actions = new string[] { "Пройти", "Вернуться", "Помочь", "Убежать" };
        string[] outcomes = new string[] { "Вы нашли лесного духа", "Вы нашли деревенского духа", "Вы нашли речного духа", "Вы нашли каменного духа" };
        int choice = 0;
        int score = 0;

        Console.WriteLine("Добро пожаловать в сказку о лесном духе!");
        Console.WriteLine("Вы находитесь в лесу, где живут различные духи. Вы можете:");
        for (int i = 0; i < actions.Length; i++)
        {
            Console.WriteLine($"{i + 1}. {actions[i]}");
        }

        while (true)
        {
            Console.Write("Выберите действие: ");
            string input = Console.ReadLine();

            if (!int.TryParse(input, out choice) || choice < 1 || choice > actions.Length)
            {
                Console.WriteLine("Пожалуйста, введите корректный номер действия.");
                continue;
            }

            int spiritIndex = random.Next(0, spirit.Length);
            string spiritName = spirit[spiritIndex];
            string outcome = outcomes[spiritIndex];

            Console.WriteLine($"Вы {actions[choice - 1]} и нашли {spiritName}.");
            Console.WriteLine(outcome);

            if (choice == 1)
            {
                Console.WriteLine("Вы продолжили свой путь.");
                score++;
            }
            else if (choice == 2)
            {
                Console.WriteLine("Вы вернулись домой.");
                break;
            }
            else if (choice == 3)
            {
                Console.WriteLine("Вы помогли духу и он вам благословил.");
                score += 2;
                break;
            }
            else if (choice == 4)
            {
                Console.WriteLine("Вы убежали от духа и больше не видели его.");
                score--;
                break;
            }

            if (score >= 5)
            {
                Console.WriteLine("Вы стали мудрым путником и заслужили уважение духов.");
                break;
            }
            else if (score <= -3)
            {
                Console.WriteLine("Вы испугали духов своим поведением и они прогнали вас из леса.");
                break;
            }
        }

        Console.WriteLine($"Ваш счет: {score}");
        Console.WriteLine("Спасибо за игру!");
    }
}
