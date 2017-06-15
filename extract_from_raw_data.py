# coding=utf-8

import gzip
import traceback

import ujson as json
import os
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

def main():
    start = 500000
    end =  1027674
    battle_ids = range(start, end)
    
    if len(sys.argv)<2:
      print "usage: this datadir"
      sys.exit()

    with open('./battles.tsv', 'w') as out:
        out.write(get_header_line())
        out.write('\n')
        write_to(extract_fields(read_file(battle_ids)), out)


def read_file(battle_ids):
    for battle_id in battle_ids:
        try:
            filename = os.path.join(sys.argv[1], str(battle_id)+".json.gz")
            with gzip.open(filename, "rt") as f:
#            with gzip.open(filename, "rt", encoding="utf-8") as f:
                try:
                    raw = f.read(-1)
                    if len(raw) == 0:
                        continue

                    battle = json.loads(raw)
                    yield battle

                except Exception as e:
                    print('=========================')
                    print(e)
                    print(battle)
                    traceback.print_exc()
        except Exception as ee:
            print(ee)
            continue


def extract_player_fields(p):
    return {
        'weapon': p['weapon']['key'],
        'weapon_type': p['weapon']['type']['key'],
        'rank': p['rank']['key'] if isinstance(p.get('rank'), dict) else '',
        'level': str(p['level']),
        'kill': str(p['kill']),
        'death': str(p['death'])
    }


def extract_fields(battles):
    valid_count = 0
    for battle in battles:
        if 'error' in battle:
            continue

        if battle['players'] is None:
            print('No player data. Skip')
            continue

        if len(battle['players']) != 8:
            print('Not full member match. Skip')
            continue

        id = battle.get('id')
        url = battle.get('url')
        rule_name, rule_mode = extract_rule_mode_name(battle)
        map_name = extract_map_name(battle)
        is_win = 1 if battle['result'] == 'win' else 0

        players = battle['players']
        friends = list(map(
            extract_player_fields,
            filter(lambda p: p['team'] == 'my' and p.get('weapon'), players)))
        enemies = list(map(
            extract_player_fields,
            filter(lambda p: p['team'] == 'his' and p.get('weapon'), players)))

        if len(friends) != 4 or len(enemies) != 4:
            print('No full member match. Skip')
            continue

        print(id)

        # =========================================================
        values = [
            str(id), url, rule_name, map_name, str(is_win),
        ]
        for f in friends:
            values.extend([
                f['weapon'],
                f['weapon_type'],
                f['rank'],
                f['level'],
                f['kill'],
                f['death'],
            ])

        for e in enemies:
            values.extend([
                e['weapon'],
                e['weapon_type'],
                e['rank'],
                e['level'],
                e['kill'],
                e['death'],
            ])
        yield values
        valid_count += 1

    print("Validated data count {0}".format(valid_count))


def write_to(records, output):
    for record in records:
        output.write('\t'.join(record))
        output.write('\n')


def get_header_line():
    fields = [
        'id', 'url', 'rule_name', 'map_name', 'is_win',
    ]
    for y in ['friend', 'enemy']:
        for x in [1, 2, 3, 4]:
            fields.extend([
                '{0}{1}_weapon'.format(y, x),
                '{0}{1}_weapon_type'.format(y, x),
                '{0}{1}_rank'.format(y, x),
                '{0}{1}_level'.format(y, x),
                '{0}{1}_kill'.format(y, x),
                '{0}{1}_death'.format(y, x)
            ])
    return '\t'.join(fields)


def extract_rule_mode_name(battle):
    rule = battle.get('rule')
    rule_name = ''
    rule_mode = ''
    if rule:
        rule_name = rule['key']
        mode = rule.get('rule')
        if mode:
            rule_mode = mode['key']
    return rule_name, rule_mode


def extract_map_name(battle):
    map_name = ''
    map_info = battle.get('map')
    if map_info:
        map_name = map_info['key']
    return map_name


if __name__ == "__main__":
    main()
