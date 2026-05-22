package com.demo;
import jakarta.persistence.*;
import java.util.List;
import jakarta.persistence.CascadeType;

@Entity
public class Auto {
    @Id @GeneratedValue Long id;
    String mark;
    double pikkus;
    double mass;
    @ManyToOne(cascade = CascadeType.ALL) @JoinColumn(name = "omanik_id") Omanik omanik;
    @OneToMany(mappedBy = "auto") List<Soidupaeviku> soidupaevikud;

    public Long getId() { return id; }
    public String getMark() { return mark; }
    public double getPikkus() { return pikkus; }
    public double getMass() { return mass; }
    public Omanik getOmanik() { return omanik; }
    public List<Soidupaeviku> getSoidupaevikud() { return soidupaevikud; }
    public void setMark(String mark) { this.mark = mark; }
    public void setPikkus(double pikkus) { this.pikkus = pikkus; }
    public void setMass(double mass) { this.mass = mass; }
    public void setOmanik(Omanik omanik) { this.omanik = omanik; }
}
