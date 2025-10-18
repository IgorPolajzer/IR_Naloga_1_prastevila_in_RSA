# Naloga 1 - Praštevila in RSA

## Naloga 1.1

---
### Tvorjenje naključnih števil
Nalogo sem pričel tako da sem ustvarili generator naključnih števil LCG z parametri Super-Duper.

**Histrogram 1000000 naključnih števil na intervalu [1, 1000]**

<div style="display: flex; justify-content: space-between;">
    <img src="images/generator_gui.png" alt="Generator GUI" style="width: 45%;"/>
    <img src="images/random_number_histogram.png" alt="Random Number Histogram" style="width: 45%;"/>
</div>

Ugotovitve: Generator deluje pravilno, saj so verjetnosti pojavitve posameznega števila relativno blizu.

---
### Generiranje preštevil

V GUI sem dodal možnosti za:
- Testiranje poljubnega števila z testom Miller-Rabin
<div style="display: flex; justify-content: space-between;">
    <img src="images/miller_rabin_test_composite.png" alt="Miller Rabin Test Prime" style="width: 45%;"/>
    <img src="images/miller_rabin_test_prime.png" alt="Miller Rabin Test Composite" style="width: 45%;"/>
</div>

- Testiranje poljubnega števila z naivnim testom
<div style="display: flex; justify-content: space-between;">
    <img src="images/test_naive_prime.png" alt="Naive Test Prime" style="width: 45%;"/>
    <img src="images/test_naive_composite.png" alt="Naive Test Composite" style="width: 45%;"/>
</div>

- Generiranje praštevila z testom Miller-Rabin
- Generiranje praštevila z naivnim testom
- Izris grafa za generiranje praštevil glede na n (bite števila) in čas generiranja
  - n -> [4, 32]
  - generiranjem sem zagnal tri krat in izračunal povprečje ter ga vstavil v graf
  - <div style="display: flex; justify-content: space-between;">
      <img src="images/miller_rabin_graph.png" alt="Milelr Rabin Graph" style="width: 45%;"/>
      <img src="images/naive_graph.png" alt="Naive Graph" style="width: 45%;"/>
    </div>
  - Nato sem grafa obeh algoirmtov še primerjal (oranžna - Miller-Rabin, modra: Naiven pristop)
  - <div style="display: flex; justify-content: space-between;">
      <img src="images/comparison_graph.png" alt="Comparison Graph" style="width: 45%;"/>
    </div>

**Ugotovitve**: Opazimo da pri naivnem pristopu čas generiranja nasrašča skoraj da exponentno glede na število bitov
zgeneriranega praštevila, medtem ko pristop z Miller-Rabin testiranjem bolj ali manj ohranja isto časovno zahtevnost.
