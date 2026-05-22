package com.demo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import java.util.List;

interface OmanikRepo extends JpaRepository<Omanik, Long> {}

interface AutoRepo extends JpaRepository<Auto, Long> {
    List<Auto> findByMark(String mark);
    List<Auto> findByPikkusBetween(double min, double max);
    List<Auto> findByMassBetween(double min, double max);
}

interface SoidupaevikuRepo extends JpaRepository<Soidupaeviku, Long> {
    @Query("SELECT COALESCE(SUM(s.km),0) FROM Soidupaeviku s WHERE s.auto.id = :id")
    double sumByAutoId(Long id);
}
