class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        def allEqual(list):
            return all(i == list[0] for i in list) if len(list)>1 else True
        loop = 2*len(students)
        while len(sandwiches)>=0 and loop !=0:
            if allEqual(sandwiches) and allEqual(students) and sandwiches[0] != students[0]:
                break
            # if allEqual(sandwiches) and allEqual(students) :
            #     break
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                loop = 2*len(students)
            else:
                returned = students.pop(0)
                students.append(returned)
                loop = loop-1
                
        return len(sandwiches)