public class Ring implements Kujund {
    private double raadius;

    public Ring(double raadius) {
        this.raadius = raadius;
    }

    @Override
    public double arvutaPindala() {
        return Math.PI * raadius * raadius;
    }

    @Override
    public double arvutaÜmbermõõt() {
        return 2 * Math.PI * raadius;
    }

    @Override
    public String annaNimi() {
        return "Ring raadiusega " + raadius;
    }
}
