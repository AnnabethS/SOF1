def rod_cutting(length, prices):
    # if length==1:
    #     return prices[0]
    # else:
    #     best = [0, 0]
    #     for i in range(0, length):
    #         x = [0,0]
    #         if i==0:
    #             x[0] = prices[length-1]
    #             x[1] = 0
    #         else:
    #             x[0] = rod_cutting(length - i, prices)
    #             x[1] = i

    #         if i==0:
    #             x_total = x[0]
    #         else:
    #             x_total = x[0] + prices[x[1]-1]
    #         if best[1]==0:
    #             best_total = best[0]
    #         else:
    #             best_total = best[0] + prices[best[1]]

    #         if x_total > best_total:
    #             best = x.copy()

    #     if best[1]==0:
    #         return best[0]
    #     else:
    #         return best[0] + prices[best[1]]

    if length==1:
        return [prices[0], 0]
    else:
        best = [0, 0]
        for i in range(0, length):
            x = [0,0]
            if i==0:
                x[0] = prices[length-1]
                x[1] = 0
            else:
                section = rod_cutting(length - i, prices)
                x[0] = section[0]
                x[1] = section[1]

            if x[1]==0:
                x_total = x[0]
            else:
                x_total = x[0] + prices[x[1]-1]

            if i!=0:
                x_total = x_total + prices[i-1]

            if best[1]==0:
                best_total = best[0]
            else:
                best_total = best[0] + prices[best[1]]

            if x_total > best_total:
                best = x.copy()

        if best[1]==0:
            return [best[0], 0]
        else:
            return [best[0], prices[best[1]]]

#print(rod_cutting(4, [1, 5, 8, 9, 10, 17]))



def rod_cutting_2(length, prices):
    if length==1:
        return prices[0]
    else:
        best = 0
        for i in range(length):
            if i==0:
                best = prices[length-1]
            else:
                bestSubSection = rod_cutting_2(length-i, prices)
                if bestSubSection + prices[i - 1] > best:
                    best = bestSubSection + prices[i - 1]
        return best

print(rod_cutting_2(4, [1, 5, 8, 9, 10, 17]))

