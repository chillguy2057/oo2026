import java.util.ArrayList;

public class Raamatukogu {
    private String raamatukoguNimi;

    private ArrayList<Raamat> raamatud;

    
    public Raamatukogu(String raamatukoguNimi) {
        this.raamatukoguNimi = raamatukoguNimi;
        this.raamatud = new ArrayList<>();
    }

    
    public void lisaRaamat(Raamat raamat) {
        raamatud.add(raamat);
        System.out.println("Süsteemi lisatud: " + raamat.getPealkiri());
    }

    
    public void kuvaKõikRaamatud() {
        System.out.println("\n--- " + raamatukoguNimi + " raamatute nimekiri ---");
        if (raamatud.isEmpty()) {
            System.out.println("Raamatukogu on tühi.");
        } else {
            for (Raamat r : raamatud) {
                System.out.println(r.annaInfo());
            }
        }
    }

    
    public double arvutaKeskmineLehekülgedeArv() {
        if (raamatud.isEmpty()) return 0;
        
        int summa = 0;
        for (Raamat r : raamatud) {
            summa += r.getLehekülgi();
        }
        return (double) summa / raamatud.size();
    }
}
