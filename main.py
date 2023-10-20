import os
import csv
import sys
import matplotlib.pyplot as plt
import re

"""
使いかた:
1. 空のフォルダーにこのファイルを移行する
2. このファイルと同じディレクトリにdataとgraphsというファイルを作る
3. dataの中にオシロからとれたフォルダー (恐らく、名前はALL####)を全てそのままdataに入れる
4. 1 channel しかとっていないデータがある場合それをコピーして、同じのが二つあるようにしてください
5. pip で上のincludeをまだ居れていない人は pip install (include名) をターミナルにそれぞれ入れて、ダウンロードしてください
6. すく下のpathの変数を自分のpcのdataがある場所に変えてください

何か上手くいかなかった場合、ぜひ言っていただけると対応します。

"""

path = "C:/Users/ukinu/uKinuly/data/医工学実験1/data"

for curDir, dirs, files in os.walk(path):
    fcount=0
    for f in files:
        print(dirs)
        if fcount==0:
            
            file = open(os.path.join(curDir, f))
            csvreader = csv.reader(file)
            t = []
            data1=[]
            ig=0
            for row in csvreader:
                if ig<18:
                    ig+=1
                else:
                    t.append(float(row[3]))
                    data1.append(float(row[4]))
            file.close()
        if fcount==1:
            print(f)
            file = open(os.path.join(curDir, f))
            csvreader = csv.reader(file)
            data2=[]
            ig=0
            for row in csvreader:
                if ig<18:
                    ig+=1
                else:
                    data2.append(float(row[4]))
            fig, ax = plt.subplots()
            ax.plot(t, data1,label="channel1")
            ax.plot(t, data2,label="channel2")
            plt.xlabel("Time [s]")
            plt.ylabel("Voltage [V]")
            ax.legend()
            fig.savefig("graphs/"+"_".join(re.split("/|\\\\",curDir)[-2:])+".png")
        fcount+=1
        if fcount==4:
            fcount=0