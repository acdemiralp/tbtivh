import enum
import forex_python.converter

class vehicle(enum.Enum):
    automobile = 1,
    motorcycle = 2,
    other      = 3

class fuel   (enum.Enum):
    gasoline   = 1,
    electric   = 2,
    hybrid     = 3,
    other      = 4

# Reference: https://ticaret.gov.tr/gumruk-islemleri/sikca-sorulan-sorular/bireysel/bedelsiz-nakil-vasitasi-ithali/
# Last validation: 05.2022
def calculate_depreciation_multiplier      (vehicle_age):
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

# Last validation: 05.2022
def calculate_customs_tax_multiplier       (exemption_string):
    if exemption_string == 'yes' or exemption_string == 'y' or exemption_string == 'True' or exemption_string == 'true':
        return 0.0
    else:
        return 0.1

# Reference: https://www.arabam.com/blog/genel/2022-araclarin-otv-oranlari/
# Last validation: 05.2022
def calculate_special_excise_tax_multiplier(vehicle_type, fuel_type, engine_size, engine_power, price_in_lira):
    if   vehicle_type == vehicle.automobile:
        if   fuel_type == fuel.gasoline:
            if   engine_size <= 1600:
                if   price_in_lira <= 120000:
                    return 0.45
                elif price_in_lira <= 150000:
                    return 0.5
                elif price_in_lira <= 175000:
                    return 0.6
                elif price_in_lira <= 200000:
                    return 0.7
                else:
                    return 0.8
            elif engine_size <= 2000:
                if   price_in_lira <= 170000:
                    return 1.3
                else:
                    return 1.5
            else:
                return 2.2
        elif fuel_type == fuel.electric:
            if   engine_power <= 85:
                return 0.1
            elif engine_power <= 120:
                return 0.25
            else:
                return 0.6
        elif fuel_type == fuel.hybrid  :
            if   engine_size <= 1800 and engine_power >= 50:
                if   price_in_lira <= 130000:
                    return 0.45
                elif price_in_lira <= 170000:
                    return 0.5
                else:
                    return 0.8
            elif engine_size <= 2500 and engine_power >= 100:
                if   price_in_lira <= 170000:
                    return 1.3
                else:
                    return 1.5
            else:
                return 2.2
        else:
            return 0.0
    elif vehicle_type == vehicle.motorcycle:
        if engine_size <= 250:
            return 0.08
        else:
            return 0.37
    else:
        return 0.0

# Last validation: 05.2022
def calculate_value_added_tax_multiplier   ():
    return 0.18

