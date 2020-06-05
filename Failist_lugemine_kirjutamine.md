## Failist lugemine ja faili kirjutamine

Kuidas toimub failide töötlemine Pythonis?
Kujutame ette, et meil on olemas fail **_example.txt_** järgmise sisuga:
```python
Hello, World!
Have a nice day.
```

### Faili avamine
Enne, kui hakkame tegelema faili sisu lugemise ja töötlemisega, peame faili avama. Pythonis on selle jaoks olemas sisseehitatud funktsioon open():
```python
  file_object = open('filename', 'mode')
```

- filename - tähistab faili nime koos tüübiga (extension). Meie näitefaili puhul oleks see 'example.txt', mitte ainult 'example'. On võimalik kasutada ka faili täispikka teekonna ('C:\directory\taltech\file.txt'). 
NB! Täispikka teekonda on VAJA kasutada juhul, kui fail ei ole samas kataloogis (eng.k *directory*), kus programm, mis seda faili küsib.
NB!! Pyhtonis tähistab \ erisümboli algust. Antud näites oleks faili nimeks 'C:\directory altech\file.txt', kuna erisümbol \t tähistab TABi. Erisümbolite vältimiseks võib näiteks kasutada kahte kaldkriipsu 'C:\\directory\\taltech\\file.txt' või kasutada spetsiaalset flagi r'C:\directory\taltech\file.txt', kus kõiki sümboleid tõlgendatakse otseselt (raw string).

- mode - tähistab, mida tuleb antud failiga teha. Vaikimisi on selle väärtuseks r ehk read. Muud võimalikud väärtused:

  r ehk read - faili sisu lugemine;
  w ehk write - faili kirjutamine. Selle režiimiga kaasneb faili sisu üle kirjutamine;
  a ehk append - faili kirjutamine ilma eelneva sisu üle kirjutamata. Uus sisu lisatakse faili lõppu;
  r+ ehk read/write - faili lugemine ja muutmine. Kirjutab eelmist sisu üle;
  a+ ehk append and read - faili lugemine ja uue sisu lisamine. Ei kirjuta eelmist sisu üle.

open() tagastab faili objekti (file object), millest (millesse) edasi saab lugeda (kirjutada) andmeid.

### Failist lugemine
Nüüd, kui fail sai avatud, saame hakata tegelema selle sisu lugemisega. Failist lugemine on võimalik järgmistel viisidel:

- **read(size)** - loeb sisse size baiti (sümbolit) ning tagastab need. Juhul, kui size pole määratud, loeb terve faili sisu.
  ```python
  file_object = open('example.txt', 'r')  # Avame faili lugemiseks
  print(file_object.read())  # Loeme terve faili sisu
  ```
  Väljund:
  ```python
  Hello, World!
  Have a nice day.
  ```

- **readline(size)** - kui size pole määratud, tagastab ühe rea, liikudes ülevalt alla (ehk esimesel kutsel tagastab esimese rida, teisel teise jne kuni faili lõpuni). Vastasel juhul tagastab järgmised size baiti.
  ```python
  file_object = open('example.txt', 'r')

  print(file_object.readline())
  print(file_object.readline(5))
  ```
  Väljund:
  ```python
  Hello, World!
  Have
  ```

- **readlines(hint)** - tagastab järjendi koos kõikide failis olevate ridadega. hint määrab, kui palju ridu tuleb järjendisse panna. Selle analoogiks võib kasutada ka list(file_object) kirjapilti, mis samuti tagastab järjendi koos kõikide ridadega.
  ```python
  file_object = open('example.txt', 'r')
  print(file_object.readlines())
  ```
  Väljund:
  ```python
  ['Hello, World!\n', 'Have a nice day.']
  ```

#### LISAKS !
**Ridade itereerimine.** - kõiki ridu saab kätte ka tavalise itereerimise kaudu.
```python
file_object = open('example.txt', 'r')
for line in file_object:
    print(line)
```
Väljund:
```python
Hello, World!
Have a nice day.
```


### Faili kirjutamine
Faili kirjutamist teostatakse meetodi **write()** abil. Meetod võtab vastu sõne, seega kui on vaja kirjutada näiteks arvu, peame seda alguses muutma sõneks.
```python
file_object = open('example.txt', 'w')  # Avame faili kirjutamiseks
file_object.write('This is a new line.')
file_object.close()  # Sulgeme faili (sellest on juttu allpool)
```
Meie *example.txt* fail näeb nüüd selline välja:
```python
This is a new line.
```
Nagu näha on kogu eelmine tekst kirjutatud üle uue tekstiga. See tuleneb sellest, et me kasutasime *w* ehk write režiimi. Selleks, et lisada teksti ilma kogu faili sisu üle kirjutamata, tuleb kasutada *a+* režiimi.
```python
file_object = open('example.txt', 'a+')

file_object.write('\nThis is appended line.')
file_object.close()
```
Erisümbol (string literal) **\n** ehk line break ehk reavahetus on selle jaoks, et meie lisatud tekst asuks uuel real. Faili sisu on nüüd:
```python
This is a new line.
This is appended line.
```


