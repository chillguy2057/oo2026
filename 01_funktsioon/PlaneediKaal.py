public class Kehamass {

    public static void main(String[] args) {
        // Näidisandmed testimiseks
        double kaal = 75.5; // kilogrammides
        double pikkus = 1.82; // meetrites

        // Kutsume välja oma loodud funktsiooni
        double kmi = arvutaKMI(kaal, pikkus);

        // Demonstreerime tulemust ja jagame harivat infot
        System.out.println("=== Hariv tervisefunktsioon ===");
        System.out.println("Inimese kaal: " + kaal + " kg");
        System.out.println("Inimese pikkus: " + pikkus + " m");
        System.out.println("Arvutatud kehamassiindeks (KMI) on: " + String.format("%.2f", kmi));
        
        System.out.println("\nHariv teadmine:");
        System.out.println("Normaalne ja tervislik KMI vahemik on 18.5 kuni 24.9.");
        
        if (kmi < 18.5) {
            System.out.println("Hinnang: Alakaal. Tuleks jälgida toitumist.");
        } else if (kmi >= 18.5 && kmi <= 24.9) {
            System.out.println("Hinnang: Normaalkaal. Suurepärane, hoia seda!");
        } else {
            System.out.println("Hinnang: Ülekaal. Tasuks pöörata tähelepanu liikumisele.");
        }
    }

    /**
     * Funktsioon arvutab kehamassiindeksi.
     * Valem: kaal (kg) jagatud pikkuse ruuduga (m^2).
     */
    public static double arvutaKMI(double kaalKilogrammides, double pikkusMeetrites) {
        // Matemaatiline tehe: kaal / (pikkus * pikkus)
        return kaalKilogrammides / (pikkusMeetrites * pikkusMeetrites);
    }
}
