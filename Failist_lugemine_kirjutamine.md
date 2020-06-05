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

file_object.seek(0)  # Tagasi faili algusesse (sellest on juttu allpool)

print(file_object.read(5))  # Loeme esimesed 5 baiti
print(file_object.read(5))  # Loeme järgmised 5 baiti

```
Väljund:
```python
Hello, World!
Have a nice day.

Hello
, Wor
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

####LISAKS
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
...

### Faili sulgemine
..

## Abistavad lingid

- [Tekstifailist lugemine (PyDoc)](https://ained.ttu.ee/pydoc/read_from_file.html)
- [Tekstifaili kirjutamine (PyDoc)](https://ained.ttu.ee/pydoc/write_to_file.html)
- [Sõnastik(dict) (PyDoc)](https://ained.ttu.ee/pydoc/dict.html)

## Ülesanne
Selles ülesandes tuleb nii lugeda kui ka kirjutada faili...

## .csv fail
...

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
