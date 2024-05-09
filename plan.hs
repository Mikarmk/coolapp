import System.IO

data Task = Task { taskId :: Int, taskName :: String, taskDone :: Bool } deriving (Show)

type TaskList = [Task]

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering
    taskLoop []

taskLoop :: TaskList -> IO ()
taskLoop tasks = do
    putStrLn "Менеджер задач"
    putStrLn "1. Показать задачи"
    putStrLn "2. Добавить задачу"
    putStrLn "3. Отметить задачу как выполненную"
    putStrLn "4. Удалить задачу"
    putStrLn "5. Выйти"
    putStrLn "Выберите действие:"
    choice <- getLine
    case choice of
        "1" -> do
            showTasks tasks
            taskLoop tasks
        "2" -> do
            newTasks <- addTask tasks
            taskLoop newTasks
        "3" -> do
            newTasks <- markTaskDone tasks
            taskLoop newTasks
        "4" -> do
            newTasks <- deleteTask tasks
            taskLoop newTasks
        "5" -> putStrLn "До свидания!"
        _ -> do
            putStrLn "Некорректный выбор. Попробуйте снова."
            taskLoop tasks

showTasks :: TaskList -> IO ()
showTasks tasks = do
    putStrLn "Список задач:"
    mapM_ print tasks

addTask :: TaskList -> IO TaskList
addTask tasks = do
    putStrLn "Введите название новой задачи:"
    name <- getLine
    let newTaskId = if null tasks then 1 else taskId (last tasks) + 1
    let newTask = Task newTaskId name False
    return (tasks ++ [newTask])

markTaskDone :: TaskList -> IO TaskList
markTaskDone tasks = do
    putStrLn "Введите ID задачи, которую хотите отметить как выполненную:"
    taskIdStr <- getLine
    let taskIdInt = read taskIdStr :: Int
    let updatedTasks = map (\task -> if taskId task == taskIdInt then task { taskDone = True } else task) tasks
    return updatedTasks

deleteTask :: TaskList -> IO TaskList
deleteTask tasks = do
    putStrLn "Введите ID задачи, которую хотите удалить:"
    taskIdStr <- getLine
    let taskIdInt = read taskIdStr :: Int
    let updatedTasks = filter (\task -> taskId task /= taskIdInt) tasks
    return updatedTasks
