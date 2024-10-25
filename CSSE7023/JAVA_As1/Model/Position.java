package Model;


/**
 * Define class `Position`, the object in maze(start, goose, end, wall...etc.) are all a `Position`.
 */
public class Position implements Moveable{

    public int yCoordinate;
    public int xCoordinate;
    public Position lastPoint;

    public Position(int yCoordinate, int xCoordinate, Position lastPoint) {
        this.yCoordinate = yCoordinate;
        this.xCoordinate = xCoordinate;
        this.lastPoint = lastPoint;
    }

    public Position(int yCoordinate, int xCoordinate) {
        this.yCoordinate = yCoordinate;
        this.xCoordinate = xCoordinate;
    }


    /**
     * override the logic of equal in this assignment.
     * @param obj  another position.
     * @return a boolean whether they are at same coordination.
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Position otherPosition = (Position) obj;
        return this.yCoordinate == otherPosition.yCoordinate && this.xCoordinate == otherPosition.xCoordinate;
    }

    /**
     * The implementation of `Moveable` interface.
     */
    @Override
    public void moveUp() {
        this.yCoordinate = yCoordinate - 1;
    }

    @Override
    public void moveDown() {
        this.yCoordinate = yCoordinate + 1;
    }

    @Override
    public void moveLeft() {
        this.xCoordinate = xCoordinate - 1;
    }

    @Override
    public void moveRight() {
        this.xCoordinate = xCoordinate + 1;
    }


    /**
     * get the x coordinate of this point, weill be used for testing.
     * @return the x coordinate of this point
     */
    public int getxCoordinate() {
        return this.xCoordinate;
    }

    /**
     * get the y coordinate of this point, weill be used for testing.
     * @return the y coordinate of this point
     */
    public int getyCoordinate() {
        return this.yCoordinate;
    }
}

