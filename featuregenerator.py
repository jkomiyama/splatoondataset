# coding=utf-8

import sys
import pandas as pd
import numpy as np
import copy
from argparse import ArgumentParser

chargers=["bamboo14mk1","bamboo14mk2","herocharger_replica","splatcharger","splatcharger_wakame","splatscope","splatscope_wakame","liter3k","liter3k_scope","liter3k_custom","liter3k_scope_custom"]
def isCharger(weapon_type):return weapon_type=="charger"
def isShooter(weapon_type):return weapon_type=="shooter"
def isRoller(weapon_type):return weapon_type=="roller"
def isRankS(rank):return rank in ["s","s+"]
def isRankSplus(rank):return rank=="s+"
def isSpkora(weapon):return weapon in ["sshooter_collabo","octoshooter_replica"]
def is96deco(weapon):return weapon=="96gal_deco"
def is3kscope(weapon):return weapon=="liter3k_scope"
def isDynamo(weapon):return weapon=="dynamo"
def isCarbon(weapon):return weapon=="carbon"
def isNovaneo(weapon):return weapon=="nova_neo"
def isWakaba(weapon):return weapon=="wakaba"

def generate_reverse_match(row):
  newRow = {}
  newRow = copy.deepcopy(row)
  newRow['friend1_weapon'], newRow['enemy1_weapon'] = newRow['enemy1_weapon'], newRow['friend1_weapon']
  newRow['friend2_weapon'], newRow['enemy2_weapon'] = newRow['enemy2_weapon'], newRow['friend2_weapon']
  newRow['friend3_weapon'], newRow['enemy3_weapon'] = newRow['enemy3_weapon'], newRow['friend3_weapon']
  newRow['friend4_weapon'], newRow['enemy4_weapon'] = newRow['enemy4_weapon'], newRow['friend4_weapon']
  newRow['friend1_kill'], newRow['enemy1_kill'] = newRow['enemy1_kill'], newRow['friend1_kill']
  newRow['friend2_kill'], newRow['enemy2_kill'] = newRow['enemy2_kill'], newRow['friend2_kill']
  newRow['friend3_kill'], newRow['enemy3_kill'] = newRow['enemy3_kill'], newRow['friend3_kill']
  newRow['friend4_kill'], newRow['enemy4_kill'] = newRow['enemy4_kill'], newRow['friend4_kill']
  newRow['friend1_weapon_type'], newRow['enemy1_weapon_type'] = newRow['enemy1_weapon_type'], newRow['friend1_weapon_type']
  newRow['friend2_weapon_type'], newRow['enemy2_weapon_type'] = newRow['enemy2_weapon_type'], newRow['friend2_weapon_type']
  newRow['friend3_weapon_type'], newRow['enemy3_weapon_type'] = newRow['enemy3_weapon_type'], newRow['friend3_weapon_type']
  newRow['friend4_weapon_type'], newRow['enemy4_weapon_type'] = newRow['enemy4_weapon_type'], newRow['friend4_weapon_type']
  newRow['friend1_rank'], newRow['enemy1_rank'] = newRow['enemy1_rank'], newRow['friend1_rank']
  newRow['friend2_rank'], newRow['enemy2_rank'] = newRow['enemy2_rank'], newRow['friend2_rank']
  newRow['friend3_rank'], newRow['enemy3_rank'] = newRow['enemy3_rank'], newRow['friend3_rank']
  newRow['friend4_rank'], newRow['enemy4_rank'] = newRow['enemy4_rank'], newRow['friend4_rank']
  newRow['friend1_level'], newRow['enemy1_level'] = newRow['enemy1_level'], newRow['friend1_level']
  newRow['friend2_level'], newRow['enemy2_level'] = newRow['enemy2_level'], newRow['friend2_level']
  newRow['friend3_level'], newRow['enemy3_level'] = newRow['enemy3_level'], newRow['friend3_level']
  newRow['friend4_level'], newRow['enemy4_level'] = newRow['enemy4_level'], newRow['friend4_level']
  newRow['friend1_death'], newRow['enemy1_death'] = newRow['enemy1_death'], newRow['friend1_death']
  newRow['friend2_death'], newRow['enemy2_death'] = newRow['enemy2_death'], newRow['friend2_death']
  newRow['friend3_death'], newRow['enemy3_death'] = newRow['enemy3_death'], newRow['friend3_death']
  newRow['friend4_death'], newRow['enemy4_death'] = newRow['enemy4_death'], newRow['friend4_death']
#  newRow['friend1_hogehoge'], newRow['enemy1_hogehoge'] = newRow['enemy1_hogehoge'], newRow['friend1_hogehoge']
#  newRow['friend2_hogehoge'], newRow['enemy2_hogehoge'] = newRow['enemy2_hogehoge'], newRow['friend2_hogehoge']
#  newRow['friend3_hogehoge'], newRow['enemy3_hogehoge'] = newRow['enemy3_hogehoge'], newRow['friend3_hogehoge']
#  newRow['friend4_hogehoge'], newRow['enemy4_hogehoge'] = newRow['enemy4_hogehoge'], newRow['friend4_hogehoge']
  newRow['is_win'] = 1-row['is_win']
  return newRow

