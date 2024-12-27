import random


class Item:
    def __init__(self, i, w):
        self.ID = i
        self.weight = w

class Solution:
    def __init__(self):
        self.bins = []

class Bin:
    def __init__(self):
        self.capacity = 0
        self.emptySpace = 0
        self.tot_weight = 0
        self.assigned_items = []


def report_solution(sol):
    print('Best Fit:', len(sol.bins))

    # i = 1
    # for b in sol.bins:
    #     its = b.assigned_items
    #     stri = ','.join([str(it.ID) for it in its])
    #     idd = 'P' + str(i)
    #     print(idd, stri, 'Utilization:', b.tot_weight)
    #     i += 1


def sortGroups(listOFGroups: list):
    listOFGroups.sort(key=lambda x: x.weight, reverse=True)


def BestFit(sol, all_items, bin_capacity):
    sol.bins.clear()
    total_items = len(all_items)

    for i in range(0, total_items):

        to_be_assigned = all_items[i]
        index_of_best_bin = -1
        minimum_empty_space = 1000000

        total_open_bins = len(sol.bins)

        for b in range(0, total_open_bins):
            trial_bin = sol.bins[b]
            if trial_bin.emptySpace >= to_be_assigned.weight:
                if trial_bin.emptySpace < minimum_empty_space:
                    minimum_empty_space = trial_bin.emptySpace
                    index_of_best_bin = b

        if index_of_best_bin != -1:
            bin_of_insertion: Bin = sol.bins[index_of_best_bin]
            bin_of_insertion.assigned_items.append(to_be_assigned)
            bin_of_insertion.tot_weight = bin_of_insertion.tot_weight + to_be_assigned.weight
            bin_of_insertion.emptySpace = bin_of_insertion.emptySpace - to_be_assigned.weight
        else:
            new_bin = Bin()
            new_bin.capacity = bin_capacity
            new_bin.tot_weight = 0
            new_bin.emptySpace = bin_capacity

            sol.bins.append(new_bin)
            new_bin.assigned_items.append(to_be_assigned)
            new_bin.tot_weight = new_bin.tot_weight + to_be_assigned.weight
            new_bin.emptySpace = new_bin.emptySpace - to_be_assigned.weight
    # print('Best Fit termination')


def FirstFit(sol, all_items, busCapacity):
    sol.bins.clear()
    total_items = len(all_items)

    for i in range(0, total_items):

        to_be_assigned = all_items[i]
        index_of_bin_to_be_inserted = -1
        total_open_bins = len(sol.bins)

        for b in range(0, total_open_bins):
            trial_bin: Bin = sol.bins[b]

            if trial_bin.emptySpace >= to_be_assigned.weight:
                index_of_bin_to_be_inserted = b
                break

        if index_of_bin_to_be_inserted != -1:
            bin_of_insertion: Bin = sol.bins[index_of_bin_to_be_inserted]
            bin_of_insertion.assigned_items.append(to_be_assigned)
            bin_of_insertion.tot_weight = bin_of_insertion.tot_weight + to_be_assigned.weight
            bin_of_insertion.emptySpace = bin_of_insertion.emptySpace - to_be_assigned.weight
        else:
            new_bin = Bin()
            new_bin.capacity = busCapacity
            new_bin.tot_weight = 0
            new_bin.emptySpace = busCapacity

            sol.bins.append(new_bin)

            new_bin.assigned_items.append(to_be_assigned)
            new_bin.tot_weight = new_bin.tot_weight + to_be_assigned.weight
            new_bin.emptySpace = new_bin.emptySpace - to_be_assigned.weight
    print('First Fit termination')




def solve_bin_packing_from_orders(order_list, capacity):
    all_items = []
    for ord in order_list:
        dimension = ord.width
        level = ord.order_level
        for i in range(level):
            it = Item(len(all_items), dimension)
            all_items.append(it)
    bin_capacity = capacity

    sol = Solution()

    all_items.sort(key=lambda a: a.weight, reverse=True)

    # print('Best Fit')
    BestFit(sol, all_items, bin_capacity)
    report_solution(sol)
