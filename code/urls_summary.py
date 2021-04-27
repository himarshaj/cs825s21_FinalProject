#!/usr/bin/env python3

import io


if __name__ == "__main__":
	with open("urls_filtered.csv","r") as f:
		lines = f.readlines()
	dic = {}
	lines.pop(0)
	for line in lines:
		#print(line + "==========")
		domain, count_list = line.split(",",1)
		domain = domain.strip('"')
		count_list = (count_list.strip('"\n')).split(",")
		count_list = [int(i) for i in count_list]
		if domain in dic:
			old = dic[domain]
			old.append(count_list)
			dic[domain] = old
		else:
			dic[domain] = [count_list]
	newdic = {}
	for key in dic:
		l = dic[key]
		sum_l = [sum(i) for i in zip(*l)]
		newdic[key] = sum_l
	#print(newdic)
	with open("urls_summary.csv","w") as g:
		g.write('"domain","tweet_count","retweet_count_metadata","quote_count_metadata","tweet_count_by_community_0","retweet_count_by_community_0","quote_count_by_community_0","tweet_count_by_community_1","retweet_count_by_community_1","quote_count_by_community_1","tweet_count_by_community_2","retweet_count_by_community_2","quote_count_by_community_2","tweet_count_by_community_3","retweet_count_by_community_3","quote_count_by_community_3","tweet_count_by_community_4","retweet_count_by_community_4","quote_count_by_community_4","tweet_count_by_suspended_users","retweet_count_by_suspended_users","quote_count_by_suspended_users"\n')
		for key in newdic:
			l = newdic[key]			
			string_ints = [str(int) for int in l]
			str_of_ints = ""
			str_of_ints = ",".join(string_ints)
			g.write(f"{key},{str_of_ints}\n")
