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

## Naloga 1.2

V implementaicji naloge 1.2 se je podprla implementacija kriptiranja in dekriptiranja datotek z algoritmom RSA,
v kateri sem za ustvarjanje ključev uporabljal generator praštevil ustvarjen v nalogi 1.1.

**Posodobljen GUI**
<div style="display: flex; justify-content: space-between;">
      <img src="images/naloga_1_2_gui.png" alt="Comparison Graph" style="width: 45%;"/>
</div>

---

### Generiranje ključev

**Primerjava generiranja ključev generiranjem ključev** z različnima metodama generiranja praštevil 
(ključi so bili generirani v naslednjih bitnih velikostih: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]).
- Naivna metoda
<div style="display: flex; justify-content: space-between;">
      <img src="images/naive_key_generation.png" alt="Comparison Graph" style="width: 45%;"/>
</div>

- Miller rabin
<div style="display: flex; justify-content: space-between;">
      <img src="images/miller_rabin_key_generation.png" alt="Comparison Graph" style="width: 45%;"/>
</div>

- Primerjava obeh na enem grafu
<div style="display: flex; justify-content: space-between;">
      <img src="images/comparison_key_generation.png" alt="Comparison Graph" style="width: 45%;"/>
</div>

---

## Enkripcija/Dekripcija datotek

**Primerjava časa izvajanja enkripcije in dekripcije** poljubnega n bitnega števila (n je bil na intervalu [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
ob enem pa je na RSA ključ bil tudi n biten). Vsako iteracijo se je izvedlo 5 enkripcij in dekripcij z RSA algoritmom in se v graf vstavilo povprečje za n.

<div style="display: flex; justify-content: space-between;">
      <img src="images/ecryption_decryption_comparison.png" alt="Comparison Graph" style="width: 45%;"/>
</div>
