using System;
using System.Collections.Generic;
using System.Threading;

class Program
{
    static int playerX = 10;
    static int playerY = 20;
    static List<int> bulletsX = new List<int>();
    static List<int> bulletsY = new List<int>();
    static int score = 0;
    static bool gameOver = false;

    static void Main()
    {
        Console.CursorVisible = false;
        Console.SetWindowSize(40, 30);

        Thread inputThread = new Thread(MovePlayer);
        inputThread.Start();

        Thread gameThread = new Thread(GameLoop);
        gameThread.Start();
    }

    static void MovePlayer()
    {
        while (!gameOver)
        {
            ConsoleKeyInfo key = Console.ReadKey(true);

            if (key.Key == ConsoleKey.LeftArrow && playerX > 0)
            {
                playerX--;
            }
            else if (key.Key == ConsoleKey.RightArrow && playerX < 39)
            {
                playerX++;
            }
            else if (key.Key == ConsoleKey.Spacebar)
            {
                bulletsX.Add(playerX);
                bulletsY.Add(playerY - 1);
            }
        }
    }

    static void GameLoop()
    {
        while (!gameOver)
        {
            Console.Clear();

            DrawPlayer();
            DrawBullets();
            MoveBullets();
            DrawScore();

            Thread.Sleep(100);
        }
    }

    static void DrawPlayer()
    {
        Console.SetCursorPosition(playerX, playerY);
        Console.Write("^");
    }

    static void DrawBullets()
    {
        for (int i = 0; i < bulletsX.Count; i++)
        {
            Console.SetCursorPosition(bulletsX[i], bulletsY[i]);
            Console.Write("|");
        }
    }

    static void MoveBullets()
    {
        for (int i = 0; i < bulletsY.Count; i++)
        {
            bulletsY[i]--;

            if (bulletsY[i] < 0)
            {
                bulletsY.RemoveAt(i);
                bulletsX.RemoveAt(i);
                i--;
            }
        }
    }

    static void DrawScore()
    {
        Console.SetCursorPosition(0, 0);
        Console.Write($"Score: {score}");
    }
}
