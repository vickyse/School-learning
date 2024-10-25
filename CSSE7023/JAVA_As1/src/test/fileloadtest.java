package test;

import static org.junit.jupiter.api.Assertions.*;

import exception.FileInterface;
import io.FileLoader;
import org.junit.jupiter.api.Test;

import java.io.FileNotFoundException;

/**
 * test all situations would occur while loading maze file.
 */
public class fileloadtest {
    FileLoader loader = new FileLoader();

    /**
     * test if user entered not a txt file.
     */
    @Test
    public void testNottxt() {
        String filename = "validFile.jpg";

        assertThrows(FileInterface.MazeMalformedException.class, () -> {
            char[][] maze = loader.load(filename);
        });
    }

    /**
     * test if user entered not exist file.
     */
    @Test
    public void testFileNotFound() {
        String filename = "notExistFile.txt";
        assertThrows(FileNotFoundException.class, () -> {
            char[][] maze = loader.load(filename);
        });
    }

    /**
     * test if the file user entered an even width or length maze.
     */
    @Test
    public void testMissSize() {
        String filename = "/Users/linker0730/Desktop/JAVA_As1/src/test/test material/" +
                "even_width_and_length_example.txt";
        assertThrows(FileInterface.MazeSizeMissmatchException.class, () -> {
            char[][] maze = loader.load(filename);
        });
    }

    /**
     * test if the file user entered its real width or length is mismacth to it records.
     */
    @Test
    public void testSizeMismatch() {
        String filename = "/Users/linker0730/Desktop/JAVA_As1/src/test/test material/" +
                "recorded_width_and_length_not_match_to_real.txt";
        assertThrows(FileInterface.MazeSizeMissmatchException.class, () -> {
            char[][] maze = loader.load(filename);
        });
    }

    /**
     * test if the file user entered has illegal char in it.
     */
    @Test
    public void testcontainsillegalchar() {
        String filename = "/Users/linker0730/Desktop/JAVA_As1/src/test/test material/" +
                "having_illegal_char.txt";
        assertThrows(IllegalArgumentException.class, () -> {
            char[][] maze = loader.load(filename);
        });
    }
}
