package Model;
import java.util.LinkedList;
import java.util.Queue;

/**
 * the class `textMazeAuto`, when user choose to show maze in text and want to solve the maze automatically, this class
 * would be called. It provides all methods would be used to solve the maze.
 */
public class textMazeAuto {

    /**
     * Solve maze, it won't return anything, the interaction to user and result of maze would be printed in terminal.
     * @param maze the maze that `FileLoader` has loaded.
     */
    public static char[][] solveMaze(char[][] maze, boolean usingGUIOrNot) {
        Position start = new Position(0, 0);
        Position end = new Position(0, 0);

        // determine the position of start and end.
        for (int i = 0 ; i < maze.length ; i++) {
            for (int j = 0 ; j < maze[0].length ; j++) {
                if (maze[i][j] == 'S') {
                    start = new Position(i, j);
                } else if (maze[i][j] == 'E') {
                    end = new Position(i, j);
                }
            }
        }

        // Define the useful tool would be used in `mazeCanBeSolve`.
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        boolean[][] visitedpath = new boolean[maze.length][maze[0].length];
        // 創立一個可知地圖哪邊走哪邊沒走過的相同二維數組
        Queue<Position> points = new LinkedList<>(); // 隊列

        boolean result = textMazeAuto.mazeCanBeSolve(points, start, end, maze, visitedpath, directions);
        System.out.println("");
        if (!usingGUIOrNot) {
            if (result) {
                System.out.println("The maze can be result?: " + result);
                System.out.println("The result of maze is: ");
                for (char[] row : maze) {
                    System.out.println(row);
                } // 在迷宮走完之後，應該要印出一個已經完成的迷宮
            } else {
                System.out.println("The maze can be result?: " + result);
            }
        }
        return maze;
    }

    /**
     * Critical program to automatically solve the maze.
     * @param points the linked-queue to store the current point.
     * @param start the start of the maze.
     * @param end the end of the maze.
     * @param maze the maze.
     * @param visitedPath a 2D array to store the path that has been visited, avoid program go back when solving the
     *                    maze.
     * @param directions the direction current point is taking.
     * @return boolean if program can reach the end.
     */
    public static boolean mazeCanBeSolve(
            Queue<Position> points,
            Position start,
            Position end,
            char[][] maze,
            boolean[][] visitedPath,
            int[][] directions) {
        points.add(start);
        while (!points.isEmpty()) {
            // with `currentpoints.add(nextPosition);` below, while loop would run until the maze
            // is solved or the maze has no result.
            Position currentPosition = points.poll(); // get info of current position.
            for (int[] goingDirection : directions) {
                Position nextPosition = new Position(
                        currentPosition.yCoordinate + goingDirection[0],
                        currentPosition.xCoordinate + goingDirection[1],
                        currentPosition);
                if (nextPosition.yCoordinate >= 1
                        && nextPosition.yCoordinate <= maze.length
                        && nextPosition.xCoordinate >= 1
                        && nextPosition.xCoordinate <= maze[0].length
                        // position cannot go beyond the maze.
                        && maze[nextPosition.yCoordinate][nextPosition.xCoordinate] != '#'
                        && !visitedPath[nextPosition.yCoordinate][nextPosition.xCoordinate]) {
                    if (nextPosition.equals(end)) {
                        textMazeAuto.getPath(maze, currentPosition, start);
                        return true;
                    }
                    visitedPath[nextPosition.yCoordinate][nextPosition.xCoordinate] = true;
                    points.add(nextPosition);
                    // next position is not the end of maze, keep searching.
                }
            }
        }
        return false;
    }

    /**
     * Show the path to escape the maze, the program would.
     * @param maze the maze.
     * @param currentPosition current position, starts at the end.
     * @param start start point at maze.
     */
    private static void getPath(char[][] maze, Position currentPosition, Position start) {
        while (!currentPosition.equals(start)) {
            maze[currentPosition.yCoordinate][currentPosition.xCoordinate] = 'P';
            currentPosition = currentPosition.lastPoint;
            // show the path when finish the maze.
        }
    }
}

