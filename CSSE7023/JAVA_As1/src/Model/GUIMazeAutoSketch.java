package Model;

import exception.FileInterface;
import io.FileLoader;

import java.io.FileNotFoundException;

public class GUIMazeAutoSketch {
    public static void main(String[] args) throws
            FileNotFoundException,
            FileInterface.MazeSizeMissmatchException,
            FileInterface.MazeMalformedException {
        FileLoader model = new FileLoader();
        char[][] maze = model.load("C:\\Users\\User\\IdeaProjects\\JAVA As1\\src\\test\\test material\\" +
                "medium.txt");
        char[][] textResult = textMazeAuto.solveMaze(maze, true);
        GUIMazeAuto.showResult(textResult);
    }
}
