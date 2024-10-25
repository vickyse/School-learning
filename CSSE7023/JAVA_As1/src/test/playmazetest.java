package test;

import Model.Position;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class playmazetest {

    @Test
    public void positionmoveup() {
        Position testPosition = new Position(0, 0);
        testPosition.moveUp();
        Assertions.assertEquals(-1, testPosition.getyCoordinate());
    }
    @Test
    public void positionmovedown() {
        Position testPosition = new Position(0, 0);
        testPosition.moveDown();
        Assertions.assertEquals(1, testPosition.getyCoordinate());
    }
    @Test
    public void positionmoveleft() {
        Position testPosition = new Position(0, 0);
        testPosition.moveLeft();
        Assertions.assertEquals(-1, testPosition.getxCoordinate());
    }
    @Test
    public void positionmoveright() {
        Position testPosition = new Position(0, 0);
        testPosition.moveRight();
        Assertions.assertEquals(1, testPosition.getxCoordinate());
    }
}
