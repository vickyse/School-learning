package Model;
import exception.FileInterface;
import io.FileLoader;

import java.io.FileNotFoundException;
import java.util.Scanner;

public class textMazeManulsketch {
    public static void main(String[] args) throws
            FileNotFoundException,
            FileInterface.MazeSizeMissmatchException,
            FileInterface.MazeMalformedException {
        FileLoader model = new FileLoader();
        char[][] maze = model.load("C:\\Users\\User\\IdeaProjects\\JAVA As1\\src\\test\\test material\\" +
                "medium.txt");

        Position start = new Position(0, 0);
        Position end = new Position(0, 0);

        for (int i = 0 ; i < maze.length ; i++) { //垂直遍歷
            for (int j = 0 ; j < maze[0].length ; j++) { //水平遍歷
                if (maze[i][j] == 'S') {
                    start = new Position(i, j);
                } else if (maze[i][j] == 'E') {
                    end = new Position(i, j);
                }
            }
        } // 定義起點與終點

        for (int i = 0 ; i < maze.length ; i++) {
            maze[start.yCoordinate][start.xCoordinate] = 'G';
            System.out.println(maze[i]);
        } //打印出地圖並把S改成G

        Position goose = new Position(start.yCoordinate, start.xCoordinate); //定義手動迷宮的角色鵝，起始點與起點一樣。
        textMazeManulsketch.playMazeModel(maze, end, goose);
    }

    static void playMazeModel(char[][] maze, Position endPoint, Position theGoose) {
        Scanner scanner = new Scanner(System.in);
        while (!theGoose.equals(endPoint)) { //迴圈一直運行直到到達終點
            System.out.println("Which direction do you wan to go?");
            System.out.println("You can enter Up, Down, Left, Right: ");
            String answer = scanner.nextLine();

            if (maze[theGoose.yCoordinate][theGoose.xCoordinate] != 'S') {
                maze[theGoose.yCoordinate][theGoose.xCoordinate] = ' ';
            } //讓地圖只會有一個鵝的符號

            if (!answer.equalsIgnoreCase("up")
                    && !answer.equalsIgnoreCase("down")
                    && !answer.equalsIgnoreCase("left")
                    && !answer.equalsIgnoreCase("right")) {
                System.out.println("Please enter Up, Down, Left, Right: ");
                scanner.nextLine(); // 清除輸入緩存
            } else {
                if (answer.equalsIgnoreCase("up")) {
                    theGoose.moveUp();
                } else if (answer.equalsIgnoreCase("down")) {
                    theGoose.moveDown();
                } else if (answer.equalsIgnoreCase("left")) {
                    theGoose.moveLeft();
                } else if (answer.equalsIgnoreCase("right")) {
                    theGoose.moveRight();
                }
            }

            if (maze[theGoose.yCoordinate][theGoose.xCoordinate] == '#') {
                System.out.println("You reach the wall!");
                if (answer.equalsIgnoreCase("up")) {
                    theGoose.moveDown();
                } else if (answer.equalsIgnoreCase("down")) {
                    theGoose.moveUp();
                } else if (answer.equalsIgnoreCase("left")) {
                    theGoose.moveRight();
                } else if (answer.equalsIgnoreCase("right")) {
                    theGoose.moveLeft();
                }
                continue;
            } // 處理撞到牆的情況

            System.out.println("Your now in the maze at: ");
            System.out.println("");
            for (int i = 0 ; i < maze.length ; i++) {
                maze[theGoose.yCoordinate][theGoose.xCoordinate] = 'G';
                System.out.println(maze[i]);
            } //打印移動後的地圖
        }

        System.out.println("You escape the maze, congrats!");
        scanner.close();
    }
}