def main():
    currency_code                         =        (input('Enter the currency you bought the vehicle in (default: EUR): '                                          ) or 'EUR'       )
    vat                                   = float  (input('Enter the VAT percentage of the country you bought the vehicle in (default: 0.18): '                    ) or 0.18        )
    vehicle_type                          = vehicle[input('Enter the type of the vehicle as one of automobile, motorcycle, other (default: automobile): '          ) or 'automobile']
    fuel_type                             = fuel   [input('Enter the type of the fuel as one of gasoline, electric, hybrid, other (default: gasoline): '           ) or 'gasoline'  ]
    price                                 = float  (input('Enter the price of the vehicle in the currency you bought it (default: 10000.0): '                      ) or 10000.0     )
    engine_size                           = int    (input('Enter the engine size of the vehicle in cubic centimeters (default: 1600): '                            ) or 1600        )
    engine_power                          = int    (input('Enter the engine power of the vehicle in kilowatts per hour if it is electric or hybrid (default: 50): ') or 50          )
    production_year                       = int    (input('Enter the production year of the vehicle (default: 2020): '                                             ) or 2020        )
    registration_year                     = int    (input('Enter the year the vehicle will be registered to the Republic of Turkey (default: 2022): '              ) or 2022        )
    exemption_string                      =        (input('Are you entitled to customs tax exemption (default: yes): '                                             ) or 'yes'       )

    vehicle_age                           = registration_year - production_year + 1

    if vehicle_age > 3:
        print('Error: The vehicle can not be imported to the Republic of Turkey because it is older than 3 years.')
        return

    currency_rate                         = forex_python.converter.CurrencyRates().get_rate(currency_code, 'TRY')
    price_without_vat                     = price * (float(1) - vat)
    price_without_vat_in_lira             = price_without_vat * currency_rate

    depreciation_multiplier               = calculate_depreciation_multiplier      (vehicle_age)
    depreciated_price_without_vat_in_lira = depreciation_multiplier * price_without_vat_in_lira

    customs_tax_multiplier                = calculate_customs_tax_multiplier       (exemption_string)
    customs_tax                           = customs_tax_multiplier * depreciated_price_without_vat_in_lira
    price_with_customs_tax                = customs_tax + depreciated_price_without_vat_in_lira

    special_excise_tax_multiplier         = calculate_special_excise_tax_multiplier(vehicle_type, fuel_type, engine_size, engine_power, depreciated_price_without_vat_in_lira)
    special_excise_tax                    = special_excise_tax_multiplier * price_with_customs_tax
    price_with_special_excise_tax         = special_excise_tax + price_with_customs_tax

    value_added_tax_multiplier            = calculate_value_added_tax_multiplier   ()
    value_added_tax                       = value_added_tax_multiplier * price_with_special_excise_tax
    final_price                           = value_added_tax + price_with_special_excise_tax

    total_tax                             = final_price - depreciated_price_without_vat_in_lira

    print ('####################################################################################################')
    print (currency_code + '/TRY currency rate                 : ' + str(currency_rate))
    print ('Origin country VAT percentage         : ' + str(vat                                   * 100          ) + ' %')
    print ('Price                                 : ' + str(price                                                ) + ' ' + currency_code + ' (' + str(price * currency_rate                ) + ' TRY)')
    print ('Price without VAT                     : ' + str(price_without_vat                                    ) + ' ' + currency_code + ' (' + str(price_without_vat_in_lira            ) + ' TRY)')
    print ('Vehicle age                           : ' + str(vehicle_age                                          ))
    print ('Depreciation multiplier               : ' + str(depreciation_multiplier               * 100          ) + ' %')
    print ('Depreciated price                     : ' + str(depreciated_price_without_vat_in_lira / currency_rate) + ' ' + currency_code + ' (' + str(depreciated_price_without_vat_in_lira) + ' TRY)')
    print ('Customs tax multiplier                : ' + str(customs_tax_multiplier                * 100          ) + ' %')
    print ('Customs tax                           : ' + str(customs_tax                           / currency_rate) + ' ' + currency_code + ' (' + str(customs_tax                          ) + ' TRY)')
    print ('Price with customs tax                : ' + str(price_with_customs_tax                / currency_rate) + ' ' + currency_code + ' (' + str(price_with_customs_tax               ) + ' TRY)')
    print ('Special excise tax (OTV) multiplier   : ' + str(special_excise_tax_multiplier         * 100          ) + ' %')
    print ('Special excise tax                    : ' + str(special_excise_tax                    / currency_rate) + ' ' + currency_code + ' (' + str(special_excise_tax                   ) + ' TRY)')
    print ('Price with special excise tax         : ' + str(price_with_special_excise_tax         / currency_rate) + ' ' + currency_code + ' (' + str(price_with_special_excise_tax        ) + ' TRY)')
    print ('Value added tax (VAT) multiplier      : ' + str(value_added_tax_multiplier            * 100          ) + ' %')
    print ('Value added tax                       : ' + str(value_added_tax                       / currency_rate) + ' ' + currency_code + ' (' + str(value_added_tax                      ) + ' TRY)')
    print ('Final price                           : ' + str(final_price                           / currency_rate) + ' ' + currency_code + ' (' + str(final_price                          ) + ' TRY)')
    print ('Total tax to be paid                  : ' + str(total_tax                             / currency_rate) + ' ' + currency_code + ' (' + str(total_tax                            ) + ' TRY)')
    print ('####################################################################################################')

if __name__ == '__main__':
    main()