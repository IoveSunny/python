#!/usr/bin/python
#coding:utf-8


from os import popen

for i in range(4):
	global info
	# Ubuntu cpufreq* 来控制 cpu frequence（CPU频率）
	popen("cpufreq-set -c "+str(i)+" -d 800M && cpufreq-set -c "+str(i)+" -u 1500M")

print popen("cpufreq-info").read()