def generate_named_features(row):
  features = []
  numFriendCharger = int(isCharger(row['friend1_weapon_type'])) + int(isCharger(row['friend2_weapon_type'])) +  int(isCharger(row['friend3_weapon_type'])) +  int(isCharger(row['friend4_weapon_type']))
  numEnemyCharger = int(isCharger(row['enemy1_weapon_type'])) + int(isCharger(row['enemy2_weapon_type'])) +  int(isCharger(row['enemy3_weapon_type'])) +  int(isCharger(row['enemy4_weapon_type']))
  features.append("f_ch_"+str(numFriendCharger))
  features.append("e_ch_"+str(numEnemyCharger))
  numFriendShooter = int(isShooter(row['friend1_weapon_type'])) + int(isShooter(row['friend2_weapon_type'])) +  int(isShooter(row['friend3_weapon_type'])) +  int(isShooter(row['friend4_weapon_type']))
  numEnemyShooter = int(isShooter(row['enemy1_weapon_type'])) + int(isShooter(row['enemy2_weapon_type'])) +  int(isShooter(row['enemy3_weapon_type'])) +  int(isShooter(row['enemy4_weapon_type']))
  features.append("f_sh_"+str(numFriendShooter))
  features.append("e_sh_"+str(numEnemyShooter))
  numFriendRoller = int(isRoller(row['friend1_weapon_type'])) + int(isRoller(row['friend2_weapon_type'])) +  int(isRoller(row['friend3_weapon_type'])) +  int(isRoller(row['friend4_weapon_type']))
  numEnemyRoller = int(isRoller(row['enemy1_weapon_type'])) + int(isRoller(row['enemy2_weapon_type'])) +  int(isRoller(row['enemy3_weapon_type'])) +  int(isRoller(row['enemy4_weapon_type']))
  features.append("f_ro_"+str(numFriendRoller))
  features.append("e_ro_"+str(numEnemyRoller))
  numFriendRankS = int(isRankS(row['friend1_rank'])) + int(isRankS(row['friend2_rank'])) +  int(isRankS(row['friend3_rank'])) +  int(isRankS(row['friend4_rank']))
  numEnemyRankS = int(isRankS(row['enemy1_rank'])) + int(isRankS(row['enemy2_rank'])) +  int(isRankS(row['enemy3_rank'])) +  int(isRankS(row['enemy4_rank']))
  numFriendRankSplus = int(isRankSplus(row['friend1_rank'])) + int(isRankSplus(row['friend2_rank'])) +  int(isRankSplus(row['friend3_rank'])) +  int(isRankSplus(row['friend4_rank']))
  numEnemyRankSplus = int(isRankSplus(row['enemy1_rank'])) + int(isRankSplus(row['enemy2_rank'])) +  int(isRankSplus(row['enemy3_rank'])) +  int(isRankSplus(row['enemy4_rank']))
  features.append("f_rs_"+str(numFriendRankS))
  features.append("e_rs_"+str(numEnemyRankS))
  features.append("f_rsp_"+str(numFriendRankSplus))
  features.append("e_rsp_"+str(numEnemyRankSplus))
  if row["rule_name"]=="nawabari":
    features.append("rule_nw")
  elif row["rule_name"]=="area":
    features.append("rule_area")
  elif row["rule_name"]=="yagura":
    features.append("rule_yagura")
  elif row["rule_name"]=="hoko":
    features.append("rule_hoko")
  return features

allFeatures = ["f_ch_0","f_ch_1","f_ch_2","f_ch_3","f_ch_4","e_ch_0","e_ch_1","e_ch_2","e_ch_3","e_ch_4",\
               "f_sh_0","f_sh_1","f_sh_2","f_sh_3","f_sh_4","e_sh_0","e_sh_1","e_sh_2","e_sh_3","e_sh_4",\
               "f_ro_0","f_ro_1","f_ro_2","f_ro_3","f_ro_4","e_ro_0","e_ro_1","e_ro_2","e_ro_3","e_ro_4",\
               "f_rs_0","f_rs_1","f_rs_2","f_rs_3","f_rs_4","e_rs_0","e_rs_1","e_rs_2","e_rs_3","e_rs_4",\
               "f_rsp_0","f_rsp_1","f_rsp_2","f_rsp_3","f_rsp_4","e_rsp_0","e_rsp_1","e_rsp_2","e_rsp_3","e_rsp_4",\
               "rule_nw","rule_area","rule_yagura","rule_hoko",\
              ]
feature_to_ind = {}
ind_to_feature = {}
for i,f in enumerate(allFeatures):
  feature_to_ind[f] = i+1
  ind_to_feature[i+1] = f

if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument(
      '-d', '--decode',
      action = 'store_true', 
      dest = 'decode', 
  )
  parser.add_argument(
      '-f', '--filename',
      type = str,         
      dest = 'filename', 
  )

  args = parser.parse_args()
  if args.decode:
    if not args.filename:
      print "please specify filename (-f filename)";sys.exit()
    lines = [line.strip() for line in open(args.filename, "r").readlines()]
    for line in lines:
      print " ".join( map(lambda i:ind_to_feature[int(i)], line.split(" ")) )
  else: #data generation
    data = pd.read_csv(args.filename, delimiter="\t")
    for index,row in data.iterrows():
      if (index%2)==1:
        row = generate_reverse_match(row)
      named_features = generate_named_features(row)
      features = map(lambda f:feature_to_ind[f], named_features)
      label = row['is_win']
      print " ".join(map(str, sorted(features)))+" "+str(label)
 
