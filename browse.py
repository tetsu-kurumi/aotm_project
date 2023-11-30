#import termcolor
from pprint import pprint
import json


try:
    with open('hands_valid.json', 'r') as f:
        print('#' * 60)
        line = f.readline()
        while line:
            hand = json.loads(line)
            print('time', hand['time'])
            print('id', hand['id'])
            print('board', hand['board'])
            print('pots')
            pots = []
            for stage in ['f', 't', 'r', 's']:
                p = [h for h in hand['pots'] if h['stage'] == stage][0]
                pots.append((p['num_players'], p['size']))
            print(pots)
            print('players')
            hand['players'] = {player['pos']: player for player in hand['players']}
            for pos in range(1, hand['num_players'] + 1):
                description = hand['players'][pos].copy()
                user = description['user']
                del description['user'], description['pos']
                print(user + ' (#' + str(pos) + ')')
                pprint(description)
                print(('· ' if pos < hand['num_players'] else '##') * 30)
            line = f.readline()
    print('Finished.')
except KeyboardInterrupt:
    print('Interrupted.')
