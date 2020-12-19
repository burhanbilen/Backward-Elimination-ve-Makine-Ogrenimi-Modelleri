# Backward Elimination ve Makine Öğrenimi Modelleri

Bu çalışmada, belirlenen bir veriseti üzerinde Geri Eleme yöntemiyle birçok makine öğrenmesi modeline göre gereksiz görünen kolonlar elenmiştir. Bu bağlamda, p-value değerine göre veri kolonu elemeleri yapılarak R-Square değeri artırılmaya çalışılmıştır.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Aşağıda verilen kodun çıktısı olarak, veri kolonları arasındaki ilişkinin görülebilmesi için Korelasyon Matrisi verilmiştir.

import pandas as pd
df = pd.read_csv('veri.csv', encoding='utf-8')
print(df.corr())

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

|               | Calisan ID | UnvanSeviyesi | Kidem    | Puan     | maas     |
| ------------- |:----------:|:-------------:|:--------:|:--------:|---------:|
|Calisan ID     | 1.000000   | 0.331847      | 0.206278 |-0.251278 | 0.226287 |
|UnvanSeviyesi  | 0.331847   | 1.000000      |-0.125200 | 0.034948 | 0.727036 |
|Kidem          | 0.206278   |-0.125200      | 1.000000 | 0.322796 | 0.117964 |
|Puan           |-0.251278   | 0.034948      | 0.322796 | 1.000000 | 0.201474 |
|maas           | 0.226287   | 0.727036      | 0.117964 | 0.201474 | 1.000000 |
