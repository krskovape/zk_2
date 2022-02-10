from os import stat

#Function for loading a sequence from input txt file
def SequenceFromFile(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            if stat(file_name).st_size == 0:
                print("File is empty.")
                quit()
            data = f.read().split()
            return data
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except Exception as e:
        print(f"Unexpected error opening {file_name}: {e}")
        quit()

#Function for writing into output txt file
def WriteToFile(file_name, text):
    try:
        with open(file_name, mode="a", encoding="utf-8") as f:
            return f.write(str(text))
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except Exception as e:
        print(f"Unexpected error opening {file_name}: {e}")
        quit()

#Function for converting string elements into integers
def StrToInt(list):
    sequence = []
    index = -1
    for x in list:
        index += 1
        try:
            y = int(x)
            sequence.append(y)
        except ValueError:
            print(f"Element in position {index} in {list} is not a number and the program will skip this element")
            continue
    return sequence

#Function for ascending sorting of list values
def SortList(input_list):
    for i in range(len(input_list)):
        min = i
        for j in range(i+1, len(input_list)):
            if input_list[min] > input_list[j]:
                min = j
        input_list[i], input_list[min] = input_list[min], input_list[i]
    return input_list

#Function for intersection of two lists
def IntersectionOfLists(l1, l2):
    m = len(l1)
    n = len(l2)
    i, j = 0, 0
    intersection = []
    last = None

    while i < m and j < n:
        if l1[i] < l2[j]:
            i += 1
        elif l2[j] < l1[i]:
            j += 1
        elif l1[i] == l2[j]:
            if l1[i] != last:
                intersection.append(l1[i])
                WriteToFile("output.txt", f"{l1[i]} ")
                last = l1[i]
            i += 1
            j += 1
    return intersection

#Loading sequences from files, converting to integers and deleting duplicate elements
sequence_1 = SequenceFromFile("input1.txt")
sequence_2 = SequenceFromFile("input2.txt")
l1 = SortList(StrToInt(sequence_1))
l2 = SortList(StrToInt(sequence_2))

#Intersection
intersection = IntersectionOfLists(l1, l2)