public class Ristkülik implements Kujund {
    private double külgA;
    private double külgB;

    public Ristkülik(double külgA, double külgB) {
        this.külgA = külgA;
        this.külgB = külgB;
    }

    @Override
    public double arvutaPindala() {
        return külgA * külgB;
    }

    @Override
    public double arvutaÜmbermõõt() {
        return 2 * (külgA + külgB);
    }

    @Override
    public String annaNimi() {
        return "Ristkülik mõõtudega " + külgA + "x" + külgB;
    }
}
