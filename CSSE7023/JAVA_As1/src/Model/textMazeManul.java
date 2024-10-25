package Model;
import java.util.Scanner;

/**
 * the class `textMazeManul`, when user choose to show maze in text and want to play the maze , this class would be
 * called. It provides all methods would be used to play the maze.
 */
public class textMazeManul {

    /**
     * Solve maze, it won't return anything, the interaction to user and result of maze would be printed in terminal.
     *
     * @param maze the maze that `FileLoader` has loaded.
     */
    public static void playMaze(char[][] maze) {

        Position start = new Position(0, 0);
        Position end = new Position(0, 0);

        for (int i = 0; i < maze.length; i++) { //垂直遍歷
            for (int j = 0; j < maze[0].length; j++) { //水平遍歷
                if (maze[i][j] == 'S') {
                    start = new Position(i, j);
                } else if (maze[i][j] == 'E') {
                    end = new Position(i, j);
                }
            }
        } // 定義起點與終點
        System.out.println("");
        for (int i = 0; i < maze.length; i++) {
            maze[start.yCoordinate][start.xCoordinate] = 'G';
            System.out.println(maze[i]);
        } //打印出地圖並把S改成G

        Position goose = new Position(start.yCoordinate, start.xCoordinate); //定義手動迷宮的角色鵝，起始點與起點一樣。
        textMazeManul.playMazeModel(maze, end, goose);
    }

    /**
     * Program and interaction to users.
     *
     * @param maze     the maze.
     * @param endPoint end of the maze.
     * @param theGoose The goose! Replace start point.
     */
    static void playMazeModel(char[][] maze, Position endPoint, Position theGoose) {
        Scanner scanner = new Scanner(System.in);
        while (!theGoose.equals(endPoint)) {
            System.out.println("Which direction do you wan to go?");
            System.out.println("You can enter Up, Down, Left, Right: ");
            String answer = scanner.nextLine();

            if (maze[theGoose.yCoordinate][theGoose.xCoordinate] != 'S') {
                maze[theGoose.yCoordinate][theGoose.xCoordinate] = ' ';
            } // place only a single 'G' in the maze.

            if (!answer.equalsIgnoreCase("up")
                    && !answer.equalsIgnoreCase("down")
                    && !answer.equalsIgnoreCase("left")
                    && !answer.equalsIgnoreCase("right")) {
                System.out.println("Please enter Up, Down, Left, Right: ");
                answer = scanner.nextLine();
                moveGoose(theGoose, answer);
            } else {
                moveGoose(theGoose, answer);
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
            } // deal if the move reach the wall.

            System.out.println("");
            System.out.println("Your now in the maze at: ");
            for (int i = 0; i < maze.length; i++) {
                maze[theGoose.yCoordinate][theGoose.xCoordinate] = 'G';
                System.out.println(maze[i]);
            } //print maze after a move.
        }

        System.out.println("You escape the maze, congrats!");
        scanner.close();
    }

    private static void moveGoose(Position theGoose, String answer) {
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
}
