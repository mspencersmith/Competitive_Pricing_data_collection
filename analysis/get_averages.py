import average as av

av.avg_all('data/cleaned_pricing_data.csv','data/average_price.csv')

for i in range(1, 7):
    av.avg_rooms('data/cleaned_pricing_data.csv', i, f'data/test/average_{i}bed_price.csv')

print(av.count_rooms('data/cleaned_pricing_data.csv', 'data/bedroom_count.csv'))
