import random
import time

def board(Qs): #Queenleri satranç tahtası üzerinde gösterir
    n=8
    for i in range(n):
        for j in range(n):
            if j == Qs[7-i]:
                print("Q  ", end="")
            else:
                print(".  ", end="")
        print()

def randomize(): #random bir queen seti oluşturur
    Qs = [random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7)]
    return Qs

def score(Qs): # her bir Queen için kesişme sayılarına bakarak puanlamayı sağlar
    totalPoints = 0
    vPoints = 0
    dPoints = 0
    # vertical intersection
    for i in range(8):
        if Qs.count(i) > 1:
            vPoints += Qs.count(i)
    # end of VI

    # diagonal intersection
    for j in range(8):
        xmain = Qs[j]
        Qs[j] = -1
        ymain = j
        for k in range(8):
            xcheck = Qs[k]
            ycheck = k
            if abs(xmain-xcheck) == abs(ymain - ycheck):
                dPoints +=1
        Qs[j] = xmain
    #end of DI

    totalPoints = vPoints + dPoints

    return totalPoints

def movePieces(Qs): # tahtada o anda yapılabilecek en iyi hamleyi bulur ve Queen pozisyonlarını günceller
    baseScore = score(Qs)
    bestRow = -1
    bestColumn = -1
    for i in range (8):
        qtemp = Qs[i]
        for j in range(8):
            if qtemp == j:
                continue
            else:
                Qs[i] = j
                tempScore = score(Qs)
                if tempScore < baseScore:
                    baseScore = tempScore
                    bestColumn = j
                    bestRow = i
        Qs[i] = qtemp
    if bestColumn == -1 and bestRow == -1:
        return Qs
    else:
        Qs[bestRow] = bestColumn
        return Qs

def printList(aList): # "Yer Değiştirme Sayısı", "Random Restart Sayısı" ve "İşlem Süresi" değerlerini bastırır
    print("Yer Değiştirme Sayısı   Random Restart Sayısı   İşlem Süresi")
    print("---------------------   ---------------------   ------------")
    for i in range(len(aList)):
        if i == 20:
            print("Ortalama Değerler")
            print("--------------------------------------------------------------")
        for j in range(len(aList[i])):
            if j<2:
                print('{:^21}'.format(aList[i][j]), end='   ')
            else:
                print('{:10f}'.format(aList[i][j]))

def main(): # programın çalıştığı yer.
    mama = []
    tyds = 0
    trrs = 0
    tiss = 0
    for i in range(20):
        yds = -1
        rrs = 0
        Qs = randomize()
        x = True
        start = time.time()
        while x:
            baseScore = score(Qs)

            # -----   liste ve board kontrolü   -----
            #print(Qs)
            #board(Qs)
            #print(score(Qs))
            #-----  -----   -----   ------  -----

            movePieces(Qs)
            newScore = score(Qs)
            yds += 1
            if baseScore == newScore and newScore != 0:
                Qs = randomize()
                rrs += 1
                yds -= 1
            elif baseScore == newScore and newScore == 0:
                x = False
        iss = (time.time() - start)
        temp = [yds, rrs, iss]
        tyds += yds
        trrs += rrs
        tiss += iss
        mama.append(temp)
    mama.append([tyds/20, trrs/20, tiss/20])
    printList(mama)

main()

