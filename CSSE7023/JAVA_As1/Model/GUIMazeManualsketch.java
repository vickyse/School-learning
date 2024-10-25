package Model;

import exception.FileInterface;
import io.FileLoader;

import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.FileNotFoundException;

public class GUIMazeManualsketch {
    public static void main(String[] args) throws
            FileNotFoundException,
            FileInterface.MazeSizeMissmatchException,
            FileInterface.MazeMalformedException {
        FileLoader model = new FileLoader();
        char[][] maze = model.load("C:\\Users\\User\\IdeaProjects\\JAVA As1\\src\\test\\test material\\" +
                "large.txt");

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

        for (int i = 0; i < maze.length; i++) {
            maze[start.yCoordinate][start.xCoordinate] = 'G';
        } //把S改成G

        Position goose = new Position(start.yCoordinate, start.xCoordinate); //定義手動迷宮的角色鵝，起始點與起點一樣。

        playMaze(maze, goose, end);
    }

    private static void playMaze(char[][] maze, Position goose, Position end) {
        createFrame(maze, goose, end);
    }

    private static void createFrame(char[][] maze, Position goose, Position end) {
        JFrame GUI = new JFrame();
        GUI.setTitle("Maze game");
        GUI.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel mazePanel = new JPanel();
        mazePanel.setLayout(new GridLayout(maze.length, maze[0].length));

        GUI.add(mazePanel);
        GUI.setSize(800, 800);
        GUI.setVisible(true);

        KeyListener listener = new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
            }

            @Override
            public void keyPressed(KeyEvent e) {
                int key = e.getKeyCode();
                if (key == KeyEvent.VK_SPACE) {
                    System.out.println("GG");
                } else if (key == KeyEvent.VK_W) {
                    System.out.println('w');
                    goose.moveUp();
                    System.out.println(goose.yCoordinate + "," + goose.xCoordinate);
                    reDrawGUI(maze, mazePanel, GUI);
                } else if (key == KeyEvent.VK_A) {
                    System.out.println('a');
                    goose.moveLeft();
                    reDrawGUI(maze, mazePanel, GUI);
                } else if (key == KeyEvent.VK_S) {
                    System.out.println('s');
                    goose.moveDown();
                    reDrawGUI(maze, mazePanel, GUI);
                } else if (key == KeyEvent.VK_D) {
                    System.out.println('d');
                    goose.moveRight();
                    reDrawGUI(maze, mazePanel, GUI);
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
            }
        };

        GUI.addKeyListener(listener);
        drawGUI(maze, mazePanel, GUI);
    }
    public static void drawGUI(char[][] maze, JPanel mazePanel, JFrame GUI) {

        for (char[] chars : maze) {
            for (int j = 0; j < maze[0].length; j++) {
                char cell = chars[j];
                JPanel cellPanel = new JPanel();

                if (cell == '#') {
                    cellPanel.setBackground(Color.BLACK);
                } else if (cell == 'G') {
                    cellPanel.setBackground(Color.GREEN);
                } else if (cell == 'E') {
                    cellPanel.setBackground(Color.RED);
                }
                mazePanel.add(cellPanel);
            }
        }
        GUI.add(mazePanel);
        GUI.revalidate();
        GUI.repaint();
    }

    private static void reDrawGUI(char[][] maze, JPanel mazePanel, JFrame GUI) {
        mazePanel.removeAll();

        for (char[] chars : maze) {
            for (int j = 0; j < maze[0].length; j++) {
                char cell = chars[j];
                JPanel cellPanel = new JPanel();

                if (cell == '#') {
                    cellPanel.setBackground(Color.BLACK);
                } else if (cell == 'G') {
                    cellPanel.setBackground(Color.GREEN);
                } else if (cell == 'E') {
                    cellPanel.setBackground(Color.RED);
                }
                mazePanel.add(cellPanel);
            }
        }
        GUI.add(mazePanel);
        GUI.revalidate();
        GUI.repaint();
    }
}
