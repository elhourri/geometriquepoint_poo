public class Point {
    private double x;
    private double y;

    public Point() {
        this.x = 0;
        this.y = 0;
    }

    public Point(double x, double y) {
        this.x = x;
        this.y =y;
    }

    public double get_x() {
        return x;
    }

    public void set_x(double valeur) {
        this.x = valeur;
    }

    public double y() {
        return y;
    }

    public void set_y(double valeur) {
        this.y = valeur;
    }

    public double distance(Point point) {
        return Math.sqrt(Math.pow(this.x - point.x, 2) + Math.pow(this.y - point.y, 2));
    }

    public double norm() {
        return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2));
    }

    public static void main(String[] args) {
        Point point1 = new Point(4, 3);

        System.out.println("Distance: " + point1.distance(new Point(0, 0)));
        System.out.println("Norm: " + point1.norm());
    }
}