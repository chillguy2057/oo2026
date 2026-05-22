package com.demo;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.Comparator;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping
public class Controller {

    final AutoRepo ar; final OmanikRepo or; final SoidupaevikuRepo sr;
    Controller(AutoRepo ar, OmanikRepo or, SoidupaevikuRepo sr) {
        this.ar = ar; this.or = or; this.sr = sr;
    }

    //Autod
    @GetMapping("/autod/mark/{mark}")
    List<Auto> byMark(@PathVariable String mark) { return ar.findByMark(mark); }

    @GetMapping("/autod/pikkus/{min}/{max}")
    List<Auto> byPikkus(@PathVariable double min, @PathVariable double max) { return ar.findByPikkusBetween(min, max); }

    @GetMapping("/autod/mass/{min}/{max}")
    List<Auto> byMass(@PathVariable double min, @PathVariable double max) { return ar.findByMassBetween(min, max); }

    @PostMapping("/auto")
    ResponseEntity<?> addAuto(@RequestBody Auto a) {
        if (a.getMass() > 3500) return ResponseEntity.badRequest().body("Viga: mass ei tohi ületada 3500 kg!");
        return ResponseEntity.ok(ar.save(a));
    }

    // Omanik
    @PostMapping("/omanik")
    Omanik addOmanik(@RequestBody Omanik o) { return or.save(o); }

    @GetMapping("/omanik/{id}/autod")
    List<Auto> omanikAutod(@PathVariable Long id) { return or.findById(id).orElseThrow().getAutod(); }

    @GetMapping("/omanik/{id}/pikim")
    Auto pikim(@PathVariable Long id) {
        return or.findById(id).orElseThrow().getAutod().stream()
                .max(Comparator.comparingDouble(Auto::getPikkus)).orElseThrow();
    }

    @GetMapping("/omanik/{id}/raskem")
    Auto raskem(@PathVariable Long id) {
        return or.findById(id).orElseThrow().getAutod().stream()
                .max(Comparator.comparingDouble(Auto::getMass)).orElseThrow();
    }

    // Soidupaeviku
    @PostMapping("/soidupaeviku")
    Soidupaeviku addSoidupaeviku(@RequestBody Soidupaeviku s) { return sr.save(s); }

    @GetMapping("/auto/{id}/kogukm")
    Map<String,Double> autoKm(@PathVariable Long id) { return Map.of("kogukm", sr.sumByAutoId(id)); }

    @GetMapping("/omanik/{id}/kogukm")
    Map<String,Double> omanikKm(@PathVariable Long id) {
        double km = or.findById(id).orElseThrow().getAutod().stream()
                .mapToDouble(a -> sr.sumByAutoId(a.getId())).sum();
        return Map.of("kogukm", km);
    }
}
