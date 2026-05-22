package com.demo;
import jakarta.persistence.*;
import java.time.LocalDate;
import jakarta.persistence.CascadeType;

@Entity
public class Soidupaeviku {
    @Id @GeneratedValue Long id;
    LocalDate kuupaev;
    double km;
    @ManyToOne(cascade = CascadeType.ALL) @JoinColumn(name = "auto_id") Auto auto;
    public Long getId() { return id; }
    public double getKm() { return km; }
    public Auto getAuto() { return auto; }
    public void setKuupaev(LocalDate kuupaev) { this.kuupaev = kuupaev; }
    public void setKm(double km) { this.km = km; }
    public void setAuto(Auto auto) { this.auto = auto; }
}
