class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        items = {}
        foods = []
        tables = []
        for order in orders:
            if order[2] not in foods:
                foods.append(order[2])
            if order[1] not in items:
                tables.append(int(order[1]))
                items[order[1]] = {order[2]: 1}
            else:
                if order[2] in items[order[1]]:
                    items[order[1]][order[2]] += 1
                else:
                    items[order[1]][order[2]] = 1
        foods.sort()
        result = []
        result.append(["Table"] + foods)
        tables.sort()
        print(tables)
        for table in tables:
            foodArr = [str(table)]
            for food in foods:
                if food in items[str(table)]:
                    foodArr.append(str(items[str(table)][food]))
                else:
                    foodArr.append("0")
            result.append(foodArr)
        return result
        