#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

const int WINDOW_WIDTH = 40;
const int WINDOW_HEIGHT = 20;
const int CELL_SIZE = 1;
const int GRID_WIDTH = WINDOW_WIDTH / CELL_SIZE;
const int GRID_HEIGHT = WINDOW_HEIGHT / CELL_SIZE;

struct Point {
    int x, y;
};

class Snake {
public:
    Snake() {
        body.push_back({GRID_WIDTH / 2, GRID_HEIGHT / 2});
        direction = {1, 0};
    }

    void move() {
        Point head = body.front();
        head.x += direction.x;
        head.y += direction.y;

        if (head.x < 0) head.x = GRID_WIDTH - 1;
        if (head.x >= GRID_WIDTH) head.x = 0;
        if (head.y < 0) head.y = GRID_HEIGHT - 1;
        if (head.y >= GRID_HEIGHT) head.y = 0;

        body.insert(body.begin(), head);
        body.pop_back();
    }

    void grow() {
        Point tail = body.back();
        body.push_back(tail);
    }

    const std::vector<Point>& getBody() const {
        return body;
    }

    Point getDirection() const {
        return direction;
    }

    void setDirection(Point newDirection) {
        direction = newDirection;
    }

private:
    std::vector<Point> body;
    Point direction;
};

Point generateFood() {
    return {rand() % GRID_WIDTH, rand() % GRID_HEIGHT};
}

void drawGame(const Snake& snake, const Point& food) {
    for (int y = 0; y < GRID_HEIGHT; ++y) {
        for (int x = 0; x < GRID_WIDTH; ++x) {
            bool isSnake = false;
            for (const auto& part : snake.getBody()) {
                if (part.x == x && part.y == y) {
                    isSnake = true;
                    break;
                }
            }

            if (isSnake) {
                std::cout << "O";
            } else if (x == food.x && y == food.y) {
                std::cout << "F";
            } else {
                std::cout << " ";
            }
        }
        std::cout << std::endl;
    }
}

int main() {
    srand(time(NULL));
    Snake snake;
    Point food = generateFood();

    bool running = true;
    while (running) {
        if (std::cin.peek() != EOF) {
            char key;
            std::cin >> key;
            Point newDirection = snake.getDirection();
            switch (key) {
                case 'w':
                    if (newDirection.y != 1) newDirection = {0, -1};
                    break;
                case 's':
                    if (newDirection.y != -1) newDirection = {0, 1};
                    break;
                case 'a':
                    if (newDirection.x != 1) newDirection = {-1, 0};
                    break;
                case 'd':
                    if (newDirection.x != -1) newDirection = {1, 0};
                    break;
            }
            snake.setDirection(newDirection);
        }

        snake.move();

        if (snake.getBody().front().x == food.x && snake.getBody().front().y == food.y) {
            snake.grow();
            food = generateFood();
        }

        drawGame(snake, food);

        for (int i = 0; i < 10000000; ++i) {}
    }

    return 0;
}
