import Model.GUIMazeManual;
import Model.textMazeAuto;
import Model.textMazeManul;
import Model.GUIMazeAuto;
import exception.FileInterface;
import io.FileLoader;
import java.io.FileNotFoundException;
import java.util.Objects;
import java.util.Scanner;

/**
 * Main function of the assignment.
 */
public class Launcher {
    public static void main(String[] args) throws
            FileNotFoundException,
            FileInterface.MazeSizeMissmatchException,
            FileInterface.MazeMalformedException{
        boolean useText = true;
        String filename = null;

        for (String arg : args) {
            if (arg.toUpperCase().contains("GUI")) {
                useText = false;
            } else if (arg.endsWith("txt")) {
                filename = arg;
            }
        }

        FileLoader loader = new FileLoader();
        char[][] maze = loader.load(filename);
        boolean userWantMazeSolvedAutolly = userWantMazeSolvedAutolly();
        //determine using GUI or text, and read the maze file as well.

        if (useText) {
            if (userWantMazeSolvedAutolly) {
                textMazeAuto.solveMaze(maze, false);
            } else {
                textMazeManul.playMaze(maze);
            }
        } else { // using GUI to show maze.
            if (userWantMazeSolvedAutolly) {
                char[][] textResult = textMazeAuto.solveMaze(maze, true);
                GUIMazeAuto.showResult(textResult);
            } else {
                // TODO:GUIMazeManual()
            }
        }
    }

    /**
     * Interaction to makes sure users want to play maze or solve maze automatically.
     * @return boolean of answer.
     */
    public static boolean userWantMazeSolvedAutolly() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome!");
        System.out.println("Do you want to play the maze by yourself or have it solved automatically?");
        System.out.println("Type 'play it' to play it yourself or 'solve it' to have it solved");
        System.out.println("If solved it, it would return the maze can be solved or not in T/F");
        System.out.println("And if T, solution will also printed.");
        String answer = scanner.nextLine();
        if (Objects.equals(answer, "solve it")) {
            return true;
        } else if (Objects.equals(answer, "play it")) {
            return false;
        } else {
            return userWantMazeSolvedAutolly();
        }
    }
}
