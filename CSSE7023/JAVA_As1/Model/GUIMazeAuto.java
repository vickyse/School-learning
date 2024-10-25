package Model;

import exception.FileInterface;
import io.FileLoader;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;


/**
 * This is a class when user choose to show maze as GUI and also want maze be solved automatically.
 */
public class GUIMazeAuto {

    /**
     * The making process of it is to first using text to solve the maze, and transfer it into GUI version.
     * @param maze the maze that has been solved in text.
     */
    public static void showResult(char[][] maze) {
        JFrame GUI = new JFrame();
        GUI.setTitle("Maze game");
        GUI.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        GUI.setSize(800, 800);
        GUI.setVisible(true);

        JPanel mazePanel = new JPanel();
        mazePanel.setLayout(new GridLayout(maze.length, maze[0].length));
        GUI.add(mazePanel);

        JMenuBar menuBar = new JMenuBar();
        GUI.setJMenuBar(menuBar);
        JMenu fileMenu = new JMenu("File");
        menuBar.add(fileMenu);
        JMenuItem openMenuItem = new JMenuItem("Load another maze file");
        fileMenu.add(openMenuItem); // Create and define the GUI frame.

        openMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                GUI.dispose();
                JFileChooser fileChooser = new JFileChooser();
                int result = fileChooser.showOpenDialog(null);

                if (result == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    String filePath = selectedFile.getAbsolutePath();

                    FileLoader loader = new FileLoader();
                    try {
                        char[][] reloadedMaze = loader.load(filePath);

                        char[][] textResult = textMazeAuto.solveMaze(reloadedMaze, true);
                        GUIMazeAuto.showResult(textResult);
                    } catch (FileNotFoundException ex) {
                    } catch (FileInterface.MazeSizeMissmatchException ex) {
                    } catch (FileInterface.MazeMalformedException ex) {
                    } catch (IllegalArgumentException ex) {
                    }
                }
            }
        });


        for (char[] chars : maze) {
            for (int j = 0; j < maze[0].length; j++) {
                char cell = chars[j];
                JPanel cellPanel = new JPanel();

                if (cell == '#') {
                    cellPanel.setBackground(Color.BLACK);
                } else if (cell == 'S') {
                    cellPanel.setBackground(Color.GREEN);
                } else if (cell == 'E') {
                    cellPanel.setBackground(Color.RED);
                } else if (cell == 'P') {
                    cellPanel.setBackground(Color.BLUE);
                }
                mazePanel.add(cellPanel);
            }
        }
        GUI.revalidate();
        //GUI.repaint();
    }
}
