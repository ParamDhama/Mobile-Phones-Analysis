import pandas as pd
import re

data = pd.read_csv('C../Mobile-Phones-Analysis/Data/flipkart_product.csv')

disc_list = list(map(str, data['Discription']))





ram_details = []
rom_details = []
display_details = []
battery_details = []

def GetDetails():
    ram_pattern = r'(\d+)\s*GB\s*RAM'
    rom_pattern = r'(\d+)\s*GB\s*ROM'
    battery_pattern = r'(\d+)\s*mAh'
    display_pattern = r'(\d+)\s*cm'

    for spec in disc_list:
        ram_match = re.search(ram_pattern, spec)
        rom_match = re.search(rom_pattern, spec)
        display_match = re.search(display_pattern, spec)
        battery_match = re.search(battery_pattern,spec)

        if ram_match:
            ram_details.append(ram_match.group(1))
        else:
            ram_details.append("")

        if rom_match:
            rom_details.append(rom_match.group(1))
        else:
            rom_details.append("")
            
        if display_match:
            display_details.append(display_match.group(1))
        else:
            display_details.append("")

        if battery_match:
            battery_details.append(battery_match.group(1))
        else:
            battery_details.append("")



GetDetails()
print('ram',len(ram_details))
print('rom',len(rom_details))
print('DD',len(display_details))
print('BD',len(battery_details))

data['ram(GB)']=ram_details
data['rom(GB)']=rom_details
data['display(cm)']=display_details
data['battery(mAh)']=battery_details

data.drop('Discription',axis=1,inplace=True)

data.to_csv('../Mobile-Phones-Analysis/Data/flipkart_product_clean_data.csv',index=False)