### Turkiye Bedelsiz Tasit Ithalati Vergi Hesaplayicisi (TBTIVH)
Turkiye Cumhuriyeti'ne ozel arac ithal etmek icin odenmesi gereken gumruk, katma deger (KDV) ve ozel tuketim (OTV) vergilerini hesaplar.

### Turkish Private Vehicle Import Tax Calculator
Calculates the customs, value added (VAT) and special excise taxes that must be paid to import private vehicles into the Republic of Turkey.

### Gereksinimler / Requirements
- [Python 3](https://www.python.org/downloads/)

### Kullanim / Usage
- `pip install -r ./requirements.txt`
- `py ./tbtivh.py`

### Ornek Cikti / Example Output
```
py .\tbtivh.py
Enter the currency you bought the vehicle in (default: EUR): EUR
Enter the VAT percentage of the country you bought the vehicle in (default: 0.18): 0.18
Enter the type of the vehicle as one of automobile, motorcycle, other (default: automobile): automobile
Enter the type of the fuel as one of gasoline, electric, hybrid, other (default: gasoline): gasoline
Enter the price of the vehicle in the currency you bought it (default: 10000.0): 10000.0
Enter the engine size of the vehicle in cubic centimeters (default: 1600): 1600
Enter the engine power of the vehicle in kilowatts per hour if it is electric or hybrid (default: 50): 0
Enter the production year of the vehicle (default: 2020): 2020
Enter the year the vehicle will be registered to the Republic of Turkey (default: 2022): 2022
Are you entitled to customs tax exemption (default: yes): yes
####################################################################################################
EUR/TRY currency rate                 : 15.8078
Origin country VAT percentage         : 18.0 %
Price                                 : 10000.0 EUR (158078.0 TRY)
Price without VAT                     : 8200.0 EUR (129623.96 TRY)
Vehicle age                           : 3
Depreciation multiplier               : 60.0 %
Depreciated price                     : 4920.0 EUR (77774.376 TRY)
Customs tax multiplier                : 0.0 %
Customs tax                           : 0.0 EUR (0.0 TRY)
Price with customs tax                : 4920.0 EUR (77774.376 TRY)
Special excise tax (OTV) multiplier   : 45.0 %
Special excise tax                    : 2214.0 EUR (34998.4692 TRY)
Price with special excise tax         : 7134.000000000001 EUR (112772.84520000001 TRY)
Value added tax (KDV) multiplier      : 18.0 %
Value added tax                       : 1284.12 EUR (20299.112136 TRY)
Final price                           : 8418.12 EUR (133071.95733600002 TRY)
Total tax to be paid                  : 3498.1200000000013 EUR (55297.58133600002 TRY)
####################################################################################################
```

### Kaynaklar / Resources
- [Turkish Customs Guide (TR/EN/DE/FR)](https://gumrukrehberi.gov.tr/kategori/bireysel-slemler/bedelsiz-thal-edilen-tasit-rehberi)
- [Turkish Ministry of Trade - Vehicle Import FAQ (TR)](https://ticaret.gov.tr/gumruk-islemleri/sikca-sorulan-sorular/bireysel/bedelsiz-nakil-vasitasi-ithali)