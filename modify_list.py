def modify_list(str_list):
    """
    str_list: list(list(str))

    Return: list(list(str))

    Example:
    
    Input:
    1 2 3 4 5 6 7
    2 4 5 6 7 3 9
    
    Output:
    1 2 3 4
    1 5 6 7
    2 4 5 6
    2 7 3 9
    """
    length = (len(str_list[0]) - 1) // 2
    res = []

    for string in str_list:
        for i in range(2):
            row = []
            row.append(string[0]) # append the first element of each row
            if i == 0:
                row.extend(string[1:length + 1]) # append first half
            else:
                row.extend(string[length + 1:]) # append the second half
            res.append(row)
    return res

if __name__ == "__main__":
    res = []
    res = modify_list([[1,2,3,4,5,6,7],[2,4,5,6,7,3,9],[3,5,4,2,4,6,5],[4,9,5,2,4,24,2]])
    print(res)
