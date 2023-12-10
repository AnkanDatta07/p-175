# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:42:42 2023

@author: Ankan Datta
"""

import matplotlib .pyplot as plt
import psutil as p
app_name_dict = {}
count = 0

for process in p.process_iter():
    count = count+1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print("NAME : ", name, "-- CPU usage", cpu_usage)
        app_name_dict.update({name : cpu_usage})
        keymax = max(app_name_dict, key = app_name_dict.get)
        print(keymax)
        keymin = min(app_name_dict, key = app_name_dict.get)
        
        app_name_list = [keymax, keymin]
        print(app_name_list)
        
        apps = app_name_dict.values()
        max_usage = max(apps)
        print(max_usage)
        min_usage = max(apps)
        print(min_usage)
        
        max_min_apps_list = [max_usage, min_usage]
        print(max_min_apps_list)
        
plt.figure(figsize = (15, 7))
plt.xlabel("Applications")
plt.ylabel("CPU usage")
plt.bar(app_name_list, max_min_apps_list, width = 0.5, color = ("blue", "green"))
plt.show()