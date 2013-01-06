#!/usr/bin/env python3

import os 
from subprocess import call, check_output

filelist = os.listdir("./images")
newlist = []

for i in filelist:
    print(i)
    [name,ext] = os.path.splitext(i)
    if name.endswith("_z"):
        print("ends with _z, checking...")
        if name.rstrip("_z")+ext in filelist:
            print("bigger file coming, deleting")
            os.unlink(os.path.join("images",i))
            continue
        else:
            print("no larger file exists...")
    newlist.append(i)

for i in newlist:
    print(i)
    [name,ext] = os.path.splitext(i)
    w = check_output(['/usr/bin/identify','-format','%w','images/'+i])    
    h = check_output(['/usr/bin/identify','-format','%h','images/'+i])    
    print(int(w),'x',int(h))
   
    if ( int(w) > 1280 or int(h) > 1280):
        print("_z@2x")
        zx2 = ['/usr/bin/convert','images/' + i,'-resize','1280x1280>','-quality','70',
                'images/' + name + '_z@2x' + ext]
        call(zx2)
    if ( int(w) > 640 or int(h) > 640):
        print("_z")
        z = ['/usr/bin/convert','images/' + i,'-resize','640x640>','-quality','90','images/' + name + '_z' + ext]
        call(z)
    print("Done.")