### Faili sulgemine
Kui avame faili, peame ka faili sulgema, kui oleme selle kasutamise lõpetanud! Seda saab teha käsitsi, kasutades meetodit **close()**. Kui jätame faili avatuks võib programmis tekkida vigu. 
```python
file_object = open('example.txt', 'r')  # Avame faili
print(file_object.read(5))  # Loeme esimesed 5 baiti
file_object.close()  # Sulgeme faili
print(file_object.read())  # Proovime faili sisu lugeda (peaks tulema ValueError)
```
Väljund:
```python
This
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: I/O operation on closed file.
```
Nagu näha, peale seda, kui fail suletakse, ei saa sellega enam midagi teha.

#### LISAKS !
Samuti võib kasutada spetsiaalset with kontekstihaldurit (context manager), mis paneb faili automaatselt kinni peale sellega töö lõpetamist.
```python
with open('example.txt', 'r') as file:
    print(file.read())
print(file.closed)
```
Väljund:
```python
This is a new line.
This is appended line.
True
```

## Abistavad lingid

- [Tekstifailist lugemine (PyDoc)](https://ained.ttu.ee/pydoc/read_from_file.html)
- [Tekstifaili kirjutamine (PyDoc)](https://ained.ttu.ee/pydoc/write_to_file.html)
- [Sõnastik(dict) (PyDoc)](https://ained.ttu.ee/pydoc/dict.html)

## Ülesanne
### Kirjeldus
Ülesandes **top_sales_finder** tuleb lugeda failist *data.csv* toodete hinna ja koguste kohta ning kirjutada osaandmeid ka uude faili.

### Sisu
Realiseerida tuleb järgmise funktsioonid:
- **get_sales_dict(filename: str) -> dict**
  Loeb failist korrastamata andmed ja tagastab sõnastiku iga toote kohta, kus võtmeks on toote id ning väärtuseks kogu müügitulu.
- **find_average_price(filename: str) -> int**
  Arvutab failist kõigi toodete keskmise hinna.
- **find_average_quantity(filename: str) -> int**
  Arvutab failist kõigi toodete keskmise koguse.
- **get_total_quantity(filename: str) -> int**
  Arvutab failist toodete koguse.
- **get_total_price(filename: str) -> int**
  Arvutab failist toodete kogusumma.
- **get_sales_above(price: int, sales_dict: dict) -> list**
  Leiab kogutud andmetest ainult tooted, mis on üle antud hinna.
- **get_certain_product_info(product_id, sales_dict: dict) -> str**
  Leiab info otstitava toote kohta.
- **find_top_most_profitable(top: int, sales_dict: dict, file_to_write: str) -> None**
  Leiab esimesed top suurima müügituluga tooted ning kirjutab need üle teise faili [kahanemis järjekorras].


## Mall
```python
"""Data, Data Everywhere"""

import csv


def get_sales_dict(filename: str) -> dict:
    """
       Get the results and store them in the dictionary.

       Results are following the format 'Product id - sales(price*quantity).
       You have to return a dict, where the names of the competitors
       are keys and the results are values (as ints).

       :param filename: is the path to the file with the results.
       :return: a dict containing names as keys and results as values (as ints).
       """
    pass


def find_average_price(filename: str) -> int:
    """
    Find average products price. Round down to integer.

    :param filename:
    :return:
    """
    pass


def find_average_quantity(filename: str) -> int:
    """
    Find average products quantity. Round up to integer.

    :param filename:
    :return:
    """
    pass


def get_total_quantity(filename: str) -> int:
    """
    Get total quantity of all products.

    :param filename:
    :return:
    """


def get_total_price(filename: str) -> int:
    """
    Get total quantity of all products.

    :param filename:
    :return:
    """


def get_sales_above(price: int, sales_dict: dict) -> list:
    """
    Get products above certain price and put them in a list.

    :param price:
    :param sales_dict:
    :return:
    """
    pass


def get_certain_product_info(product_id, sales_dict: dict) -> str:
    """
    Get info about certain product.

    :param sales_dict:
    :return:
    """


def find_top_most_profitable(top: int, sales_dict: dict, file_to_write: str) -> None:
    """
    Find top most profitable product(s) and write them to csv file.

    The csv file must look like this:

    rank,product_id,sales
    ex.
    1,p3,500
    2,p1,350
    ...

    :param top:
    :param file_to_write:
    :param sales_dict:
    :return:
    """
```
