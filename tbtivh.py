import enum
import forex_python

class vehicle_type(enum.Enum):
    automobile = 1,
    motorcycle = 2,
    other      = 3

class fuel_type(enum.Enum):
    gasoline = 1,
    electric = 2,
    hybrid   = 3,
    other    = 4

# Reference: https://ticaret.gov.tr/gumruk-islemleri/sikca-sorulan-sorular/bireysel/bedelsiz-nakil-vasitasi-ithali/
# Last validation: 05.2022
def calculate_depreciation_multiplier(vehicle_age):
    if vehicle_age == 1:
        return 0.8
    if vehicle_age == 2:
        return 0.7
    if vehicle_age == 3:
        return 0.6
    if vehicle_age == 4:
        return 0.5
    if vehicle_age == 5:
        return 0.4
    if vehicle_age == 6:
        return 0.3
    if vehicle_age >  6:
        return 0.2

# Reference: https://www.arabam.com/blog/genel/2022-araclarin-otv-oranlari/
# Last validation: 05.2022
def calculate_special_excise_tax_multiplier(engine_size, price_in_lira):
    if   engine_size <= 1600:
        if   price_in_lira < 120000:
            return 0.45
        elif price_in_lira < 150000:
            return 0.5
        elif price_in_lira < 175000:
            return 0.6
        elif price_in_lira < 200000:
            return 0.7
        else:
            return 0.8
    elif engine_size <= 2000:
        if   price_in_lira < 170000:
            return 1.3
        else:
            return 1.5
    else:
        return 2.2

def main():
    price                         = float(input("Enter the car's price in a currency of your choice (e.g. 10000): "))
    vat                           = float(input("Enter the VAT percentage (e.g. 0.18) of the origin country     : "))
    production_year               = int  (input("Enter the car's production year                                : "))
    registration_year             = int  (input("Enter the year the car will be registered to Turkish customs   : "))

    price_without_vat             = price * (1.0 - vat)
    depreciation                  = calculate_depreciation_multiplier(registration_year - production_year + 1)
    depreciated_price             = depreciation * price_without_vat

    special_excise_tax_multiplier = 0.8
    special_excise_tax            = depreciated_price * special_excise_tax_multiplier

    print("Origin Country VAT                    : " + str(vat              ))
    print("Price                                 : " + str(price            ))
    print("Price without VAT                     : " + str(price_without_vat))
    print("Production year                       : " + str(production_year  ))
    print("Registration year (to Turkish customs): " + str(registration_year))
    print("Depreciation due to vehicle age       : " + str(depreciation     ))
    print("Depreciated price                     : " + str(depreciated_price))

if __name__ == "__main__":
    main()