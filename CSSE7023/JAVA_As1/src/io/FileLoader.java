package io;

import exception.FileInterface;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;

/**
 * The implementation of FileLoader.
 */
public class FileLoader implements FileInterface {

    /**
     * load() method would take a txt format file, transfer it into 2D array.
     * @param filename The path to the maze file to be loaded.
     * @return 2D array of maze from specified maze(txt file).
     * @throws MazeMalformedException if the maze data doesn't match the given format.
     * @throws MazeSizeMissmatchException if the maze data doesn't match the specified dimensions or the length or width
     * of maze is an even integer.
     * @throws IllegalArgumentException for other general validation errors, such as invalid characters.
     * @throws FileNotFoundException if the specified maze file is not found.
     */
    @Override
    public char[][] load(String filename) throws MazeMalformedException,
            MazeSizeMissmatchException,
            IllegalArgumentException,
            FileNotFoundException {
        if (!filename.endsWith(".txt")) {
            throw new MazeMalformedException();
        }

        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String mazeSize = br.readLine();
            String[] mazeheightAndLength = mazeSize.split(" ");

            int mazeheight = Integer.parseInt(mazeheightAndLength[0]);
            int mazeLength = Integer.parseInt(mazeheightAndLength[1]);

            if (mazeheight % 2 == 0 || mazeLength % 2 == 0) {
                throw new MazeSizeMissmatchException();
            }

            char[][] maze = new char[mazeheight][mazeLength];
            String line;
            int count = 0;
            while ((line = br.readLine()) != null) {

                char[] oneRowInMaze = line.toCharArray();
                maze[count] = oneRowInMaze; //write a row from file to maze.

                for (int i = 0; i < mazeLength - 1; i++) {
                    if (maze[count][i] != 'S'
                            && maze[count][i] != 'E'
                            && maze[count][i] != ' '
                            && maze[count][i] != '#') {
                        throw  new IllegalArgumentException();
                    }
                } //with for and while loop, check all char in file if it contains illegal char.

                count = count + 1;

                if (oneRowInMaze.length != mazeLength) {
                    throw new MazeSizeMissmatchException();
                }
            }
            if (count != mazeheight) { // if actual height of the maze != record.
                throw new MazeSizeMissmatchException();
            }
            return maze;

        } catch (FileNotFoundException fileNotFoundException) {
            throw new FileNotFoundException();
        } catch (IOException ioException) {
            throw new IllegalArgumentException();
        }
    }
}
