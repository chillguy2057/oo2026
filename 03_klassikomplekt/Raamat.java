public class Raamat {
    // Klassi väljad (omadused)
    private String pealkiri;
    private String autor;
    private int lehekülgi;

    // Konstruktor uue raamatu loomiseks
    public Raamat(String pealkiri, String autor, int lehekülgi) {
        this.pealkiri = pealkiri;
        this.autor = autor;
        this.lehekülgi = lehekülgi;
    }

    // Getterid, et teised klassid saaksid andmeid lugeda
    public String getPealkiri() { return pealkiri; }
    public String getAutor() { return autor; }
    public int getLehekülgi() { return lehekülgi; }

    // Meetod raamatu info ilusaks väljastamiseks
    public String annaInfo() {
        return '"' + pealkiri + '"' + " - " + autor + " (" + lehekülgi + " lk.)";
    }
}
