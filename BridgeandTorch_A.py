import itertools

#node class'ı ve içerisinde uzunluk değerlerini, karşıya geçiş couple'ını, geri dönüşte torch'u taşıyan kişiyi
# ve parent'ını tutar
class Node():
    def __init__(self,parent=None, couple = None, turn = None):
        self.g = 0 # git gel sürelerinin toplamı
        self.h = 0 # bir sonraki geçmesi gereken en uzun süreli kimse
        self.f = 0 # g + h

        self.parent = parent
        self.couple = couple
        self.turn = turn

#köprünün sağında kalanların bulunduğu listeyi alarak olası ikili kombinasyonları oluşturur
def generate_couple(arr):
    couple_list = []
    for subset in itertools.combinations(arr, 2):
        couple_list.append(subset)
    return couple_list

#node' un g değerini o node için gidiş ve dönüş değerlerinin toplamı olarak hesaplar
def calculate_g(node, left_arr, right_arr):
    couple = node.couple
    min_couple = min(couple)
    max_couple = max(couple)
    if len(left_arr) != 0:
        min_left_list = min(left_arr)
        if min_couple < min_left_list and len(right_arr) > 2:
            node.turn = min_couple
            return max_couple + min_couple

        elif min_couple > min_left_list and len(right_arr) > 2:
            node.turn = min_left_list
            return max_couple + node.turn

        elif len(right_arr) == 2:
            node.turn = 0
            return max_couple
    else:
        return max_couple + min_couple

#node'un h değerini kendisinden sonra gelip karşıya geçmesi gereken en büyük değer olarak hesaplar
def calculate_h(node, right_arr):
    maxCouple = max(node.couple)
    minCouple = min(node.couple)
    if len(right_arr) == 0:
        return 0
    elif maxCouple == max(right_arr):
        tempList = right_arr.copy()
        tempList.remove(maxCouple)
        if minCouple == max(tempList) and len(tempList)>1:
            temp2 = tempList.copy()
            temp2.remove(minCouple)
            return max(temp2)
        else:
            return max(tempList)
    else:
        return max(right_arr)

#node'un f uzunluğunu  g+h şeklinde hesaplar
def calculate_f(node):
    node.f=node.g + node.h
    return node.f

#seçilen node'un sağ listeden sol listeye geçmesi için gerekli olan işlemleri yapar
def addLeftRight(node, left_list, right_list):
    couple = node.couple
    min_couple = min(couple)
    max_couple = max(couple)
    min_left_list = min(left_list)

    if min_couple < min_left_list and len(right_list) > 2:
        right_list.remove(max_couple)
        left_list.append(max_couple)
        node.turn = min_couple

    elif min_couple > min_left_list and len(right_list) > 2:
        right_list.append(min_left_list)
        node.turn = min_left_list
        left_list.remove(min_left_list)
        left_list.append(min_couple)
        left_list.append(max_couple)
        right_list.remove(max_couple)
        right_list.remove(min_couple)

    elif len(right_list) == 2:
        left_list.append(min_couple)
        left_list.append(max_couple)
        right_list.remove(max_couple)
        right_list.remove(min_couple)
        node.turn = 0

#tüm a* algoritması ile ilgili işlemler burada gerçekleşir
def Solver(start_couple, left_list, right_list, time):

    start_node = Node(None, start_couple, min(start_couple))
    start_node.h = calculate_h(start_node, right_list)
    start_node.g = calculate_g(start_node,left_list,right_list)
    start_node.f = calculate_f(start_node)

    count = 0
    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):#f değerine göre en iyi node seçimi burada gerçekleşir
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node.couple == start_node.couple:
            left_list.append(max(start_node.couple))
            right_list.remove(max(start_node.couple))
            start_node.turn = min(start_node.couple)

        else:
            addLeftRight(current_node, left_list, right_list)

        print("Şuandaki Çift: ",current_node.couple)
        count += current_node.turn + max(current_node.couple)

        if  count == time: #sona ulşılınca path döndürme işlemi burada gerçekleşir
            path = []
            current = current_node
            while current is not None:
                path.append(current.couple)
                current = current.parent
            return path[::-1]

        children = []
        for new_couple in generate_couple(right_list): #sağ listede kalanlara göre olası çiftler oluşturulur
            node_couple = new_couple
            new_node = Node(current_node, node_couple)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            #oluşturulan child için g,h,f değerlerinin hesaplandırılması
            child.g = calculate_g(child, left_list, right_list)
            child.h = calculate_h(child, right_list)
            child.f = calculate_f(child)

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)

def main():

    left_arr = []
    right_arr = [1,2,5,8]
    start_arr = [1,2,5,8]
    time = 15

    #ilk node için doğru node seçilip istenilen sonuç elde edilene kadar devam edilir.
    for x in generate_couple(start_arr):
        path = Solver(x, left_arr,right_arr, time)
        if path is not None:
            print("Olası yol: ",path)
            break
        else:
            continue

if __name__ == '__main__':
    main()