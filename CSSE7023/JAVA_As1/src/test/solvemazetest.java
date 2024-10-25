package test;

import Model.Position;
import Model.textMazeAuto;
import exception.FileInterface;
import io.FileLoader;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Queue;

public class solvemazetest {
    int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    @Test
    public void mazeHasSolution() throws FileNotFoundException,
            FileInterface.MazeSizeMissmatchException,
            FileInterface.MazeMalformedException {

        String filename = "/Users/linker0730/Desktop/JAVA As1/src/test/test material/small.txt";
        FileLoader model = new FileLoader();
        char[][] maze = model.load(filename);
        Queue<Position> points = new LinkedList<>();
        boolean[][] visitedpath = new boolean[maze.length][maze[0].length];

        Position start = new Position(0, 0);
        Position end = new Position(0, 0);

        for (int i = 0 ; i < maze.length ; i++) {
            for (int j = 0 ; j < maze[0].length ; j++) {
                if (maze[i][j] == 'S') {
                    start = new Position(i, j);
                } else if (maze[i][j] == 'E') {
                    end = new Position(i, j);
                }
            }
        }
        boolean result = textMazeAuto.mazeCanBeSolve(points, start, end, maze, visitedpath, directions);
        Assertions.assertTrue(result);
    }

    @Test
    public void mazeHasNoSolution() throws FileNotFoundException,
            FileInterface.MazeSizeMissmatchException,
            FileInterface.MazeMalformedException {
        String filename = "/Users/linker0730/Desktop/JAVA As1/src/test/test material/no_solution_maze.txt";
        FileLoader model = new FileLoader();
        char[][] maze = model.load(filename);
        Queue<Position> points = new LinkedList<>();
        boolean[][] visitedpath = new boolean[maze.length][maze[0].length];

        Position start = new Position(0, 0);
        Position end = new Position(0, 0);

        for (int i = 0 ; i < maze.length ; i++) {
            for (int j = 0 ; j < maze[0].length ; j++) {
                if (maze[i][j] == 'S') {
                    start = new Position(i, j);
                } else if (maze[i][j] == 'E') {
                    end = new Position(i, j);
                }
            }
        }
        boolean result = textMazeAuto.mazeCanBeSolve(points, start, end, maze, visitedpath, directions);
        Assertions.assertFalse(result);
    }

}

