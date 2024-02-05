
import random
Kelime_listesi=["system", "data", "algorithm", "such", "base", "node", "model", "case", "program", "information", "set",
                "code", "function", "process", "application", "software", "class", "point", "type", "network", "tree",
                "object", "element", "input", "operation", "level", "memory", "table", "order", "file", "variable", "language",
                "write",	"list", "structure", "compute", "sequence", "computer", "bit", "probability", "machine", "array",
                "page", "error", "step", "search", "most", "path", "graph", "web", "length", "several", "security", "proof",
                "access", "obtain", "matrix", "task", "image", "form", "return", "interface", "resource", "address",
                "implementation", "loop",	"first", "read", "location", "hardware", "behavior", "programming", "field", "key",
                "parameter", "distribution", "definition", "instance", "interaction", "internet", "representation",	"edge",	"stack",
                "return", "procedure", "link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
                "detection", "write","execute", "least", "key"]

kucuk_harf="abcdefghijklmnoprstuvyzxq"
sesli_harf="aeoui"
sessiz_harf="bcdfghjklmnprstvyzxq"
tahmin_sayisi=0
puan=0
harf_sayisi = 0
secim=1
while secim==1:
    if secim==1:
        tahmin_sayisi = 0
        puan = 0
        harf_sayisi = 0
        input("Oyuna başlamak icin bir tuşuna basin")
        kelime=random.choice(Kelime_listesi)
        gelen_harfler=[]
        for i in kelime:
            harf_sayisi+=1
        degisken=list("-"*harf_sayisi)
        print("Kelimede bulunan harf sayisi= ",harf_sayisi)

        if harf_sayisi // 2 != 0:  # tahmin sayisi hesaplamak için
            tahmin_sayisi = (harf_sayisi + 1) // 2
        else:
            tahmin_sayisi = harf_sayisi // 2

        while True:
            if tahmin_sayisi==0:
                print("KAYBETTİNİZ!!")
                exit()
            if ''.join(degisken)!=kelime:
                print("Kalan tahmin hakkınız:", tahmin_sayisi, end=" ")
                print("Puan:", puan)
                print(' '.join(degisken), end='\n')
                tahmin=input("Harf tahmin ediniz:")
                if tahmin!=kucuk_harf:
                    tahmin=tahmin.lower()
                    if tahmin in kelime:
                        for i in range(len(kelime)):
                            if tahmin==kelime[i]:
                                degisken[i]=tahmin
                                if tahmin not in sesli_harf:
                                    puan=puan+2
                                else:
                                    puan=puan+3
                    else:
                        tahmin_sayisi-=1
                        puan-=4

            else:
                print("KAZANDINIZ!!")
                secim=int(input("1-Yeni kelimeye geçiş \n2-Çıkış\n"))
                break
print("Çıkış yaptınız")