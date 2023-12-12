# Sieci Neuronowe
> Zadanie wykonane na pracownie specjalistyczną 'Sztuczna Inteligencja'
> Projekt ten demonstruje prosty model sieci neuronowej do klasyfikacji odzieży sportowej (dresów) na podstawie danych syntetycznych. Dane obejmują atrybuty takie jak cena, styl i jakość, a model przewiduje markę (Nike lub Adidas).
## Moduły

### 1. data_generator.py

Moduł zawiera klasę `Dres`, odpowiedzialną za generowanie syntetycznych danych do szkolenia modelu. Zawiera metody do tworzenia pojedynczych dresów i generowania listy dresów wraz z odpowiadającymi im etykietami.

### 2. data_preprocessing.py

Klasa `DataPreprocessor` w tym module dostarcza funkcji do przetwarzania danych przed przekazaniem ich do sieci neuronowej. Obejmuje metody do podziału danych na zbiory treningowe i testowe oraz normalizacji danych.

### 3. model_builder.py

Klasa `ModelBuilder` definiuje prosty model sieci neuronowej przy użyciu biblioteki Keras. Zawiera metodę do budowania i kompilowania modelu.

### 4. main.py

Importuje niezbędne moduły, tworzy instancję modelu, generuje syntetyczne dane, przetwarza dane, trenuje model i wizualizuje historię treningu.

## Wnioski

1. Testując model dla różnych funkcji aktywacji, możemy dojść do wniosku, że dla różnych przypadków odpowiednie będą inne funkcje aktywacji. Nie ma takiej, która jest dobra dla wszystkiego. Szczególnie powinniśmy zwrócić uważać przy używaniu funkcji wykładniczej, ponieważ często powoduje przepełnianie wag sieci neuronowej co uniemożliwia jej poprawne uczenie.
2. Zwiększając ilość neuronów w warstwach ukrytych możemy dostać mniejszy błąd na obiektach treningowych, ale zbyt duża ilość neuronów może powodować jej przetrenowanie.


