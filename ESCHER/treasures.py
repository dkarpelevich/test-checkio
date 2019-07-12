def specific_weight(info):
    gold_gram = info['golden coin']['price'] / info['golden coin']['weight']
    silver_gram = info['silver coin']['price'] / info['silver coin']['weight']
    ruby_gram = info['ruby']['price'] / info['ruby']['weight']
    return {'golden coin': gold_gram, 'silver coin': silver_gram, 'ruby': ruby_gram}

def treasures(info: dict, limit: float):
    sw = sorted(specific_weight(info).items(), key=lambda a: a[1], reverse=True)
    limit = limit * 1000
    treasures_dict = {'golden coin': 0, 'silver coin': 0, 'ruby': 0}
    return_list = []
    for i in range(len(sw)):
        treasure_total_weight = info[sw[i][0]]['weight'] * info[sw[i][0]]['amount']
        max_amount_in_backpack = limit // info[sw[i][0]]['weight']
        if info[sw[i][0]]['amount'] <= max_amount_in_backpack:
            treasures_dict[sw[i][0]] = info[sw[i][0]]['amount']
        else:
            treasures_dict[sw[i][0]] = max_amount_in_backpack
        limit = limit - treasure_total_weight
        if limit <= 0 or i == len(sw) - 1:
            if treasures_dict['golden coin'] > 0:
                return_list.append('golden coin: ' + str(int(treasures_dict['golden coin'])))
            if treasures_dict['silver coin'] > 0:
                return_list.append('silver coin: ' + str(int(treasures_dict['silver coin'])))
            if treasures_dict['ruby'] > 0:
                return_list.append('ruby: ' + str(int(treasures_dict['ruby'])))
            return return_list

if __name__ == '__main__':
    # print("Example:")
    # print(treasures({'golden coin':
    #                     {'price': 100, 'weight': 50, 'amount': 200},
    #                  'silver coin':
    #                     {'price': 10, 'weight': 20, 'amount': 1000},
    #                  'ruby':
    #                     {'price': 1000, 'weight': 200, 'amount': 2}}, 5))
    # assert treasures({'golden coin':
    #                      {'price': 100, 'weight': 50, 'amount': 200},
    #                   'silver coin':
    #                      {'price': 10, 'weight': 20, 'amount': 1000},
    #                   'ruby':
    #                      {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
    #                       'golden coin: 92', 'ruby: 2']
    assert treasures({'golden coin':
                         {'price': 100, 'weight': 50, 'amount': 100},
                      'silver coin':
                         {'price': 10, 'weight': 20, 'amount': 100},
                      'ruby':
                         {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
                          'golden coin: 100', 'silver coin: 100', 'ruby: 1']
    print("Coding complete? Click 'Check' to earn cool rewards!")
