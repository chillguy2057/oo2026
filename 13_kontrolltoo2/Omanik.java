package com.demo;
import jakarta.persistence.*;
import java.util.List;

@Entity
public class Omanik {
    @Id @GeneratedValue Long id;
    String nimi;
    @OneToMany(mappedBy = "omanik") List<Auto> autod;

    public Long getId() { return id; }
    public String getNimi() { return nimi; }
    public List<Auto> getAutod() { return autod; }
    public void setNimi(String nimi) { this.nimi = nimi; }
}
