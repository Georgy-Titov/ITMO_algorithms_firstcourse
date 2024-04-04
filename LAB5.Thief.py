def thief(m, k, exhibitions):
    sorted_exhibitions = sorted(exhibitions, key=compare_exhibit, reverse=True)
    total_stolen_cost = 0
    stolen = []

    while m != 0:
        curent_weight = 0
        for j in sorted_exhibitions:
            if j.status != "Stolen" or j.status != "Heavy":
                if curent_weight + j.weight <= k:
                    curent_weight += j.weight
                    stolen.append(j)
                    j.status = "Stolen"
                    total_stolen_cost += j.cost
                elif len(stolen) != 0 and curent_weight == k:
                    break
                elif j.weight > k:
                    j.status = "Heavy"
        m -= 1


    print(f"Было украдено {len(stolen)} экспанатов на стоимость {total_stolen_cost} руб.")



class Exhibit:
    def __init__(self, cost, weight, status=None):
        self.cost = cost
        self.weight = weight
        self.status = status

    def __str__(self):
        return f"Цена экспоната: {self.cost}\n" \
               f"Вес экспоната: {self.weight}\n"


def compare_exhibit(a):
    return a.cost / a.weight


Exhibits = []
N = int(input("Введите кол-во экспонатов: "))
for i in range(N):
    c, w = map(int, input("Введите стоимость и вес экспоната: ").split())
    Exhibits.append(Exhibit(c, w))

M = int(input("Введите кол-во ходок вора: "))
K = int(input("Введите вместимость рюкзака (кг): "))

thief(M, K, Exhibits)
